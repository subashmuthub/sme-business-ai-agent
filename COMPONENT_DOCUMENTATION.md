# SME Business AI Agent - Complete Component Documentation

## 🏗️ Project Architecture Overview

This project implements an intelligent business analytics platform for Small to Medium Enterprises (SMEs). It provides multiple interfaces to interact with business data through AI-powered insights, analytics, and recommendations.

## 📁 Directory Structure

```
sme_ai_agent/
├── 🚀 Application Entry Points
│   ├── run.py                    # Main launcher with interface selection
│   ├── main.py                   # CLI interface for AI agent
│   ├── dashboard.py              # Streamlit web dashboard
│   └── web_interface.py          # Simple HTTP web interface
│
├── 🧠 Core AI Components  
│   └── src/
│       ├── agent.py              # Advanced LangChain-powered AI agent
│       ├── rag_pipeline.py       # Retrieval Augmented Generation pipeline
│       ├── tools.py              # Business analysis tools
│       └── __init__.py           # Python package initialization
│
├── 📊 Data & Business Logic
│   ├── sme_business_agent.py     # Core business agent (lightweight)
│   └── data/
│       ├── sme_data.csv          # Business data (12 months)
│       └── DATA_DICTIONARY.md    # Data structure documentation
│
├── 🎨 Frontend Components
│   └── frontend/
│       └── app.py                # Advanced Streamlit application
│
├── 📚 Documentation
│   ├── README.md                 # Project overview
│   ├── CONTRIBUTING.md           # Development guidelines
│   ├── PROJECT_STRUCTURE.md      # Architecture details
│   └── PROJECT_RESTRUCTURE_COMPLETE.md  # Migration notes
│
├── ⚙️ Configuration
│   ├── requirements.txt          # Python dependencies
│   ├── .gitignore               # Git ignore patterns
│   └── LICENSE                   # MIT license
│
└── 🔧 Git Repository
    └── .git/                     # Version control data
```

## 🚀 Application Entry Points

### 1. `run.py` - Main Application Launcher
**Purpose**: Central entry point with menu-driven interface selection
**Features**:
- Interactive menu for choosing interfaces
- System information display
- Dependency checking
- Streamlit dashboard launch
- Web interface startup
- CLI mode activation

**Key Functions**:
```python
def main()                    # Main launcher menu
def show_system_info()        # Display system & dependency status
```

**Usage**: `python run.py`

### 2. `main.py` - Command Line Interface
**Purpose**: Direct CLI access to the advanced AI agent
**Features**:
- Terminal-based chat interface
- Direct agent interaction
- LangChain-powered responses
- Tool integration access

**Key Functions**:
```python
def main()                    # CLI chat loop with AI agent
```

**Usage**: `python main.py`

### 3. `dashboard.py` - Streamlit Web Dashboard
**Purpose**: Interactive web-based business intelligence dashboard
**Features**:
- Multi-tab interface (Dashboard, AI Chat, Analytics)
- Real-time business metrics
- Interactive charts and visualizations
- Chat interface with session persistence
- Quick action buttons
- Professional UI styling

**Key Components**:
```python
def main()                    # Main Streamlit app
def show_dashboard(agent)     # Business metrics & KPIs
def show_chat_interface(agent) # AI chat with history
def show_analytics(agent)     # Charts & data visualization
```

**Usage**: `streamlit run dashboard.py`

### 4. `web_interface.py` - Simple HTTP Web Interface
**Purpose**: Lightweight web server with chat capabilities
**Features**:
- Single-page web application
- Real-time chat interface
- Quick question buttons
- Modern responsive design
- Auto-opening browser
- Simple HTTP server

**Key Components**:
```python
class SMEHandler              # HTTP request handler
def run_simple_server()       # Start web server
```

**Usage**: `python web_interface.py`

## 🧠 Core AI Components

### 1. `src/agent.py` - Advanced AI Agent
**Purpose**: LangChain-powered intelligent business agent
**Features**:
- LangChain Agent framework
- Tool integration (search, analysis, optimization)
- Ollama LLM integration (Llama3:8b)
- RAG pipeline integration
- Fallback to simple queries

**Key Components**:
```python
class SMEBusinessAgent:
    def __init__()            # Initialize LLM, RAG, tools
    def _create_tools()       # Define LangChain tools
    def simple_query()        # Fallback query handler
```

**Tools Available**:
- `search_business_data`: RAG-powered data search
- `get_monthly_profit`: Monthly profit analysis
- `get_quarterly_summary`: Quarter performance reports
- `get_cost_optimization`: Business improvement suggestions

### 2. `src/rag_pipeline.py` - RAG Pipeline
**Purpose**: Retrieval Augmented Generation for business data
**Features**:
- ChromaDB vector database
- Sentence transformer embeddings
- Business data chunking
- Semantic search capabilities
- CSV data processing

**Key Components**:
```python
class SMERAGPipeline:
    def __init__()                  # Initialize ChromaDB & embeddings
    def load_and_process_data()     # Process CSV into text chunks
    def create_vector_store()       # Create embeddings & store
    def query()                     # Semantic search queries
```

**Technical Stack**:
- **Vector DB**: ChromaDB
- **Embeddings**: SentenceTransformer (all-MiniLM-L6-v2)
- **Data Format**: Structured text chunks from CSV

### 3. `src/tools.py` - Business Analysis Tools
**Purpose**: Specialized business analytics functions
**Features**:
- Monthly profit analysis
- Quarterly summaries
- Cost optimization suggestions
- Performance metrics calculation
- Data validation & fallbacks

**Key Components**:
```python
class BusinessAnalysisTools:
    def __init__()                    # Load & process business data
    def get_monthly_profit()          # Monthly financial analysis
    def get_quarterly_summary()       # Quarter aggregations
    def suggest_cost_optimization()   # Business recommendations
```

**Analytics Capabilities**:
- Profit margin calculations
- ROI analysis
- Cost efficiency assessment
- Performance benchmarking

## 📊 Data & Business Logic

### 1. `sme_business_agent.py` - Core Business Agent
**Purpose**: Lightweight business intelligence agent (no heavy ML dependencies)
**Features**:
- CSV data loading with fallbacks
- Natural language query processing
- Business insights generation
- Performance analysis
- Sample data creation

**Key Components**:
```python
class SimpleBusinessAgent:
    def __init__()                # Load business data
    def load_data()               # CSV loading with fallbacks
    def create_sample_data()      # Generate realistic sample data
    def get_monthly_summary()     # Financial summaries
    def get_business_insights()   # AI-generated insights
    def simple_query()            # Natural language processing
```

**Query Capabilities**:
- Profit analysis by month/quarter
- Sales trend analysis
- Customer metrics
- Growth rate calculations
- Cost optimization suggestions
- Business performance summaries

### 2. `data/sme_data.csv` - Business Dataset
**Purpose**: 12-month SME business data for analysis
**Structure**:
- **Time**: Month, Quarter, Year
- **Financial**: Sales, Expenses, Profit, Costs
- **Customer**: Count, New acquisitions, Retention
- **Performance**: Growth rates, Margins

**Data Quality**:
- Realistic SME business patterns
- Consistent growth trajectory
- Seasonal variations
- Complete 12-month dataset
- No missing values

### 3. `data/DATA_DICTIONARY.md` - Data Documentation
**Purpose**: Comprehensive data structure documentation
**Contents**:
- Column definitions
- Business context
- Usage guidelines
- Sample queries
- Data quality notes

## 🎨 Frontend Components

### 1. `frontend/app.py` - Advanced Streamlit App
**Purpose**: Enhanced version of the dashboard with additional features
**Features**:
- Advanced analytics
- Extended visualizations
- Custom styling
- Enhanced user experience

