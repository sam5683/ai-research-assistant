from pydantic import BaseModel
from fastapi import APIRouter

from app.services.rag_service import generate_rag_answer


class RAGRequest(BaseModel):
    question: str


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.post("")
async def rag_endpoint(request: RAGRequest):
    """
    Retrieve-Augmented Generation endpoint.
    
    Takes a question and returns an answer based on
    the knowledge base with source attribution.
    """
    result = await generate_rag_answer(
        question=request.question,
        top_k=3
    )
    
    return result
