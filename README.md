# 🤖 RAG Chatbot – AI Engineer Intern Assignment

This repository contains a **production-ready Retrieval-Augmented Generation (RAG) chatbot** designed as part of an **AI Engineer Intern evaluation**.

The project aligns with expectations from **Appening, Great Learning, and TheCophil**, focusing on:
- Clean architecture
- Practical RAG implementation
- Open-source LLM usage (no paid APIs)
- Deployability (Docker)
- Simple UI for demonstration

---

## 🚀 Key Highlights
- HuggingFace embeddings + LLM (no OpenAI key required)
- FAISS vector database
- Streamlit Chat UI
- FastAPI backend
- Dockerized for easy deployment
- Clear, modular code structure

---

## 🧠 Tech Stack
- Python 3.10
- HuggingFace Transformers
- Sentence-Transformers
- FAISS
- LangChain
- FastAPI
- Streamlit
- Docker

---

## 📁 Project Structure
```
rag-chatbot-ai-intern/
├── app.py            # FastAPI backend
├── streamlit_app.py  # Streamlit UI
├── ingest.py         # Document ingestion
├── rag.py            # RAG pipeline
├── requirements.txt
├── Dockerfile
├── data/sample.pdf
└── queries/sample_queries.md
```

---

## ⚙️ Setup (Local)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ingest.py
uvicorn app:app --reload
```

Streamlit UI:
```bash
streamlit run streamlit_app.py
```

---

## 🐳 Docker Setup

```bash
docker build -t rag-chatbot .
docker run -p 8000:8000 -p 8501:8501 rag-chatbot
```

---

## 🏗️ Architecture Overview

1. **Ingestion**
   - PDF → chunking → embeddings
2. **Storage**
   - FAISS vector index
3. **Retrieval**
   - Semantic similarity search
4. **Generation**
   - Retrieved context + HuggingFace LLM
5. **Interaction**
   - REST API & Streamlit UI

This ensures **low hallucination**, **context-aware**, and **scalable** responses.

---

## 💬 Sample Queries
See `queries/sample_queries.md`

---

## 🎯 Evaluation Alignment
✔ Practical RAG usage  
✔ Open-source stack  
✔ Clear code separation  
✔ Deployable solution  
✔ UI + API demonstration  

---

## 👨‍💻 Author
**Mithun Kodandera**  
AI Engineer Intern Candidate
