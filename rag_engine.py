from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.docstore.document import Document
import json

def load_catalog():
    with open("data/shl_catalog.json") as f:
        data = json.load(f)
    docs = []
    for item in data:
        content = f"{item['assessment']}: {item['description']} Suitable for roles {item['roles']}"
        docs.append(Document(page_content=content))
    return docs

def build_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)

def recommend(query, vectorstore):
    llm = OpenAI(temperature=0)
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Candidate Query: {query}

    Based on the following assessments:
    {context}

    Recommend the most suitable assessments and explain why.
    """

    return llm(prompt)
def recommend_json(query, vectorstore):
    docs = vectorstore.similarity_search(query, k=3)
    return {
        "query": query,
        "recommended_assessments": [d.page_content for d in docs]
    }
