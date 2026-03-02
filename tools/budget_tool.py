import pandas as pd
import sqlite3
from langchain.tools import tool

conn = sqlite3.connect("finance.db")


budget = pd.read_sql_query("SELECT * FROM budget", conn)
transactions = pd.read_sql_query("SELECT * FROM transactions", conn)

@tool
def budget_tracker(query:str) -> str:
    """Check the budget for each category

    Args : the query to check category (e.g."Food & Drinks","Entertainment")

    Returns:
        Category names and total amount of the each budget category 
    """

    try:
        budget['Budget Amount'] = pd.to_numeric(budget['Budget Amount'],errors='coerce')

        category_map = {
            "Food":"Food & Drinks",
            "Drink":"Food & Drinks",
            "Entertainment":"Entertainment",
            "Utilities":"Utilities",
            "Groceries":"Groceries",
            "Transport":"Transport" 
        }

        matched_category = None
        for keyword,category_name in category_map.items():
            if keyword.lower() in query.lower():
                matched_category = category_name
                break
        if matched_category:
            budgeted_amount = budget[budget['Category'] == matched_category]['Budget Amount'].sum()
            actual_spending = transactions[transactions['Category'] == matched_category]['Amount'].sum()
            return f"Budget for {matched_category} is: ${budgeted_amount: .2f}, Actual spending is: ${actual_spending: .2f}."
        return "Query not understood"

    except Exception as e:
        return f"Error accessing budget: {str(e)}"