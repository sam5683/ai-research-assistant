from fastapi import APIRouter

from app.api.documents import router as documents_router
from app.api.rag import router as rag_router
from app.api.search import router as search_router

router = APIRouter()

router.include_router(documents_router)
router.include_router(rag_router)
router.include_router(search_router)