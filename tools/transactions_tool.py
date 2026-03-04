import pandas as pd
import sqlite3
from langchain.tools import tool

@tool
def transactions_analyzer(query: str) -> str:
    """Analyze transactions, categorize spending, and summarize expenses.

    Args:
        query : the query to check category (e.g."Food & Drinks","Entertainment") 

    Returns:
        Total amount spend on each category 
    """
    try:
        with sqlite3.connect("finance.db") as conn:
            transactions = pd.read_sql_query("SELECT * FROM transactions", conn)

        transactions['Amount'] = pd.to_numeric(transactions['Amount'], errors='coerce')

        # category mapping
        category_map = {
            "Food":"Food & Drinks",
            "Drink":"Food & Drinks",
            "Entertainment":"Entertainment",
            "Utilities":"Utilities",
            "Groceries":"Groceries",
            "Transport":"Transport"    
        }

        # look for matching category in the query
        matched_category = None
        for keyword , category_name in category_map.items():
            if keyword.lower() in query.lower():
                matched_category = category_name
                break
        if matched_category:
            total = transactions[transactions["Category"] == matched_category]['Amount'].sum()
            return f"Total for {matched_category} is: ${total:.2f}"
        return "Query not understood"
    except Exception as e:
        return f"Error accessing transactions{str(e)}"