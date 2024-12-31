import os
from dotenv import load_dotenv
import sys
from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.
    """
    try:
        logging.info("Loading Gemini model...")
        # Configure the model with the correct name format
        model = Gemini(
            api_key=GOOGLE_API_KEY,
            model_name="models/gemini-1.0-pro"  # Updated model name format
        )
        logging.info("Gemini model loaded successfully")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        raise customexception(e, sys)