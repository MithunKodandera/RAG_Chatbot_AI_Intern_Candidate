import streamlit as st
from rag import get_rag_chain

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🤖 RAG Chatbot")

qa = get_rag_chain()

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question")

if query:
    answer = qa.run(query)
    st.session_state.history.append((query, answer))

for q, a in reversed(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
