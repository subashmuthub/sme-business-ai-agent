from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from rag_pipeline import SMERAGPipeline  # Keep simple imports
from tools import BusinessAnalysisTools
import json

class SMEBusinessAgent:
    def __init__(self):
        # Initialize components
        self.rag_pipeline = SMERAGPipeline()
        self.business_tools = BusinessAnalysisTools()
        
        # Initialize LLM (using a simple approach first)
        try:
            self.llm = ChatOllama(model="llama3:8b", temperature=0.1)
        except:
            # Fallback to a mock LLM for testing
            self.llm = None
            print("⚠️ Ollama not available, using mock responses")
        
        # Create vector store if not exists
        try:
            self.rag_pipeline.collection = self.rag_pipeline.client.get_collection("sme_business_data")
        except:
            self.rag_pipeline.create_vector_store()
        
        self.tools = self._create_tools()
    
    def _create_tools(self):
        """Create LangChain tools from our business functions"""
        
        def search_business_data(query: str) -> str:
            """Search business data using RAG"""
            results = self.rag_pipeline.query(query, n_results=2)
            return f"Relevant data: {results['documents'][0][:2]}"
        
        def get_monthly_profit_tool(month: str) -> str:
            """Get profit information for a specific month"""
            result = self.business_tools.get_monthly_profit(month)
            return json.dumps(result, indent=2)
        
        def get_quarterly_summary_tool(quarter: str) -> str:
            """Get quarterly business summary (Q1, Q2, Q3, Q4)"""
            result = self.business_tools.get_quarterly_summary(quarter)
            return json.dumps(result, indent=2)
        
        def get_cost_optimization_tool(month: str) -> str:
            """Get cost optimization suggestions for a month"""
            suggestions = self.business_tools.suggest_cost_optimization(month)
            return "Suggestions:\n" + "\n".join([f"• {s}" for s in suggestions])
        
        return [
            Tool(
                name="search_business_data",
                description="Search through business data to find relevant information about sales, expenses, profits, customers, etc.",
                func=search_business_data
            ),
            Tool(
                name="get_monthly_profit",
                description="Get detailed profit information for a specific month (e.g., 'May', 'Jun')",
                func=get_monthly_profit_tool
            ),
            Tool(
                name="get_quarterly_summary", 
                description="Get business summary for a quarter (Q1, Q2, Q3, Q4)",
                func=get_quarterly_summary_tool
            ),
            Tool(
                name="get_cost_optimization",
                description="Get cost optimization and business improvement suggestions for a specific month",
                func=get_cost_optimization_tool
            )
        ]
    
    def simple_query(self, user_question: str) -> str:
        """Handle queries without LangChain agent (for testing)"""
        question_lower = user_question.lower()
        
        # Profit queries
        if "profit" in question_lower:
            months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
            for month in months:
                if month in question_lower:
                    result = self.business_tools.get_monthly_profit(month)
                    if "error" not in result:
                        return f"In {result['month']}: Sales ₹{result['sales']}, Expenses ₹{result['expenses']}, Profit ₹{result['profit']} (Margin: {result['profit_margin']}%)"
        
        # Quarterly queries
        if any(q in question_lower for q in ["q1", "quarter 1", "first quarter"]):
            result = self.business_tools.get_quarterly_summary("Q1")
            return f"Q1 2023 Summary: Total Sales ₹{result['total_sales']}, Total Profit ₹{result['total_profit']}, Avg Profit Margin {result['avg_profit_margin']}%"
        
        # Suggestions
        if "suggest" in question_lower or "improve" in question_lower:
            months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
            for month in months:
                if month in question_lower:
                    suggestions = self.business_tools.suggest_cost_optimization(month)
                    return "Business Improvement Suggestions:\n" + "\n".join([f"• {s}" for s in suggestions])
        
        # RAG search for general queries
        results = self.rag_pipeline.query(user_question, n_results=1)
        if results['documents']:
            return f"Based on your data:\n{results['documents'][0][0]}"
        
        return "I can help you with profit analysis, quarterly summaries, and business suggestions. Try asking about specific months or quarters!"

# Test the agent
if __name__ == "__main__":
    agent = SMEBusinessAgent()
    
    # Test queries
    test_queries = [
        "What was the profit in May 2023?",
        "Summarize Q1 2023 performance",
        "Suggest improvements for June 2023",
        "What were the sales in August?"
    ]
    
    print("🤖 SME Business AI Agent Testing\n" + "="*50)
    
    for query in test_queries:
        print(f"\n❓ Query: {query}")
        response = agent.simple_query(query)
        print(f"🤖 Response: {response}")
        print("-" * 50)