import streamlit as st
# Must be the first Streamlit command
st.set_page_config(page_title="Q&A with Documents")

import logging
from pathlib import Path
from setup_nltk import setup_nltk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def install_requirements():
    """Install required packages from requirements.txt"""
    try:
        import subprocess
        import sys
        logger.info("Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        logger.info("Requirements installed successfully")
        st.rerun()
    except Exception as e:
        logger.error(f"Failed to install requirements: {e}", exc_info=True)
        st.error(f"Failed to install requirements: {str(e)}")
        return False
    return True

def load_dependencies():
    """Load all required dependencies"""
    try:
        logger.info("Loading dependencies...")
        
        # Set up NLTK first
        if not setup_nltk():
            logger.error("Failed to set up NLTK")
            st.error("Failed to set up NLTK.")
            return False
            
        # Import required modules
        from QAWithPDF.data_ingestion import load_data
        from QAWithPDF.embedding import download_gemini_embedding
        from QAWithPDF.model_api import load_model
        from llama_index.embeddings.gemini import GeminiEmbedding
        
        logger.info("Dependencies successfully loaded")
        return True
    except ImportError as e:
        logger.error(f"Import Error: {e}", exc_info=True)
        st.error(f"Import Error: {str(e)}")
        st.info("Installing required packages...")
        return install_requirements()

def process_document(doc, question):
    """Process the document and generate response"""
    try:
        from QAWithPDF.data_ingestion import load_data
        from QAWithPDF.embedding import download_gemini_embedding
        from QAWithPDF.model_api import load_model
        
        logger.info(f"Processing document: {doc.name}")
        document = load_data(doc)
        
        logger.info("Loading model...")
        model = load_model()
        
        logger.info("Creating query engine...")
        query_engine = download_gemini_embedding(model, document)
        
        logger.info("Generating response...")
        response = query_engine.query(question)
        
        return response.response
    except Exception as e:
        logger.error(f"Error processing document: {e}", exc_info=True)
        raise

def main():
    """Main application function"""
    try:
        logger.info("Starting main application...")
        
        st.title("Q&A with Documents (Information Retrieval)")
        
        # File uploader
        doc = st.file_uploader("Upload your document", type=['pdf', 'txt'])
        
        # Question input
        user_question = st.text_input("Ask your question")
        
        # Process button
        if doc is not None and user_question and st.button("Submit & Process"):
            with st.spinner("Processing your document... This might take a moment."):
                try:
                    response = process_document(doc, user_question)
                    st.write(response)
                except Exception as e:
                    st.error("Failed to process document.")
                    st.exception(e)
    
    except Exception as e:
        logger.error(f"Error in main: {e}", exc_info=True)
        st.error("An unexpected error occurred.")
        st.exception(e)

if __name__ == "__main__":
    if load_dependencies():
        main()
    else:
        st.error("Failed to initialize application. Please check the logs.")