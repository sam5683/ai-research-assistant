from pydantic import BaseModel
from fastapi import APIRouter

from app.services.rag_service import (
    retrieve_relevant_chunks
)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


class SearchRequest(BaseModel):
    query: str


@router.post("")
async def search(request: SearchRequest):

    results = await retrieve_relevant_chunks(
        request.query,
        top_k=5
    )

    return results