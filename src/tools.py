import pandas as pd
from typing import Dict, List

class BusinessAnalysisTools:
    def __init__(self, data_path="data/sme_data.csv"):
        self.df = pd.read_csv(data_path)
        self.df['Profit'] = self.df['Sales (INR)'] - self.df['Expenses (INR)']
        self.df['Profit Margin %'] = (self.df['Profit'] / self.df['Sales (INR)']) * 100
    
    def get_monthly_profit(self, month: str) -> Dict:
        """Get profit for a specific month"""
        row = self.df[self.df['Month'].str.contains(month, case=False)]
        if not row.empty:
            row = row.iloc[0]
            return {
                "month": row['Month'],
                "sales": row['Sales (INR)'],
                "expenses": row['Expenses (INR)'],
                "profit": row['Profit'],
                "profit_margin": round(row['Profit Margin %'], 2)
            }
        return {"error": "Month not found"}
    
    def get_quarterly_summary(self, quarter: str) -> Dict:
        """Get quarterly business summary"""
        if quarter.upper() == "Q1":
            months = ["Jan-23", "Feb-23", "Mar-23"]
        elif quarter.upper() == "Q2":
            months = ["Apr-23", "May-23", "Jun-23"]
        elif quarter.upper() == "Q3":
            months = ["Jul-23", "Aug-23", "Sep-23"]
        elif quarter.upper() == "Q4":
            months = ["Oct-23", "Nov-23", "Dec-23"]
        else:
            return {"error": "Invalid quarter"}
        
        q_data = self.df[self.df['Month'].isin(months)]
        
        return {
            "quarter": quarter.upper(),
            "total_sales": q_data['Sales (INR)'].sum(),
            "total_expenses": q_data['Expenses (INR)'].sum(),
            "total_profit": q_data['Profit'].sum(),
            "avg_customers": round(q_data['Customers'].mean()),
            "avg_profit_margin": round(q_data['Profit Margin %'].mean(), 2)
        }
    
    def suggest_cost_optimization(self, month: str) -> List[str]:
        """Suggest cost optimization strategies"""
        row = self.df[self.df['Month'].str.contains(month, case=False)]
        if row.empty:
            return ["Month not found"]
        
        row = row.iloc[0]
        suggestions = []
        
        # Check inventory costs
        avg_inventory = self.df['Inventory Cost (INR)'].mean()
        if row['Inventory Cost (INR)'] > avg_inventory:
            suggestions.append(f"Reduce inventory costs from ₹{row['Inventory Cost (INR)']} (₹{row['Inventory Cost (INR)'] - avg_inventory:.0f} above average)")
        
        # Check marketing efficiency
        marketing_roi = row['Customers'] / (row['Marketing Spend (INR)'] / 1000)
        avg_roi = (self.df['Customers'] / (self.df['Marketing Spend (INR)'] / 1000)).mean()
        
        if marketing_roi < avg_roi:
            suggestions.append(f"Improve marketing efficiency - current ROI: {marketing_roi:.2f} customers per ₹1000 spent")
        
        # Check profit margin
        if row['Profit Margin %'] < 30:
            suggestions.append("Consider raising prices or reducing operational costs to improve profit margin")
        
        return suggestions if suggestions else ["Business performance is optimal for this month"]

# Test the tools
if __name__ == "__main__":
    tools = BusinessAnalysisTools()
    
    # Test monthly profit
    may_profit = tools.get_monthly_profit("May")
    print("May profit:", may_profit)
    
    # Test quarterly summary
    q1_summary = tools.get_quarterly_summary("Q1")
    print("Q1 summary:", q1_summary)
    
    # Test suggestions
    suggestions = tools.suggest_cost_optimization("Jun")
    print("June suggestions:", suggestions)