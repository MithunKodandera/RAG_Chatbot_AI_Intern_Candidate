FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["bash", "-c", "python ingest.py && uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port 8501"]
