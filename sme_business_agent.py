"""
Simple Business AI Agent - Lightweight version without heavy ML dependencies
"""
import pandas as pd
import os
import json
from typing import Dict, Any, List

class SimpleBusinessAgent:
    def __init__(self):
        self.data_file = os.path.join("data", "sme_data.csv")
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load the business data"""
        try:
            if os.path.exists(self.data_file):
                self.df = pd.read_csv(self.data_file)
                print(f"✅ Loaded {len(self.df)} rows of business data")
            else:
                print(f"⚠️ Data file not found: {self.data_file}")
                self.create_sample_data()
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.create_sample_data()
    
    def create_sample_data(self):
        """Create comprehensive sample business data"""
        sample_data = {
            'Month': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', 'Sep-23', 'Oct-23', 'Nov-23', 'Dec-23'],
            'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4'],
            'Year': [2023] * 12,
            'Sales (INR)': [450000, 485000, 520000, 580000, 625000, 595000, 680000, 715000, 695000, 720000, 765000, 850000],
            'Expenses (INR)': [320000, 335000, 345000, 375000, 390000, 385000, 420000, 435000, 425000, 445000, 465000, 520000],
            'Profit (INR)': [130000, 150000, 175000, 205000, 235000, 210000, 260000, 280000, 270000, 275000, 300000, 330000],
            'Customers': [180, 195, 210, 235, 255, 248, 275, 290, 285, 295, 310, 335],
            'New Customers': [25, 20, 18, 28, 25, 22, 30, 28, 26, 32, 35, 45],
            'Inventory Cost (INR)': [85000, 88000, 92000, 95000, 98000, 96000, 102000, 105000, 103000, 108000, 112000, 125000],
            'Marketing Spend (INR)': [25000, 28000, 32000, 38000, 42000, 40000, 45000, 48000, 46000, 50000, 55000, 65000],
            'Employee Cost (INR)': [120000, 125000, 128000, 132000, 135000, 133000, 140000, 143000, 141000, 145000, 148000, 155000],
            'Operational Cost (INR)': [95000, 98000, 100000, 105000, 108000, 106000, 115000, 118000, 116000, 120000, 125000, 140000],
            'Revenue Growth (%)': [0.0, 7.8, 15.6, 28.9, 38.9, 32.2, 51.1, 58.9, 54.4, 60.0, 70.0, 88.9],
            'Customer Retention (%)': [85.5, 87.2, 88.1, 89.4, 90.2, 89.5, 91.3, 92.1, 91.8, 93.2, 94.1, 95.5]
        }
        self.df = pd.DataFrame(sample_data)
        
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        self.df.to_csv(self.data_file, index=False)
        print(f"✅ Created comprehensive sample data with {len(self.df)} rows")
    
    def get_monthly_summary(self, month: str = None) -> Dict[str, Any]:
        """Get summary for a specific month or all months"""
        if self.df is None:
            return {"error": "No data available"}
        
        if month:
            month_data = self.df[self.df['Month'].str.contains(month, case=False)]
            if month_data.empty:
                return {"error": f"No data found for month: {month}"}
            data = month_data.iloc[0].to_dict()
        else:
            # Overall summary
            data = {
                'Total_Sales': self.df['Sales (INR)'].sum(),
                'Total_Expenses': self.df['Expenses (INR)'].sum(),
                'Total_Profit': self.df['Sales (INR)'].sum() - self.df['Expenses (INR)'].sum(),
                'Avg_Customers': self.df['Customers'].mean(),
                'Best_Month': self.df.loc[self.df['Sales (INR)'].idxmax(), 'Month'],
                'Worst_Month': self.df.loc[self.df['Sales (INR)'].idxmin(), 'Month']
            }
        
        return data
    
    def get_business_insights(self) -> List[str]:
        """Generate comprehensive business insights"""
        if self.df is None:
            return ["No data available for analysis"]
        
        insights = []
        
        # Calculate profit if not already present
        if 'Profit (INR)' not in self.df.columns:
            self.df['Profit (INR)'] = self.df['Sales (INR)'] - self.df['Expenses (INR)']
        
        # Revenue growth analysis
        if 'Revenue Growth (%)' in self.df.columns:
            final_growth = self.df['Revenue Growth (%)'].iloc[-1]
            insights.append(f"📈 Excellent revenue growth of {final_growth:.1f}% over the year")
        
        # Profitability analysis
        avg_profit = self.df['Profit (INR)'].mean()
        profit_margin = (avg_profit / self.df['Sales (INR)'].mean()) * 100
        
        if avg_profit > 0:
            insights.append(f"✅ Strong profitability with {profit_margin:.1f}% average profit margin")
        else:
            insights.append(f"⚠️ Loss-making business - immediate action needed")
        
        # Customer retention analysis
        if 'Customer Retention (%)' in self.df.columns:
            avg_retention = self.df['Customer Retention (%)'].mean()
            final_retention = self.df['Customer Retention (%)'].iloc[-1]
            insights.append(f"� Excellent customer loyalty - {final_retention:.1f}% retention rate")
        
        # Quarterly performance
        if 'Quarter' in self.df.columns:
            quarterly_sales = self.df.groupby('Quarter')['Sales (INR)'].sum()
            best_quarter = quarterly_sales.idxmax()
            insights.append(f"🏆 {best_quarter} was the strongest quarter with ₹{quarterly_sales[best_quarter]:,} in sales")
        
        # Marketing efficiency
        if 'Marketing Spend (INR)' in self.df.columns and 'New Customers' in self.df.columns:
            total_marketing = self.df['Marketing Spend (INR)'].sum()
            total_new_customers = self.df['New Customers'].sum()
            cost_per_acquisition = total_marketing / total_new_customers if total_new_customers > 0 else 0
            insights.append(f"� Customer acquisition cost: ₹{cost_per_acquisition:,.0f} per new customer")
        
        # Seasonal patterns
        sales_growth = ((self.df['Sales (INR)'].iloc[-1] - self.df['Sales (INR)'].iloc[0]) / self.df['Sales (INR)'].iloc[0]) * 100
        if sales_growth > 50:
            insights.append("� Exceptional business growth - consider scaling operations")
        elif sales_growth > 20:
            insights.append("� Strong business growth trajectory")
        
        return insights
    
    def simple_query(self, query: str) -> str:
        """Handle simple queries about the business"""
        if self.df is None:
            return "❌ No data available. Please load business data first."
        
        query_lower = query.lower()
        
        # Profit queries
        if 'profit' in query_lower:
            if any(month in query_lower for month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
                month = next(m for m in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] if m in query_lower)
                month_data = self.get_monthly_summary(month)
                if 'error' not in month_data:
                    if 'Profit (INR)' in month_data:
                        return f"Profit for {month_data['Month']}: ₹{month_data['Profit (INR)']:,}"
                    else:
                        profit = month_data['Sales (INR)'] - month_data['Expenses (INR)']
                        return f"Profit for {month_data['Month']}: ₹{profit:,}"
            elif any(quarter in query_lower for quarter in ['q1', 'q2', 'q3', 'q4']):
                quarter = next(q.upper() for q in ['q1', 'q2', 'q3', 'q4'] if q in query_lower)
                if 'Quarter' in self.df.columns:
                    quarter_data = self.df[self.df['Quarter'] == quarter]
                    total_profit = quarter_data['Profit (INR)'].sum() if 'Profit (INR)' in self.df.columns else (quarter_data['Sales (INR)'].sum() - quarter_data['Expenses (INR)'].sum())
                    return f"Total profit for {quarter}: ₹{total_profit:,}"
            else:
                if 'Profit (INR)' in self.df.columns:
                    total_profit = self.df['Profit (INR)'].sum()
                else:
                    total_profit = self.df['Sales (INR)'].sum() - self.df['Expenses (INR)'].sum()
                return f"Total profit across all months: ₹{total_profit:,}"
        
        # Sales queries
        elif 'sales' in query_lower or 'revenue' in query_lower:
            if 'highest' in query_lower or 'best' in query_lower or 'maximum' in query_lower:
                summary = self.get_monthly_summary()
                best_month = summary['Best_Month']
                best_sales = self.df[self.df['Month'] == best_month]['Sales (INR)'].iloc[0]
                return f"Highest sales: ₹{best_sales:,} in {best_month}"
            elif 'total' in query_lower:
                summary = self.get_monthly_summary()
                return f"Total sales: ₹{summary['Total_Sales']:,}"
            else:
                return f"Average monthly sales: ₹{self.df['Sales (INR)'].mean():,.0f}"
        
        # Customer queries
        elif 'customer' in query_lower:
            avg_customers = self.df['Customers'].mean()
            return f"Average customers per month: {avg_customers:.0f}"
        
        # Expense queries
        elif 'expense' in query_lower or 'cost' in query_lower:
            if 'total' in query_lower:
                summary = self.get_monthly_summary()
                return f"Total expenses: ₹{summary['Total_Expenses']:,}"
            else:
                return f"Average monthly expenses: ₹{self.df['Expenses (INR)'].mean():,.0f}"
        
        # Quarter analysis
        elif any(quarter in query_lower for quarter in ['q1', 'q2', 'q3', 'q4', 'quarter']):
            if 'Quarter' in self.df.columns:
                if any(q in query_lower for q in ['q1', 'q2', 'q3', 'q4']):
                    quarter = next(q.upper() for q in ['q1', 'q2', 'q3', 'q4'] if q in query_lower)
                    quarter_data = self.df[self.df['Quarter'] == quarter]
                    total_sales = quarter_data['Sales (INR)'].sum()
                    total_profit = quarter_data['Profit (INR)'].sum() if 'Profit (INR)' in self.df.columns else (quarter_data['Sales (INR)'].sum() - quarter_data['Expenses (INR)'].sum())
                    avg_customers = quarter_data['Customers'].mean()
                    return f"{quarter} Performance:\n• Sales: ₹{total_sales:,}\n• Profit: ₹{total_profit:,}\n• Avg Customers: {avg_customers:.0f}"
                else:
                    quarterly_summary = self.df.groupby('Quarter').agg({
                        'Sales (INR)': 'sum',
                        'Profit (INR)': 'sum' if 'Profit (INR)' in self.df.columns else lambda x: x,
                        'Customers': 'mean'
                    }).round(0)
                    best_quarter = quarterly_summary['Sales (INR)'].idxmax()
                    return f"Quarterly Performance Summary:\n{quarterly_summary.to_string()}\n\nBest performing quarter: {best_quarter}"
        
        # Growth and trends
        elif any(word in query_lower for word in ['growth', 'trend', 'increase', 'improvement']):
            if 'Revenue Growth (%)' in self.df.columns:
                final_growth = self.df['Revenue Growth (%)'].iloc[-1]
                monthly_growth = self.df['Revenue Growth (%)'].diff().mean()
                return f"Business Growth Analysis:\n• Total growth: {final_growth:.1f}% over the year\n• Average monthly growth: {monthly_growth:.1f}%\n• Trend: Strong upward trajectory"
            else:
                sales_growth = ((self.df['Sales (INR)'].iloc[-1] - self.df['Sales (INR)'].iloc[0]) / self.df['Sales (INR)'].iloc[0]) * 100
                return f"Sales growth over period: {sales_growth:.1f}%"
        
        # Customer queries
        elif 'retention' in query_lower:
            if 'Customer Retention (%)' in self.df.columns:
                avg_retention = self.df['Customer Retention (%)'].mean()
                final_retention = self.df['Customer Retention (%)'].iloc[-1]
                improvement = final_retention - self.df['Customer Retention (%)'].iloc[0]
                return f"Customer Retention Analysis:\n• Current retention: {final_retention:.1f}%\n• Average retention: {avg_retention:.1f}%\n• Improvement: +{improvement:.1f}% over the year"
        
        # Marketing efficiency
        elif 'marketing' in query_lower or 'acquisition' in query_lower:
            if 'Marketing Spend (INR)' in self.df.columns and 'New Customers' in self.df.columns:
                total_marketing = self.df['Marketing Spend (INR)'].sum()
                total_new_customers = self.df['New Customers'].sum()
                cost_per_acquisition = total_marketing / total_new_customers if total_new_customers > 0 else 0
                return f"Marketing Performance:\n• Total marketing spend: ₹{total_marketing:,}\n• New customers acquired: {total_new_customers}\n• Cost per acquisition: ₹{cost_per_acquisition:,.0f}"
        
        # Insights and recommendations
        elif any(word in query_lower for word in ['suggest', 'recommend', 'advice', 'improve', 'insight']):
            insights = self.get_business_insights()
            return "\n".join([f"• {insight}" for insight in insights])
        
        # Summary queries
        elif any(word in query_lower for word in ['summary', 'overview', 'performance']):
            summary = self.get_monthly_summary()
            insights = self.get_business_insights()
            
            result = f"""
📊 Business Performance Summary:
• Total Sales: ₹{summary['Total_Sales']:,}
• Total Expenses: ₹{summary['Total_Expenses']:,}
• Net Profit: ₹{summary['Total_Profit']:,}
• Best Month: {summary['Best_Month']}
• Average Customers: {summary['Avg_Customers']:.0f}

🔍 Key Insights:
{chr(10).join([f"• {insight}" for insight in insights])}
            """.strip()
            return result
        
        else:
            return """
I can help you analyze your business data. Try asking:
• "What was the profit in May?"
• "Which month had highest sales?"
• "Give me business insights"
• "Show performance summary"
• "What are total expenses?"
• "How many customers on average?"
            """.strip()

if __name__ == "__main__":
    agent = SimpleBusinessAgent()
    print("\n🤖 Simple Business AI Agent Ready!")
    
    while True:
        try:
            query = input("\nAsk me about your business: ")
            if query.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            
            response = agent.simple_query(query)
            print(f"\n{response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")