import os
import nltk
import streamlit as st

def setup_nltk():
    """
    Set up NLTK data in a user-accessible location
    """
    # Create a custom directory for NLTK data in the user's home directory
    home = os.path.expanduser("~")
    nltk_data = os.path.join(home, "nltk_data")
    
    try:
        # Create the directory if it doesn't exist
        os.makedirs(nltk_data, exist_ok=True)
        
        # Set NLTK data path
        nltk.data.path.append(nltk_data)
        
        # Download required NLTK data
        nltk.download('punkt', download_dir=nltk_data)
        nltk.download('stopwords', download_dir=nltk_data)
        
        return True
    except Exception as e:
        st.error(f"Failed to set up NLTK: {str(e)}")
        return False

if __name__ == "__main__":
    setup_nltk()