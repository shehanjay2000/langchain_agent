import pandas as pd 
import datetime
import sqlite3
from langchain.tools import tool

@tool
def income_tool(query:str) -> str:
    """Check income totals, salary, sources and earnings
    Args:
        query : question about income
            examples : 
            "monthly income"
            "yearly income"
            "income sources"
            "freelance income"
    Returns:
        income summary, totals, or breakdown
    """
    try:
        with sqlite3.connect("finance.db") as conn:
            income = pd.read_sql_query("SELECT * FROM income", conn)
        
        today = datetime.datetime.now()
        q = query.lower()
        income['Amount'] = pd.to_numeric(income['Amount'], errors='coerce')
        income["Start Date"] = pd.to_datetime(income["Start Date"], errors='coerce')
        income["End Date"] = pd.to_datetime(income["End Date"], errors='coerce')
        active_income = income[(income['Start Date'] <= today) & (income['End Date'] >= today)]

        # list income sources 
        if "source" in q:
            sources = active_income['Source'].tolist()
            return f"Active income sources: {', '.join(sources)}"
        
        # monthly income
        elif "month" in q:
            total = 0
            for _,row in active_income.iterrows():
                if row['Frequency'] == "Monthly":
                    total = total + row['Amount'] 
                elif row['Frequency'] == "Weekly":
                    total = total + row['Amount'] * 4
                elif row['Frequency'] == "Quarterly":
                    total = total + row['Amount'] / 3
            return f"Estimated monthly income: ${total: .2f}"
        
        # yearly income
        elif "year" in q:
            total = 0
            for _,row in active_income.iterrows():
                if row['Frequency'] == "Monthly":
                    total = total + row['Amount'] * 12
                elif row['Frequency'] == "Weekly":
                    total = total + row['Amount'] * 52
                elif row['Frequency'] == "Quarterly":
                    total = total + row['Amount'] * 4
            return f"Estimated yearly income is: ${total: .2f}"

        # default income
        elif "total income" in q:
            total_income = active_income['Amount'].sum()
            return f"Total active income: ${total_income: .2f}"
        
        # specific source income
        else:
            for source in active_income['Source'].unique():
                if source.lower() in q:
                    amount = active_income[active_income['Source'] == source]['Amount'].sum()
                    return f"{source} income is: {amount: .2f}"
                
    except Exception as e:
        print("Error:", e)
        return f"Error accessing income data: {str(e)}"