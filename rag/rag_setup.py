from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os

BASE_DIR = os.path.dirname(__file__)
PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")

embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")



def build_db():
    docs = []

    for f in [
        "knowledge/budgeting.txt",
        "knowledge/investing.txt",
        "knowledge/savings_tips.txt"
    ]:
        docs.extend(TextLoader(f).load())

    splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = splitter.split_documents(docs)

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=PERSIST_DIR
    )

    db.persist()
    return db


# auto-load or build
if os.path.exists(PERSIST_DIR):
    db = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
else:
    db = build_db()


retriever = db.as_retriever(search_kwargs={"k": 3})