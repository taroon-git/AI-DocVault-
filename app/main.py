from fastapi import FastAPI, File, UploadFile
import shutil
import os
from app.extract_text import extract_text_from_pdf, split_text_into_chunks
from app.database import get_db_connection
from app.embedder import store_embeddings_in_faiss,search_query_in_faiss
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse


app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)


# Initialize Jinja2 Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



def store_chunks_in_db(filename:str, chunks:list):
    """
    Stores extracted chunks into MySQL database
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO document_chunks (filename, chunk_index, chunk_text) VALUES (%s, %s, %s)"
    values = [(filename, i, chunk) for i, chunk in enumerate(chunks)]

    cursor.executemany(query, values)
    conn.commit()

    cursor.close()
    conn.close()



@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    ## save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ## Extract text from the saved file
    extracted_text = extract_text_from_pdf(file_path)
    # print("📝 Extracted Text:", extracted_text)  # Debugging log


    ## split text into chunks
    text_chunks = split_text_into_chunks(extracted_text)

    ## Store into MySQL
    store_chunks_in_db(file.filename, text_chunks)

    ## Generate & store embeddings in faiss
    store_embeddings_in_faiss()


    return {
        "filename": file.filename,
        "message": "File uploaded, stored in database, and indexed in FAISS!"
    }


@app.post("/query/")
async def query_endpoint(user_query: str):
    """
    Handles user queries by searching FAISS index and returning relevant text.
    
    :param user_query: The query from the user.
    :return: Relevant document chunks.
    """
    results = search_query_in_faiss(user_query)
    print(results)
    return {"query": user_query, "results": results}
