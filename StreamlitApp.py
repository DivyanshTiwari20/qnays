import streamlit as st
from setup_nltk import setup_nltk

def install_requirements():
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        st.rerun()
    except Exception as e:
        st.error(f"Failed to install requirements: {str(e)}")

def load_dependencies():
    try:
        # Set up NLTK first
        if not setup_nltk():
            return False
            
        from QAWithPDF.data_ingestion import load_data
        from QAWithPDF.embedding import download_gemini_embedding
        from QAWithPDF.model_api import load_model
        from llama_index.embeddings.gemini import GeminiEmbedding
        return True
    except ImportError as e:
        st.error(f"Import Error: {str(e)}")
        st.error("Installing required packages...")
        install_requirements()
        return False

def main():
    if not load_dependencies():
        return

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
                
                document = load_data(doc)
                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                    
                response = query_engine.query(user_question)
                st.write(response.response)
                
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)
                
if __name__ == "__main__":
    main()