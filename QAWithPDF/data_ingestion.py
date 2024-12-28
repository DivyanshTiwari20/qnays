from llama_index import SimpleDirectoryReader
import tempfile
import os

def load_data(uploaded_file):
    try:
        if uploaded_file is None:
            raise ValueError("No file uploaded!")

        # Save the uploaded file to a temporary directory
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)

        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        # Use SimpleDirectoryReader to load the document
        reader = SimpleDirectoryReader(input_files=[temp_file_path])
        documents = reader.load_data()

        # Clean up temporary files
        os.remove(temp_file_path)
        os.rmdir(temp_dir)

        if not documents:
            raise ValueError("Document is empty or could not be processed!")

        return documents

    except Exception as e:
        # Return a clear error message for debugging
        raise Exception(f"Error in load_data: {str(e)}")
