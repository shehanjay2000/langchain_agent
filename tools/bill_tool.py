import datetime
import pandas as pd
import sqlite3
from langchain.tools import tool


conn = sqlite3.connect("finance.db")

bills = pd.read_sql_query("SELECT * FROM bills", conn)


@tool
def bill_tool(query:str) -> str:
    """"REQUIRED TOOL.
    Use this tool for any question about:
    - bills
    - due payments
    - unpaid bills
    - paid bills
    - upcoming bills
    - reminders

    Returns real bill data from CSV.
    """
    try:

        bills['Amount'] = pd.to_numeric(bills['Amount'],errors='coerce')
        bills['Due Date'] = pd.to_datetime(bills['Due Date'],errors='coerce')
        today = datetime.datetime.now()
        q = query.lower()

        if "unpaid" in q:
            unpaid_bills = bills[bills['Status'] == 'Unpaid']['Amount'].sum()
            bill_names = bills[bills['Status'] == 'Unpaid']['Bill Name'].tolist()
            return f"Total unpaid bills:${unpaid_bills:.2f}. Unpaid bills: {','.join(bill_names)}"

        elif "paid" in q:
            paid_bills = bills[bills['Status'] == 'Paid']['Amount'].sum()
            bill_names = bills[bills['Status'] == 'Paid']['Bill Name'].tolist()
            return f"Total paid bills: ${paid_bills:.2f}. Paid bills: {', '.join(bill_names)}"
        
        elif "week" in q:
            week_end = today + datetime.timedelta(days=7)
            result = bills[(bills['Due Date'] >= today) & (bills['Due Date'] <= week_end)]
            return f"Upcoming bills in the next week: {result.to_string(index=False)}"
        
        elif "month" in q:
            result = bills[bills['Due Date'].dt.month == today.month]
            return f"Upcoming bills in the current month: {result.to_string(index=False)}"
        else:
            return "Query not understood..Specify 'paid bills', 'unpaid bills', 'bills due this week' or 'bills due this month'"
    except Exception as e:
        return f"Error accessing bills: {str(e)}"