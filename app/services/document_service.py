import json
import uuid
from pathlib import Path

from fastapi import UploadFile
from pypdf import PdfReader

from app.services.chunk_service import chunk_text
from app.services.embeddings import generate_embedding
from app.services.storage import DOCUMENT_STORE


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


async def save_document(file: UploadFile):

    document_id = str(uuid.uuid4())

    file_path = UPLOAD_DIR / f"{document_id}_{file.filename}"

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "document_id": document_id,
        "filename": file.filename,
        "status": "uploaded"
    }

async def process_document(document_id: str):

    files = list(
        UPLOAD_DIR.glob(f"{document_id}_*")
    )

    if not files:

        return {
            "status": "error",
            "message": "Document not found"
        }

    file_path = files[0]

    extracted_text = ""

    if file_path.suffix.lower() == ".pdf":

        reader = PdfReader(file_path)

        for page in reader.pages:

            extracted_text += (
                page.extract_text() or ""
            )

    else:

        return {
            "status": "error",
            "message": "Currently only PDF processing is supported"
        }

    chunks = chunk_text(extracted_text)

    embeddings = []

    for chunk in chunks:

        embedding = await generate_embedding(chunk)

        embeddings.append(embedding)

    DOCUMENT_STORE[document_id] = {
        "text": extracted_text,
        "chunks": chunks,
        "embeddings": embeddings
    }

    print("\n===== DOCUMENT STORED =====")
    print("DOCUMENT ID:", document_id)
    print("TEXT LENGTH:", len(extracted_text))
    print("CHUNKS:", len(chunks))
    print("STORE SIZE:", len(DOCUMENT_STORE))
    print("STORE ID:", id(DOCUMENT_STORE))
    print("KEYS:", list(DOCUMENT_STORE.keys()))
    print("===========================\n")

    return {
        "document_id": document_id,
        "status": "processed",
        "chunks": len(chunks),
        "text_length": len(extracted_text)
    }