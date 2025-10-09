# SME Business AI Agent

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Intelligent Business Analytics Platform for Small and Medium Enterprises**

Transform your business data into actionable insights with AI-powered analytics, interactive dashboards, and natural language queries.

## 🚀 Features

### 📊 **Business Intelligence**
- **Financial Analytics**: Revenue, profit, cost analysis
- **Customer Intelligence**: Growth, retention, acquisition metrics  
- **Performance Tracking**: Quarterly reports, trend analysis
- **Growth Insights**: Revenue growth, market expansion tracking

### 🤖 **AI-Powered Analysis**
- **Natural Language Queries**: "What was profit in Q3?"
- **Smart Recommendations**: AI-generated business insights
- **Trend Detection**: Automatic pattern recognition
- **Executive Summaries**: One-click business reports

### 🎨 **Multiple Interfaces**
- **Interactive Dashboard**: Streamlit-based web application
- **Simple Web Interface**: Lightweight HTML chat interface
- **Command Line**: Developer-friendly CLI access

## 📸 Screenshots

### Dashboard Overview
*Interactive business metrics with real-time charts and KPI tracking*

### AI Chat Interface  
*Natural language business queries with instant insights*

## 🛠️ Technology Stack

- **Backend**: Python 3.11+, Pandas, NumPy
- **Frontend**: Streamlit, Plotly, HTML/CSS/JavaScript
- **AI/ML**: LangChain, ChromaDB, Sentence Transformers
- **Data**: CSV-based storage with structured business metrics

## 📋 Quick Start

### Prerequisites
- Python 3.11 or higher
- 4GB RAM minimum (8GB recommended)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sme-business-ai-agent.git
   cd sme-business-ai-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   ```bash
   # Option 1: Streamlit Dashboard (Recommended)
   streamlit run dashboard.py
   
   # Option 2: Simple Web Interface
   python web_interface.py
   
   # Option 3: Command Line
   python sme_business_agent.py
   ```

5. **Access the application**
   - **Dashboard**: http://localhost:8501
   - **Web Interface**: http://localhost:8000

## 📊 Data Format

Place your business data in `data/sme_data.csv` with the following structure:

```csv
Month,Quarter,Year,Sales (INR),Expenses (INR),Profit (INR),Customers,New Customers,Inventory Cost (INR),Marketing Spend (INR),Employee Cost (INR),Operational Cost (INR),Revenue Growth (%),Customer Retention (%)
Jan-23,Q1,2023,450000,320000,130000,180,25,85000,25000,120000,95000,0.0,85.5
Feb-23,Q1,2023,485000,335000,150000,195,20,88000,28000,125000,98000,7.8,87.2
```

### Supported Business Metrics
- **Financial**: Sales, expenses, profit, various cost categories
- **Customer**: Total customers, new acquisitions, retention rates
- **Performance**: Growth rates, margins, operational efficiency

## 💬 Usage Examples

### Natural Language Queries
```
"What was the profit in May 2023?"
"Which quarter had the highest sales?"
"Show me customer retention trends"
"Compare Q1 vs Q4 performance"
"Give me business insights and recommendations"
```

### Dashboard Features
- **Interactive Charts**: Sales trends, profit analysis, customer growth
- **KPI Metrics**: Revenue, profit margin, customer retention
- **Quarterly Reports**: Performance comparisons and insights
- **AI Chat**: Real-time business question answering

## 🏗️ Project Structure

```
sme-business-ai-agent/
├── sme_business_agent.py    # Core AI business agent
├── dashboard.py             # Streamlit web dashboard  
├── web_interface.py         # Simple web interface
├── main.py                  # Command line interface
├── src/                     # Advanced AI components
│   ├── agent.py             # LangChain agent
│   ├── rag_pipeline.py      # RAG system
│   └── tools.py             # Business analysis tools
├── frontend/                # Web UI components
│   └── app.py               # Advanced Streamlit app
├── data/                    # Business data
│   ├── sme_data.csv         # Main business dataset
│   └── DATA_DICTIONARY.md   # Data format documentation
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🎯 Use Cases

### For Business Owners
- **Performance Monitoring**: Track revenue, profit, and growth
- **Customer Analytics**: Monitor acquisition and retention
- **Financial Planning**: Analyze costs and optimize spending
- **Strategic Decisions**: Data-driven business insights

### For Accountants & Analysts
- **Automated Reporting**: Generate quarterly and annual reports
- **Trend Analysis**: Identify patterns and opportunities
- **Cost Analysis**: Break down expenses and optimize operations
- **KPI Tracking**: Monitor key performance indicators

### For Consultants
- **Client Insights**: Provide data-driven recommendations
- **Benchmarking**: Compare performance across periods
- **Growth Planning**: Identify expansion opportunities
- **Risk Assessment**: Analyze business health metrics

## 🔧 Configuration

### Environment Variables
Create a `.env` file for optional configurations:
```env
# AI Settings (Optional)
OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_API_KEY=your_langchain_key_here

# Database Settings (Optional)
DATABASE_URL=sqlite:///business_data.db
```

### Customization
- **Business Metrics**: Modify `data/sme_data.csv` structure
- **AI Responses**: Customize prompts in `src/agent.py`
- **Dashboard Layout**: Edit `dashboard.py` for custom views
- **Styling**: Update CSS in web interface files

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **Streamlit** for the excellent web app framework
- **LangChain** for AI agent capabilities
- **Plotly** for interactive visualizations
- **Pandas** for powerful data analysis

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/sme-business-ai-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/sme-business-ai-agent/discussions)
- **Email**: your.email@example.com

---

**Made with ❤️ for Small and Medium Enterprises worldwide**