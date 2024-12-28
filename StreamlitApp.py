import streamlit as st
from setup_nltk import setup_nltk
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def install_requirements():
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        st.rerun()  # Restart Streamlit to load dependencies
    except Exception as e:
        st.error(f"Failed to install requirements: {str(e)}")
        logging.error(f"Failed to install requirements: {e}")

def load_dependencies():
    try:
        # Set up NLTK first
        if not setup_nltk():
            st.error("Failed to set up NLTK.")
            return False
            
        from QAWithPDF.data_ingestion import load_data
        from QAWithPDF.embedding import download_gemini_embedding
        from QAWithPDF.model_api import load_model
        from llama_index.embeddings.gemini import GeminiEmbedding
        logging.info("Dependencies successfully loaded.")
        return True
    except ImportError as e:
        st.error(f"Import Error: {str(e)}")
        logging.error(f"Import Error: {e}")
        st.info("Installing required packages...")
        install_requirements()
        return False

def main():
    try:
        st.set_page_config(page_title="Q&A with Documents")

        st.title("Q&A with Documents (Information Retrieval)")

        doc = st.file_uploader("Upload your document", type=['pdf', 'txt'])
        user_question = st.text_input("Ask your question")

        if doc is not None and user_question and st.button("Submit & Process"):
            with st.spinner("Processing..."):
                from QAWithPDF.data_ingestion import load_data
                from QAWithPDF.embedding import download_gemini_embedding
                from QAWithPDF.model_api import load_model

                # Process the document and user query
                document = load_data(doc)
                model = load_model()
                query_engine = download_gemini_embedding(model, document)

                response = query_engine.query(user_question)
                st.write(response.response)

    except Exception as e:
        # Display detailed error messages for debugging
        st.error("An error occurred while processing your request.")
        st.exception(e)
