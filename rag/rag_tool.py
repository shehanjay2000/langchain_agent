from langchain.tools import tool
from rag.rag_setup import retriever


@tool
def finance_knowledge_search(query:str) -> str:
    """ 
    Use this for budgeting tips, saving advice,
    investing help, or general financial knowledge.
    Do NOT use for calculations or numbers.
    """

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant finance knowledge found."
    
    return docs[0].page_content.strip()