from qdrant_client import QdrantClient
from qdrant_client.http import models
from langchain_qdrant import Qdrant
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME
from embeddings import load_embedding_model

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, prefer_grpc=False)
embeddings = load_embedding_model()

def ensure_qdrant_collection():
    """
    Check if the Qdrant collection exists. If not, create a new one.
    """
    collections = client.get_collections().collections
    existing_collections = [c.name for c in collections]

    if COLLECTION_NAME not in existing_collections:
        print(f"⚡ Collection '{COLLECTION_NAME}' does not exist. Creating it now...")
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
        )
        print(f"✅ Collection '{COLLECTION_NAME}' created successfully.")
    else:
        print(f"✅ Collection '{COLLECTION_NAME}' already exists.")

def create_qdrant_index():
    """
    Ensure the collection exists before creating the Qdrant index.
    """
    ensure_qdrant_collection()
    return Qdrant(client=client, embeddings=embeddings, collection_name=COLLECTION_NAME)

def search_query(query, k=5):
    """
    Search the Qdrant index and return the top k results.
    """
    db = create_qdrant_index()
    results = db.similarity_search_with_score(query=query, k=k)
    return [{"score": score, "content": doc.page_content, "metadata": doc.metadata} for doc, score in results]
