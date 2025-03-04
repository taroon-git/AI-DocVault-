# AI DocVault 🔐

## Project Overview
AI DocVault is an advanced document upload and processing system powered by FastAPI. It enables seamless text extraction, embedding, indexing, and retrieval using state-of-the-art machine learning models.

## Features
- **Document Upload**: Upload PDFs for automated text extraction.
- **Text Processing**: Extract and clean text from uploaded documents.
- **Embeddings & Indexing**: Generate vector embeddings and store them using FAISS for efficient retrieval.
- **Database Storage**: Store document metadata and extracted text in MySQL.
- **FastAPI Backend**: Expose APIs for document processing and retrieval.
- **Scalability**: Optimized for deployment on Render.

## Technologies Used
- **FastAPI** - High-performance web framework
- **FAISS** - Facebook AI Similarity Search for indexing
- **MySQL** - Database for structured document storage
- **LLMs (Large Language Models)** - Used for document understanding and retrieval
- **PyMuPDF** - Extract text from PDFs

## Folder Structure
```
│── app/
│   ├── main.py          # FastAPI entry point (API setup)
│   ├── database.py      # MySQL connection
│   ├── embedder.py      # Generate embeddings & FAISS handling
│   ├── extract_text.py  # Extract text from PDFs
│   ├── models.py        # Define MySQL table structure
│── faiss_index/         # Directory to store FAISS index
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone <repo-link>
cd AI_DocVault
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database
- Update `database.py` with your MySQL credentials.
- Run migrations if needed.

### 5. Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 6. API Endpoints
- `POST /upload` - Upload and process a document
- `GET /search` - Retrieve information based on a query

## Deployment
For a fully free deployment, Render is recommended:
1. Push the code to GitHub.
2. Link the GitHub repo to Render.
3. Select FastAPI as the environment.
4. Configure environment variables (database credentials, etc.).
5. Deploy and get your API running!

## Contributors
- **Your Name** - Developer & Maintainer

---
🚀 **AI DocVault 🔐** - Secure, scalable, and efficient document processing.

