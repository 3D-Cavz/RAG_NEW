import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from qdrant_db import create_qdrant_index

DATA_PATH = "data"

def ingest_pdfs():
    qdrant = create_qdrant_index()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for pdf in os.listdir(DATA_PATH):
        pdf_path = os.path.join(DATA_PATH, pdf)
        print(f"Processing: {pdf_path}")

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        texts = text_splitter.split_documents(documents)

        qdrant.add_documents(texts)
        print(f"✅ {pdf} indexed successfully")

if __name__ == "__main__":
    ingest_pdfs()
