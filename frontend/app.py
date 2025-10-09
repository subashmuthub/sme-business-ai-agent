import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from agent import SMEBusinessAgent

# Page configuration
st.set_page_config(
    page_title="SME Business AI Agent",
    page_icon="🤖",
    layout="wide"
)

# Clean and simple CSS styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2d5aa0);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2d5aa0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    .chat-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    with st.spinner("Initializing AI Agent..."):
        st.session_state.agent = SMEBusinessAgent()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Load business data
@st.cache_data
def load_business_data():
    try:
        df = pd.read_csv('../data/sme_data.csv')
    except FileNotFoundError:
        # Sample data if file not found
        df = pd.DataFrame({
            'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23'],
            'Sales (INR)': [500000, 480000, 520000, 600000, 550000, 450000],
            'Expenses (INR)': [300000, 320000, 310000, 340000, 330000, 360000],
            'Customers': [200, 190, 210, 250, 230, 180],
            'Inventory Cost (INR)': [120000, 130000, 125000, 140000, 135000, 145000],
            'Marketing Spend (INR)': [30000, 28000, 35000, 40000, 37000, 25000]
        })
    df['Profit'] = df['Sales (INR)'] - df['Expenses (INR)']
    return df

df = load_business_data()

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 SME Business AI Agent</h1>
    <p>Intelligent Business Analytics & Insights</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📊 Business Overview")
    
    # Key metrics
    total_sales = df['Sales (INR)'].sum()
    total_profit = df['Profit'].sum()
    avg_customers = df['Customers'].mean()
    
    st.metric("Total Sales", f"₹{total_sales:,.0f}")
    st.metric("Total Profit", f"₹{total_profit:,.0f}")
    st.metric("Avg Customers", f"{avg_customers:.0f}")
    
    st.markdown("---")
    
    # Quick actions
    st.subheader("🚀 Quick Analysis")
    
    if st.button("� Profit Summary", use_container_width=True):
        st.session_state.chat_history.append(("You", "Show me profit analysis"))
        response = st.session_state.agent.simple_query("Show me profit for all months")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()
    
    if st.button("📊 Q1 Performance", use_container_width=True):
        st.session_state.chat_history.append(("You", "Q1 2023 summary"))
        response = st.session_state.agent.simple_query("Summarize Q1 2023 performance")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()
    
    if st.button("💡 Recommendations", use_container_width=True):
        st.session_state.chat_history.append(("You", "Business suggestions"))
        response = st.session_state.agent.simple_query("Suggest business improvements")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # Chat interface
    st.subheader("💬 Chat with AI Assistant")
    
    # Chat history
    if st.session_state.chat_history:
        for speaker, message in st.session_state.chat_history[-6:]:
            if speaker == "You":
                st.chat_message("user").write(message)
            else:
                st.chat_message("assistant").write(message)
    else:
        st.info("👋 Ask me anything about your business data!")
    
    # Chat input
    user_input = st.chat_input("Ask about sales, profits, or recommendations...")
    
    if user_input:
        st.session_state.chat_history.append(("You", user_input))
        
        with st.spinner("Analyzing..."):
            response = st.session_state.agent.simple_query(user_input)
            st.session_state.chat_history.append(("AI", response))
        
        st.rerun()

with col2:
    # Charts
    st.subheader("� Data Visualizations")
    
    # Sales trend
    fig_sales = px.line(df, x='Month', y='Sales (INR)', 
                       title="Sales Trend",
                       color_discrete_sequence=['#2d5aa0'])
    fig_sales.update_layout(height=250, showlegend=False)
    st.plotly_chart(fig_sales, use_container_width=True)
    
    # Profit chart
    fig_profit = px.bar(df, x='Month', y='Profit', 
                       title="Monthly Profit",
                       color_discrete_sequence=['#28a745'])
    fig_profit.update_layout(height=250, showlegend=False)
    st.plotly_chart(fig_profit, use_container_width=True)

# Sample questions
st.markdown("---")
st.subheader("� Try These Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("What was the profit in May 2023?"):
        st.session_state.chat_history.append(("You", "What was the profit in May 2023?"))
        response = st.session_state.agent.simple_query("What was the profit in May 2023?")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()

with col2:
    if st.button("Which month had highest sales?"):
        st.session_state.chat_history.append(("You", "Which month had highest sales?"))
        response = st.session_state.agent.simple_query("Which month had highest sales?")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()

with col3:
    if st.button("Give me cost reduction tips"):
        st.session_state.chat_history.append(("You", "Cost reduction strategies"))
        response = st.session_state.agent.simple_query("Suggest cost reduction strategies")
        st.session_state.chat_history.append(("AI", response))
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6c757d;'>"
    "🤖 SME Business AI Agent | Powered by AI"
    "</div>", 
    unsafe_allow_html=True
)