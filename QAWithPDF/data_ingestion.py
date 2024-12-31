from llama_index.core import Document
import tempfile
import os
import logging
from pypdf import PdfReader
import io

logger = logging.getLogger(__name__)

def load_data(uploaded_file):
    """Load and process the uploaded document"""
    try:
        if uploaded_file is None:
            raise ValueError("No file uploaded!")

        logger.info(f"Processing uploaded file: {uploaded_file.name}")
        
        # Create temporary directory and file
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        
        logger.info(f"Saving to temporary location: {temp_file_path}")
        
        # Save uploaded file
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # Read content based on file type
        if uploaded_file.name.lower().endswith('.pdf'):
            # Handle PDF files
            pdf_reader = PdfReader(temp_file_path)
            content = ""
            for page in pdf_reader.pages:
                content += page.extract_text() + "\n"
        else:
            # Handle text files with proper encoding detection
            with open(temp_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

        # Create Document object
        document = [Document(text=content)]

        # Cleanup
        logger.info("Cleaning up temporary files")
        os.remove(temp_file_path)
        os.rmdir(temp_dir)

        if not document[0].text.strip():
            raise ValueError("Document is empty or could not be processed!")

        logger.info("Document successfully loaded")
        return document

    except Exception as e:
        logger.error(f"Error in load_data: {e}")
        raise Exception(f"Error in load_data: {str(e)}")