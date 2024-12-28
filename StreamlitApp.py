import streamlit as st

try:
    from QAWithPDF.data_ingestion import load_data
    from QAWithPDF.embedding import download_gemini_embedding
    from QAWithPDF.model_api import load_model
    from llama_index.embeddings.gemini import GeminiEmbedding  # Changed from llama_index.embeddings.gemini
except ImportError as e:
    st.error(f"Import Error: {str(e)}")
    st.error("Installing required packages...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    st.experimental_rerun()
def main():
    try:
        st.set_page_config("Q&A with Documents")
        
        doc=st.file_uploader("upload your document")
        
        st.header("QA with Documents(Information Retrieval)")
        
        user_question= st.text_input("Ask your question")
        
        if st.button("submit & process"):
            with st.spinner("Processing..."):
                document=load_data(doc)
                model=load_model()
                query_engine=download_gemini_embedding(model,document)
                    
                response = query_engine.query(user_question)
                    
                st.write(response.response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
                
if __name__=="__main__":
    main()          
                