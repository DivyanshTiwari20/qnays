import os
import sys
import streamlit as st
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()  # works locally

# This is the fix — read from st.secrets on Streamlit Cloud, fallback to .env locally
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    try:
        logging.info("Loading Gemini model...")
        model = Gemini(
            api_key=GOOGLE_API_KEY,
            model_name="gemini-2.5-flash-lite"  # ← updated, gemini-1.0-pro is deprecated
        )
        logging.info("Gemini model loaded successfully")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        raise customexception(e, sys)
