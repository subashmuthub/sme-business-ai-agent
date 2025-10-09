"""
Simple Streamlit Business Dashboard - Lightweight version
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sme_business_agent import SimpleBusinessAgent
import os

# Page configuration
st.set_page_config(
    page_title="SME Business AI Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2E86C1, #3498DB);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #3498DB;
        margin: 0.5rem 0;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
    }
    .bot-message {
        background-color: #F1F8E9;
        border-left: 4px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize the simple agent
@st.cache_resource
def load_agent():
    return SimpleBusinessAgent()

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 SME Business AI Agent</h1>
        <p>Simple Business Intelligence Dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load agent
    try:
        agent = load_agent()
        
        if agent.df is not None:
            # Create tabs
            tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "💬 AI Chat", "📈 Analytics"])
            
            with tab1:
                show_dashboard(agent)
            
            with tab2:
                show_chat_interface(agent)
            
            with tab3:
                show_analytics(agent)
        else:
            st.error("❌ No business data available. Please check data folder.")
            
    except Exception as e:
        st.error(f"❌ Error loading agent: {str(e)}")

def show_dashboard(agent):
    """Display main dashboard metrics"""
    st.subheader("📊 Business Overview")
    
    # Get summary data
    summary = agent.get_monthly_summary()
    
    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Total Sales",
            value=f"₹{summary.get('Total_Sales', 0):,}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="💸 Total Expenses",
            value=f"₹{summary.get('Total_Expenses', 0):,}",
            delta=None
        )
    
    with col3:
        profit = summary.get('Total_Profit', 0)
        st.metric(
            label="💼 Net Profit",
            value=f"₹{profit:,}",
            delta="Profit" if profit > 0 else "Loss"
        )
    
    with col4:
        st.metric(
            label="👥 Avg Customers",
            value=f"{summary.get('Avg_Customers', 0):.0f}",
            delta=None
        )
    
    # Business insights
    st.subheader("🔍 Key Insights")
    insights = agent.get_business_insights()
    for insight in insights:
        st.info(insight)

def show_analytics(agent):
    """Show detailed analytics and charts"""
    st.subheader("📈 Business Analytics")
    
    df = agent.df.copy()
    df['Profit'] = df['Sales (INR)'] - df['Expenses (INR)']
    
    # Sales trend chart
    st.subheader("Sales Trend")
    fig_sales = px.line(
        df, 
        x='Month', 
        y='Sales (INR)',
        title='Monthly Sales Trend',
        markers=True
    )
    fig_sales.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales (INR)",
        showlegend=False
    )
    st.plotly_chart(fig_sales, use_container_width=True)
    
    # Profit analysis
    st.subheader("Profit Analysis")
    fig_profit = px.bar(
        df,
        x='Month',
        y='Profit',
        title='Monthly Profit/Loss',
        color='Profit',
        color_continuous_scale=['red', 'green']
    )
    st.plotly_chart(fig_profit, use_container_width=True)
    
    # Customer growth
    st.subheader("Customer Growth")
    fig_customers = px.area(
        df,
        x='Month',
        y='Customers',
        title='Customer Count Over Time'
    )
    st.plotly_chart(fig_customers, use_container_width=True)
    
    # Data table
    st.subheader("📋 Raw Data")
    st.dataframe(df, use_container_width=True)

def show_chat_interface(agent):
    """Simple chat interface"""
    st.subheader("💬 Ask AI About Your Business")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>AI:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    query = st.chat_input("Ask about your business...")
    
    if query:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Get AI response
        try:
            response = agent.simple_query(query)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"})
        
        # Rerun to show new messages
        st.rerun()
    
    # Quick action buttons
    st.subheader("🚀 Quick Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💰 Show Profit Summary"):
            response = agent.simple_query("show profit summary")
            st.info(response)
    
    with col2:
        if st.button("📈 Best Performance Month"):
            response = agent.simple_query("which month had highest sales")
            st.info(response)
    
    with col3:
        if st.button("🔍 Business Insights"):
            response = agent.simple_query("give me business insights")
            st.info(response)

if __name__ == "__main__":
    main()