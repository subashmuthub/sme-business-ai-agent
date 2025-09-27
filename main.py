import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from agent import SMEBusinessAgent

def main():
    print("🏢 SME/MSME Business Insights AI Agent")
    print("="*50)
    print("Ask me about your business data!")
    print("Examples:")
    print("- What was the profit in May 2023?")
    print("- Summarize Q1 2023 performance")
    print("- Suggest improvements for June")
    print("- What were the highest sales?")
    print("\nType 'quit' to exit")
    print("="*50)
    
    # Initialize agent
    agent = SMEBusinessAgent()
    
    while True:
        user_input = input("\n💼 Your question: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Thank you for using SME Business AI Agent!")
            break
        
        if not user_input:
            continue
        
        try:
            response = agent.simple_query(user_input)
            print(f"\n🤖 AI Agent: {response}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()