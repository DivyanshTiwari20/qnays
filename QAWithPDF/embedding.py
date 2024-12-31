from llama_index.core import VectorStoreIndex, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.
    """
    try:
        logging.info("Initializing Gemini embedding model")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        # Update Settings
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20
        
        logging.info("Creating vector index from documents")
        # Create index from documents
        index = VectorStoreIndex.from_documents(
            documents=document,
            settings=Settings
        )
        
        logging.info("Creating query engine")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        logging.error(f"Error in download_gemini_embedding: {str(e)}")
        raise customexception(e, sys)