# 📄 Qnays — Q&A with Documents

A Streamlit-powered RAG (Retrieval-Augmented Generation) application that lets you upload a PDF or text document and ask natural language questions about its contents. Answers are generated using Google Gemini via LlamaIndex.

---

## 🚀 Features

- Upload PDF or TXT documents directly through the browser
- Ask natural language questions about the document's content
- Powered by Google Gemini LLM and Gemini Embeddings
- Built on LlamaIndex for intelligent document indexing and retrieval
- Structured logging and custom exception handling
- Auto-installs missing dependencies on first run

---

## 🛠️ Tech Stack

| Layer | Library / Tool |
|---|---|
| UI | Streamlit |
| LLM | Google Gemini (`gemini-pro`) |
| Embeddings | Gemini Embeddings via LlamaIndex |
| Document Indexing | LlamaIndex Core |
| PDF Parsing | pypdf |
| Text Processing | NLTK |
| Config | python-dotenv |

---

## 📁 Project Structure

```
qnays/
├── QAWithPDF/
│   ├── data_ingestion.py     # Loads and parses uploaded documents
│   ├── embedding.py          # Creates Gemini embeddings & query engine
│   └── model_api.py          # Initialises the Gemini LLM
├── Data/                     # Directory for storing uploaded documents
├── storage/                  # LlamaIndex vector index persistence
├── logs/                     # Application log files
├── notebook/                 # Experimental Jupyter notebooks
├── Experiments/              # R&D and prototyping scripts
├── .streamlit/               # Streamlit configuration
├── StreamlitApp.py           # Main application entry point
├── exception.py              # Custom exception handler
├── logger.py                 # Logging configuration
├── setup_nltk.py             # NLTK data setup helper
├── setup.py                  # Package setup
├── requirements.txt          # Python dependencies
├── packages.txt              # System-level dependencies
└── template.py               # Project scaffolding script
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/DivyanshTiwari20/qnays.git
cd qnays
```

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the application

```bash
streamlit run StreamlitApp.py
```

---

## 🧑‍💻 Usage

1. Open the app in your browser (default: `http://localhost:8501`).
2. Upload a **PDF** or **TXT** file using the file uploader.
3. Type your question in the text input field.
4. Click **Submit & Process** — the app will index your document and return an answer.

---

## 📦 Dependencies

```
llama-index-core>=0.10.11.post1
llama-index-llms-gemini>=0.1.4
llama-index-embeddings-gemini>=0.1.4
llama-index-readers-file>=0.1.0
google-generativeai>=0.3.2
pypdf>=3.17.1
python-dotenv>=1.0.0
streamlit>=1.29.0
nltk>=3.8.1
```

---

## 🔍 How It Works

1. **Data Ingestion** — The uploaded file is read and parsed into LlamaIndex `Document` objects.
2. **Embedding** — Gemini Embeddings convert document chunks into vector representations and build a query engine backed by a vector index.
3. **Query** — The user's question is embedded and matched against stored vectors; the top relevant chunks are retrieved and passed to Gemini to generate a grounded answer.

---

## 📝 Logging

All application events are written to timestamped log files under the `logs/` directory, and also streamed to stdout at `INFO` level for easy debugging.

---

## 🤝 Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project does not currently specify a license. Please contact the author before using it in production or distributing it.
