from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline

def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.load_local("vector_db", embeddings)

    pipe = pipeline(
        "text-generation",
        model="mistralai/Mistral-7B-Instruct-v0.1",
        max_new_tokens=256,
        device_map="auto"
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )
