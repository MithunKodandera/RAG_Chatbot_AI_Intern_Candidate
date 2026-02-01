from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_rag_chain

app = FastAPI()
qa = get_rag_chain()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(q: Query):
    return {"answer": qa.run(q.question)}