## 📚 Documentation Files

### 1. `README.md` - Project Overview
**Contents**:
- Project description
- Installation instructions
- Usage examples
- Feature overview
- Getting started guide

### 2. `CONTRIBUTING.md` - Development Guidelines
**Contents**:
- Code style guidelines
- Development setup
- Testing procedures
- Pull request process
- Issue templates

### 3. `PROJECT_STRUCTURE.md` - Architecture Details
**Contents**:
- Detailed file explanations
- Component relationships
- Data flow diagrams
- Technical specifications

## ⚙️ Configuration Files

### 1. `requirements.txt` - Python Dependencies
**Categories**:
- **Core**: pandas, numpy (data processing)
- **Web**: streamlit, plotly (visualization)
- **AI**: langchain, chromadb, sentence-transformers (optional ML)
- **Utils**: requests, python-dateutil (utilities)
- **Dev**: pytest, black, flake8 (development tools)

### 2. `.gitignore` - Git Ignore Patterns
**Excludes**:
- Python cache files (`__pycache__/`)
- Virtual environment folders
- IDE configuration files
- OS-specific files
- Database files
- Temporary files

### 3. `LICENSE` - MIT License
**Purpose**: Open source license for distribution and usage rights

## 🔄 Data Flow Architecture

```
CSV Data (sme_data.csv)
    ↓
SimpleBusinessAgent (lightweight processing)
    ↓
Multiple Interface Options:
    ├── CLI (main.py)
    ├── Streamlit Dashboard (dashboard.py)
    ├── Web Interface (web_interface.py)
    └── Advanced Agent (src/agent.py)
         ↓
    LangChain Tools:
    ├── RAG Pipeline (src/rag_pipeline.py)
    ├── Business Tools (src/tools.py)
    └── Vector Search (ChromaDB)
```

## 🛠️ Technology Stack

### **Core Technologies**
- **Python 3.13**: Main programming language
- **Pandas**: Data processing and analysis
- **Streamlit**: Web dashboard framework
- **Plotly**: Interactive visualizations

### **AI & ML Components**
- **LangChain**: AI agent framework
- **ChromaDB**: Vector database
- **SentenceTransformers**: Text embeddings
- **Ollama**: Local LLM (Llama3:8b)

### **Web Technologies**
- **HTTP Server**: Built-in Python server
- **HTML/CSS/JavaScript**: Web interface
- **AJAX**: Real-time chat communication

### **Development Tools**
- **Git**: Version control
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting

## 🎯 Component Relationships

### **Dependency Hierarchy**
1. **Data Layer**: `sme_data.csv` → `SimpleBusinessAgent`
2. **Business Logic**: `SimpleBusinessAgent` → All interfaces
3. **AI Layer**: `agent.py` → `rag_pipeline.py` + `tools.py`
4. **Interface Layer**: Multiple entry points use business logic
5. **Configuration**: `requirements.txt` defines all dependencies

### **Interface Integration**
- All interfaces use `SimpleBusinessAgent` as the core engine
- Advanced features use `src/agent.py` for LangChain capabilities
- Data flows from CSV through business logic to user interfaces
- Consistent API across all interaction methods

## 🚀 Usage Patterns

### **For Business Users**
1. Start with `python run.py` for guided interface selection
2. Use Streamlit dashboard for visual analytics
3. Use web interface for quick queries
4. Use CLI for power users

### **For Developers**
1. Core business logic in `sme_business_agent.py`
2. Advanced AI features in `src/` directory
3. Interface customization in respective entry point files
4. Data structure documented in `DATA_DICTIONARY.md`

### **For Data Scientists**
1. RAG pipeline for semantic search
2. Business tools for analytics
3. Vector database for embeddings
4. Structured data for analysis

This architecture provides a scalable, modular approach to business intelligence with multiple access patterns and progressive enhancement capabilities.