from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.gemini import GeminiEmbedding
import os
import sys
import streamlit as st
from dotenv import load_dotenv
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

def download_gemini_embedding(model, document):
    try:
        logging.info("Initializing Gemini embedding model")
        gemini_embed_model = GeminiEmbedding(
            model_name="text-embedding-004",  # ← updated, embedding-001 is deprecated
            api_key=GOOGLE_API_KEY
        )

        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Creating vector index from documents")
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
