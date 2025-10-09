import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import json

class SMERAGPipeline:
    def __init__(self, data_path="data/sme_data.csv"):
        import os
        # Try multiple possible paths for the CSV file
        possible_paths = [
            data_path,
            os.path.join(os.path.dirname(__file__), '..', 'data', 'sme_data.csv'),
            os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sme_data.csv'),
            '../data/sme_data.csv'
        ]
        
        self.data_path = None
        for path in possible_paths:
            if os.path.exists(path):
                self.data_path = path
                break
        
        if self.data_path is None:
            self.data_path = data_path  # Use original path as fallback
        
        self.client = chromadb.Client()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.collection = None
        
    def load_and_process_data(self):
        """Load CSV data and create text chunks for embedding"""
        try:
            df = pd.read_csv(self.data_path)
        except FileNotFoundError:
            # Create sample data if file not found
            df = pd.DataFrame({
                'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', 'Sep-23', 'Oct-23'],
                'Sales (INR)': [500000, 480000, 520000, 600000, 550000, 450000, 620000, 580000, 610000, 590000],
                'Expenses (INR)': [300000, 320000, 310000, 340000, 330000, 360000, 350000, 340000, 355000, 345000],
                'Customers': [200, 190, 210, 250, 230, 180, 260, 240, 255, 245],
                'Inventory Cost (INR)': [120000, 130000, 125000, 140000, 135000, 145000, 138000, 142000, 140000, 139000],
                'Marketing Spend (INR)': [30000, 28000, 35000, 40000, 37000, 25000, 42000, 39000, 41000, 38000]
            })
        
        # Create text representations of each row
        documents = []
        metadatas = []
        ids = []
        
        for idx, row in df.iterrows():
            # Create descriptive text for each row
            text = f"""Month: {row['Month']}
Sales: ₹{row['Sales (INR)']}
Expenses: ₹{row['Expenses (INR)']}
Profit: ₹{row['Sales (INR)'] - row['Expenses (INR)']}
Customers: {row['Customers']}
Inventory Cost: ₹{row['Inventory Cost (INR)']}
Marketing Spend: ₹{row['Marketing Spend (INR)']}
Profit Margin: {((row['Sales (INR)'] - row['Expenses (INR)']) / row['Sales (INR)'] * 100):.1f}%"""
            
            documents.append(text)
            metadatas.append(row.to_dict())
            ids.append(f"record_{idx}")
        
        return documents, metadatas, ids
    
    def create_vector_store(self):
        """Create ChromaDB collection and embed documents"""
        documents, metadatas, ids = self.load_and_process_data()
        
        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name="sme_business_data"
        )
        
        # Generate embeddings
        embeddings = self.model.encode(documents).tolist()
        
        # Add to ChromaDB
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"✅ Added {len(documents)} records to vector store")
    
    def query(self, query_text, n_results=3):
        """Query the vector store"""
        if not self.collection:
            self.collection = self.client.get_collection("sme_business_data")
        
        query_embedding = self.model.encode([query_text]).tolist()
        
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        return results

# Test the RAG pipeline
if __name__ == "__main__":
    rag = SMERAGPipeline()
    rag.create_vector_store()
    
    # Test query
    results = rag.query("What was the profit in May 2023?")
    print("Query results:", results['documents'][0])