import os
import sys
import requests
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.embeddings import BaseEmbedding
from pydantic import Field
from typing import List
from exception import customexception
from logger import logging

load_dotenv()
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

class DirectGeminiEmbedding(BaseEmbedding):
    api_key: str = Field(default="")

    @classmethod
    def class_name(cls) -> str:
        return "DirectGeminiEmbedding"

    def _embed(self, text: str) -> List[float]:
        url = (
            "https://generativelanguage.googleapis.com/v1/models/"
            "text-embedding-004:embedContent"
        )
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key,
        }
        body = {
            "model": "models/text-embedding-004",
            "content": {"parts": [{"text": text}]},
        }
        resp = requests.post(url, headers=headers, json=body)
        resp.raise_for_status()
        return resp.json()["embedding"]["values"]

    def _get_text_embedding(self, text: str) -> List[float]:
        return self._embed(text)

    def _get_query_embedding(self, query: str) -> List[float]:
        return self._embed(query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._embed(query)


def download_gemini_embedding(model, document):
    try:
        logging.info("Initializing embedding model")
        embed_model = DirectGeminiEmbedding(api_key=GOOGLE_API_KEY)

        Settings.llm = model
        Settings.embed_model = embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Creating vector index")
        index = VectorStoreIndex.from_documents(documents=document)

        logging.info("Creating query engine")
        return index.as_query_engine()
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise customexception(e, sys)
