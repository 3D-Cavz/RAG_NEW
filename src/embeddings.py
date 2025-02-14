from langchain.embeddings import HuggingFaceBgeEmbeddings


def load_embedding_model():
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    return HuggingFaceBgeEmbeddings(
        model_name="BAAI/bge-large-en", 
        model_kwargs=model_kwargs, 
        encode_kwargs=encode_kwargs
    )