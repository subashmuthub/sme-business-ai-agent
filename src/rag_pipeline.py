import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import json

class SMERAGPipeline:
    def __init__(self, data_path="data/sme_data.csv"):
        self.data_path = data_path
        self.client = chromadb.Client()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.collection = None
        
    def load_and_process_data(self):
        """Load CSV data and create text chunks for embedding"""
        df = pd.read_csv(self.data_path)
        
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