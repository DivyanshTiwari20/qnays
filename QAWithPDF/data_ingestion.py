from llama_index.core import SimpleDirectoryReader
import sys
import os
from exception import customexception
from logger import logging
import tempfile

def load_data(uploaded_file):
    """
    Load document from Streamlit uploaded file.
    Args:
        uploaded_file: StreamlitUploadedFile object
    Returns:
        documents: List of documents
    """
    try:
        if uploaded_file is None:
            raise ValueError("No file uploaded")
            
        # Get file extension
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        if file_extension not in ['.pdf', '.txt']:
            raise ValueError(f"Unsupported file type: {file_extension}")
            
        # Create temp directory
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            
        # Save file
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
            
        # Load document
        reader = SimpleDirectoryReader(input_files=[temp_file_path])
        documents = reader.load_data()
            
        # Clean up
        os.remove(temp_file_path)
        os.rmdir(temp_dir)
            
        if not documents:
            raise ValueError("Could not extract content from file")
            
        return documents
        
    except Exception as e:
        raise customexception(str(e), sys)