# SME Business AI Agent - Complete Project Structure

## 📁 **Repository**: https://github.com/subashmuthub/sme-business-ai-agent

```
sme-business-ai-agent/
│
├── 📄 .gitignore                      # Git ignore rules (Python, IDE, OS files)
├── 🤝 CONTRIBUTING.md                 # Developer contribution guidelines
├── 📊 dashboard.py                    # Streamlit web dashboard (main interface)
├── 📄 LICENSE                         # MIT License
├── 💻 main.py                         # Command line interface
├── 📖 README.md                       # Project documentation & setup guide
├── 📦 requirements.txt                # Python dependencies (essential packages)
├── 🚀 run.py                          # Application launcher with interface menu
├── 🤖 sme_business_agent.py           # Core AI business agent (lightweight)
├── 🌐 web_interface.py                # Simple web interface (HTTP server)
│
├── 📊 data/                           # Business data directory
│   ├── 📋 DATA_DICTIONARY.md          # Data structure documentation
│   └── 📈 sme_data.csv                # Sample business dataset (12 months)
│
├── 🌐 frontend/                       # Web UI components
│   └── 📱 app.py                      # Advanced Streamlit application
│
└── 🧠 src/                            # Advanced AI components
    ├── 🤖 agent.py                    # LangChain-based AI agent
    ├── 🔍 rag_pipeline.py             # RAG (Retrieval Augmented Generation)
    ├── 🛠️ tools.py                    # Business analysis tools
    └── 📦 __init__.py                 # Package initializer
```

## 🎯 **File Purposes & Descriptions**

### **🚀 Core Application Files**

#### **`run.py`** - Application Launcher
- **Purpose**: Main entry point with interactive menu
- **Features**: Interface selection, system info, easy startup
- **Usage**: `python run.py`

#### **`sme_business_agent.py`** - Lightweight Business Agent
- **Purpose**: Core business intelligence engine (no heavy AI dependencies)
- **Features**: Financial analysis, customer metrics, business insights
- **Usage**: Direct import or standalone CLI

#### **`dashboard.py`** - Streamlit Web Dashboard
- **Purpose**: Interactive web-based business dashboard
- **Features**: Charts, KPIs, AI chat, multi-tab interface
- **Access**: http://localhost:8501

#### **`web_interface.py`** - Simple Web Interface
- **Purpose**: Lightweight HTML/CSS web interface
- **Features**: Basic chat, clean design, fast loading
- **Access**: http://localhost:8000

#### **`main.py`** - Command Line Interface
- **Purpose**: Terminal-based interaction
- **Features**: Direct CLI access, scripting support

### **📊 Data & Documentation**

#### **`data/sme_data.csv`** - Business Dataset
- **Content**: 12 months of SME business metrics
- **Columns**: Sales, expenses, profit, customers, costs, growth rates
- **Scale**: ₹76.8L annual revenue, 335 customers

#### **`data/DATA_DICTIONARY.md`** - Data Documentation
- **Purpose**: Explains data structure and business metrics
- **Content**: Column definitions, business context, usage examples

#### **`README.md`** - Project Documentation
- **Content**: Setup guide, features, usage examples, screenshots
- **Audience**: End users, developers, contributors

#### **`CONTRIBUTING.md`** - Developer Guide
- **Content**: Contribution guidelines, coding standards, setup process
- **Audience**: Open source contributors, developers

### **🌐 Frontend Components**

#### **`frontend/app.py`** - Advanced Streamlit App
- **Purpose**: Enhanced web interface with advanced features
- **Features**: Complex visualizations, advanced AI integration
- **Status**: Alternative to main dashboard.py

### **🧠 Advanced AI Components (src/)**

#### **`src/agent.py`** - LangChain Agent
- **Purpose**: Advanced AI agent with LangChain framework
- **Features**: Natural language processing, complex reasoning
- **Dependencies**: LangChain, Ollama (optional)

#### **`src/rag_pipeline.py`** - RAG System
- **Purpose**: Retrieval Augmented Generation for document search
- **Features**: Vector database, semantic search, context retrieval
- **Dependencies**: ChromaDB, sentence transformers

#### **`src/tools.py`** - Business Analysis Tools
- **Purpose**: Specialized business analysis functions
- **Features**: Advanced calculations, report generation
- **Integration**: Used by AI agents for business insights

### **⚙️ Configuration Files**

#### **`.gitignore`** - Git Ignore Rules
- **Content**: Python cache, virtual environments, IDE files
- **Purpose**: Keep repository clean, exclude development artifacts

#### **`requirements.txt`** - Dependencies
- **Content**: Essential Python packages with version ranges
- **Categories**: Core (pandas, streamlit), AI (langchain), Web (aiohttp)

#### **`LICENSE`** - MIT License
- **Purpose**: Open source license for project usage and distribution

---

## 🎯 **Usage Patterns**

### **For Business Users**
```bash
# Easy start with menu
python run.py

# Direct dashboard access
streamlit run dashboard.py
```

### **For Developers**
```bash
# Development setup
git clone https://github.com/subashmuthub/sme-business-ai-agent.git
cd sme-business-ai-agent
pip install -r requirements.txt

# Core business logic
from sme_business_agent import SimpleBusinessAgent
agent = SimpleBusinessAgent()
```

### **For Data Analysis**
```bash
# Access business data
import pandas as pd
df = pd.read_csv('data/sme_data.csv')

# Use AI for insights
python sme_business_agent.py
```

---

## 📈 **Key Features by File**

| File | Primary Feature | Secondary Features |
|------|----------------|-------------------|
| `run.py` | Application launcher | Interface selection, system info |
| `dashboard.py` | Interactive web dashboard | Charts, KPIs, AI chat |
| `sme_business_agent.py` | Business intelligence | Financial analysis, insights |
| `web_interface.py` | Simple web chat | Clean UI, fast loading |
| `data/sme_data.csv` | Business dataset | 12 months, comprehensive metrics |
| `src/agent.py` | Advanced AI | LangChain, complex reasoning |

---

## 🔧 **Technical Architecture**

### **Lightweight Stack** (Core functionality)
```
User Interface (dashboard.py, web_interface.py)
         ↓
Business Logic (sme_business_agent.py)
         ↓
Data Layer (pandas + CSV)
```

### **AI-Enhanced Stack** (Advanced features)
```
User Interface
         ↓
AI Agent (src/agent.py + LangChain)
         ↓
RAG Pipeline (src/rag_pipeline.py + ChromaDB)
         ↓
Business Tools (src/tools.py) + Data
```

This structure provides both **simplicity for basic use** and **advanced capabilities for power users**, making it perfect for SME businesses of all technical levels! 🚀