import os
import tempfile
from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(uploaded_file):
    """
    Load document from Streamlit uploaded file.

    Parameters:
    - uploaded_file: StreamlitUploadedFile object from st.file_uploader

    Returns:
    - A list of loaded documents processed by SimpleDirectoryReader
    """
    try:
        logging.info("Data loading started...")
        
        if uploaded_file is None:
            raise ValueError("No file was uploaded")
            
        # Create a temporary directory to store the uploaded file
        with tempfile.TemporaryDirectory() as temp_dir:
            logging.info(f"Created temporary directory: {temp_dir}")
            
            # Get the file extension
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            if file_extension not in ['.pdf', '.txt']:
                raise ValueError(f"Unsupported file type: {file_extension}")
                
            temp_file_path = os.path.join(temp_dir, f"uploaded_file{file_extension}")
            
            # Save the uploaded file to temporary directory
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            logging.info(f"Saved uploaded file to: {temp_file_path}")
            
            # Load the document using SimpleDirectoryReader
            try:
                documents = SimpleDirectoryReader(
                    input_files=[temp_file_path]
                ).load_data()
                
                if not documents:
                    raise ValueError("No content could be extracted from the file")
                    
                logging.info("Data loading completed successfully")
                return documents
                
            except ImportError as e:
                raise ImportError("Please install llama-index-readers-file package: pip install llama-index-readers-file")

    except Exception as e:
        logging.error(f"Exception in loading data: {str(e)}")
        raise customexception(str(e), sys)