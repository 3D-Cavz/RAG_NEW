import os
from fastapi import FastAPI, Query
from qdrant_db import search_query
from youtube_search import search_youtube

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to RAG System"}

@app.get("/search/")
def search(query: str = Query(..., description="Query text")):
    rag_results = search_query(query)  # Search in RAG system
    youtube_results = search_youtube(query)  # Search on YouTube

    return {
        "query": query,
        "rag_results": rag_results,
        "youtube_results": youtube_results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
