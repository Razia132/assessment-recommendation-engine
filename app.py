import streamlit as st
from rag_engine import load_catalog, build_vector_store, recommend

st.title("GenAI Assessment Recommendation System")

query = st.text_input("Enter candidate profile or query:")

if query:
    docs = load_catalog()
    vectorstore = build_vector_store(docs)
    result = recommend(query, vectorstore)

    st.subheader("Recommended Assessments")
    st.write(result)
