import os
from fastapi import FastAPI, Query
from src.qdrant_db import search_query
from src.youtube_search import search_youtube

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to RAG System"}

@app.get("/search/")
def search(query: str = Query(..., description="Query text"), search_type: str = "rag"):
    if search_type == "youtube":
        return {"query": query, "result": search_youtube(query)}
    else:
        results = search_query(query)
        return {"query": query, "results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
