import uuid
from fastapi import APIRouter, UploadFile, File
from app.services.storage import DOCUMENT_STORE
from app.services.chunk_service import chunk_text
from app.services.embeddings import generate_embedding
from app.services.ocr_service import (extract_text_from_image)
from app.services.document_service import (
    save_document,
    process_document
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    return await save_document(file)


@router.post("/{document_id}/process")
async def process_uploaded_document(
    document_id: str
):
    return await process_document(document_id)


@router.get("")
async def get_documents():

    results = []

    for document_id, data in DOCUMENT_STORE.items():

        results.append({
            "document_id": document_id,
            "source": data.get("source", "pdf"),
            "chunks": len(data.get("chunks", [])),
            "text_length": len(data.get("text", ""))
        })

    return results

@router.get("/{document_id}")
async def get_document(document_id: str):

    document = DOCUMENT_STORE.get(document_id)

    if not document:

        return {
            "error": "Document not found"
        }

    return {
        "document_id": document_id,
        "text_length": len(document["text"]),
        "chunks": len(document["chunks"]),
        "preview": document["text"][:1000]
    }

@router.post("/ocr")
async def ocr_document(
    file: UploadFile = File(...)
):

    text = await extract_text_from_image(file)

    chunks = chunk_text(text)

    embeddings = []

    for chunk in chunks:

        embedding = await generate_embedding(
            chunk
        )

        embeddings.append(
            embedding
        )

    document_id = str(
        uuid.uuid4()
    )

    DOCUMENT_STORE[document_id] = {

        "text": text,

        "chunks": chunks,

        "embeddings": embeddings,

        "source": "ocr"
    }

    return {

        "document_id": document_id,

        "source": "ocr",

        "text_length": len(text),

        "chunks": len(chunks)
    }