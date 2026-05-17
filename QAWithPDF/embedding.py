import os
import sys
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.embeddings import BaseEmbedding
from pydantic import Field
from typing import List
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

class DirectGeminiEmbedding(BaseEmbedding):
    gemini_model: str = Field(default="models/text-embedding-004")

    @classmethod
    def class_name(cls) -> str:
        return "DirectGeminiEmbedding"

    def _get_text_embedding(self, text: str) -> List[float]:
        result = genai.embed_content(model=self.gemini_model, content=text)
        return result["embedding"]

    def _get_query_embedding(self, query: str) -> List[float]:
        return self._get_text_embedding(query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)


def download_gemini_embedding(model, document):
    try:
        logging.info("Initializing embedding model")
        embed_model = DirectGeminiEmbedding()

        Settings.llm = model
        Settings.embed_model = embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Creating vector index")
        index = VectorStoreIndex.from_documents(documents=document)

        logging.info("Creating query engine")
        return index.as_query_engine()
    except Exception as e:
        logging.error(f"Error in download_gemini_embedding: {str(e)}")
        raise customexception(e, sys)
