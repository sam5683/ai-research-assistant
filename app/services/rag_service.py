import math
from typing import List, Dict, Any
from app.ai.client import call_llm
from app.core.config import settings
from app.services.storage import DOCUMENT_STORE
from app.services.embeddings import generate_embedding



def cosine_similarity(
    vec_a: List[float],
    vec_b: List[float]
) -> float:
    """
    Calculate cosine similarity between two vectors.
    """
    dot_product = sum(
        a * b for a, b in zip(vec_a, vec_b)
    )
    
    magnitude_a = math.sqrt(
        sum(a * a for a in vec_a)
    )
    magnitude_b = math.sqrt(
        sum(b * b for b in vec_b)
    )
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    
    return dot_product / (magnitude_a * magnitude_b)


async def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3
):

    print("\n===== RETRIEVAL START =====")
    print("STORE ID:", id(DOCUMENT_STORE))
    print("STORE SIZE:", len(DOCUMENT_STORE))
    print("KEYS:", list(DOCUMENT_STORE.keys()))
    print("QUERY:", query)
    print("DOCUMENTS IN STORE:", len(DOCUMENT_STORE))

    if not DOCUMENT_STORE:
        print("DOCUMENT STORE IS EMPTY")
        return []

    query_embedding = await generate_embedding(query)

    scored_chunks = []

    for document_id, doc_data in DOCUMENT_STORE.items():

        chunks = doc_data.get("chunks", [])
        embeddings = doc_data.get("embeddings", [])

        print(
            f"DOCUMENT {document_id} "
            f"CHUNKS={len(chunks)} "
            f"EMBEDDINGS={len(embeddings)}"
        )

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            similarity = cosine_similarity(
                query_embedding,
                embedding
            )

            scored_chunks.append({
                "document_id": document_id,
                "chunk": chunk,
                "similarity": similarity
            })

    scored_chunks.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    print("\nTOP RESULTS:")

    for item in scored_chunks[:3]:

        print(
            item["similarity"],
            item["chunk"][:80]
        )

    print("===========================\n")

    return scored_chunks[:top_k]

async def generate_rag_answer(
    question: str,
    top_k: int = 3
) -> Dict[str, Any]:

    retrieved_chunks = await retrieve_relevant_chunks(
        question,
        top_k=top_k
    )

    if not retrieved_chunks:
        return {
            "answer": "No relevant documents found in the knowledge base.",
            "sources": []
        }

    context = "\n\n".join(
        chunk["chunk"]
        for chunk in retrieved_chunks
    )

    prompt = f"""
Based on the following context, answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = await call_llm(
        prompt=prompt,
        system_prompt="""
You are a RAG assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say that the information was not found.

Do not hallucinate.
""",
        temperature=0.2
    )

    if not answer:
        answer = "Failed to generate response."

    sources = [
        chunk["document_id"]
        for chunk in retrieved_chunks
    ]

    return {
        "answer": answer,
        "sources": sources
    }