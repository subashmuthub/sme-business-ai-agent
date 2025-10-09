#!/usr/bin/env python3
"""
SME Business AI Agent - Main Application Launcher
"""

import sys
import os
import subprocess
from pathlib import Path

def main():
    """Main launcher with interface selection."""
    print("🤖 SME Business AI Agent - Application Launcher")
    print("=" * 50)
    print()
    print("Available interfaces:")
    print("1. 📊 Interactive Dashboard (Streamlit) - Recommended")
    print("2. 🌐 Simple Web Interface")
    print("3. 💻 Command Line Interface")
    print("4. ℹ️  Show system information")
    print("5. ❌ Exit")
    print()
    
    while True:
        try:
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                print("\n🚀 Starting Interactive Dashboard...")
                subprocess.run([sys.executable, "-m", "streamlit", "run", "dashboard.py"])
                break
                
            elif choice == "2":
                print("\n🚀 Starting Simple Web Interface...")
                subprocess.run([sys.executable, "web_interface.py"])
                break
                
            elif choice == "3":
                print("\n🚀 Starting Command Line Interface...")
                subprocess.run([sys.executable, "sme_business_agent.py"])
                break
                
            elif choice == "4":
                show_system_info()
                
            elif choice == "5":
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please select 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def show_system_info():
    """Display system and project information."""
    print("\n" + "=" * 50)
    print("📋 System Information")
    print("=" * 50)
    
    # Python version
    print(f"🐍 Python: {sys.version.split()[0]}")
    
    # Check dependencies
    dependencies = [
        ("pandas", "Data processing"),
        ("streamlit", "Web dashboard"),
        ("plotly", "Charts and visualizations"),
        ("langchain", "AI agent framework (optional)"),
    ]
    
    print("\n📦 Dependencies:")
    for package, description in dependencies:
        try:
            __import__(package)
            print(f"  ✅ {package} - {description}")
        except ImportError:
            print(f"  ❌ {package} - {description} (not installed)")
    
    # Project structure
    print(f"\n📁 Project directory: {Path.cwd()}")
    
    # Data file
    data_file = Path("data/sme_data.csv")
    if data_file.exists():
        print(f"✅ Business data: {data_file} (found)")
    else:
        print(f"❌ Business data: {data_file} (not found)")
    
    print("\n" + "=" * 50)
    print()

if __name__ == "__main__":
    main()