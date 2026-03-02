from langchain.agents import create_agent 
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.bill_tool import bill_tool
from tools.budget_tool import budget_tracker
from tools.income_tool import income_tool   
from tools.transactions_tool import transactions_analyzer
from rag.rag_tool import finance_knowledge_search


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GEMINI-API-KEY"),
    max_tokens = 1024,
    temperature = 0
    )

tools = [
    bill_tool,
    budget_tracker, 
    income_tool, 
    transactions_analyzer, 
    finance_knowledge_search
]

agent = create_agent(llm, tools)