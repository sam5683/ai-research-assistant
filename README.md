# Part 1 — AI Research & Evaluation

# AI Research Assistant

## Live Demo

https://ai-research-assistant-8g5s.onrender.com/

## API Documentation

https://ai-research-assistant-8g5s.onrender.com/docs

## Problem Statement

Researchers, product managers, engineers, and business teams often need to search through large collections of documentation, PDFs, reports, technical references, and research material.

Traditional keyword search frequently fails to retrieve semantically relevant information, resulting in slow research workflows and poor knowledge discovery.

## Proposed Solution

Build an AI-powered Research Assistant that allows users to upload documents, generate vector embeddings, perform semantic search, and receive grounded answers using Retrieval-Augmented Generation (RAG).

The system supports:

* PDF uploads
* Image uploads
* OCR text extraction
* Semantic search
* Question answering over uploaded knowledge
* Source attribution

The goal is to improve information retrieval accuracy while reducing the time required to manually search large document collections.




## LLM Pricing Evaluation (June 2026)

For an AI Research Assistant, pricing is a critical factor because Retrieval-Augmented Generation (RAG) systems repeatedly inject retrieved context into prompts. This means input token costs often become a major operational expense as usage scales.

| Model             | Input Cost (per 1M tokens) | Output Cost (per 1M tokens) |
| ----------------- | -------------------------- | --------------------------- |
| Gemini 2.5 Flash  | $0.30                      | $2.50                       |
| Claude Sonnet 4.6 | $3.00                      | $15.00                      |
| GPT-5.4 Mini      | $0.75                      | $4.50                       |
| GPT-5.4           | $2.50                      | $15.00                      |

### Cost Analysis

**Gemini 2.5 Flash**

* Lowest cost among the evaluated production-grade models.
* Approximately 10× cheaper than Claude Sonnet 4.6 for input tokens.
* Well suited for RAG workloads where large document chunks are frequently injected into prompts.

**Claude Sonnet 4.6**

* Highest cost among the evaluated models.
* Justified when advanced reasoning, coding, or complex analysis is the primary requirement.
* May require prompt caching strategies to control operating costs.

**GPT-5.4 Mini**

* Provides a balance between affordability and capability.
* More expensive than Gemini Flash but significantly cheaper than full-sized frontier models.
* Suitable for structured-output and general-purpose AI assistants.

**GPT-5.4**

* Enterprise-grade model with substantially higher costs.
* Better suited to complex reasoning tasks where model quality is prioritized over operating expenses.
* Note: Extremely large prompts may incur higher pricing tiers, making GPT-5.4 less cost-efficient than Gemini 2.5 Flash for large-scale RAG workloads.

### Recommendation

For this AI Research Assistant prototype, Gemini 2.5 Flash is the preferred model because:

1. It provides the lowest input token cost.
2. RAG systems continuously inject retrieved context into prompts.
3. Lower token costs allow the system to scale without rapidly increasing infrastructure expenses.
4. The model remains capable of handling document-centric workflows while maintaining cost efficiency.



## LLM Context Window & Document Processing Evaluation

For an AI Research Assistant, the ability to process large documents efficiently is critical. Research papers, technical documentation, legal contracts, and internal knowledge bases often exceed hundreds of pages. Therefore, context window size and document handling capabilities directly affect system performance.

| Feature           | Gemini 2.5 Flash | Claude Sonnet 4.6 | GPT-5.4          | GPT-5.4 Mini   |
| ----------------- | ---------------- | ----------------- | ---------------- | -------------- |
| Context Window    | 1,048,576 tokens | 1,000,000 tokens  | 1,050,000 tokens | 400,000 tokens |
| Max Output Tokens | 65,535           | 64,000           | 128,000          | 128,000        |
| PDF Support       | Yes              | Yes               | Yes              | Yes            |
| Image Support     | Yes              | Yes               | Yes              | Yes            |
| Audio Support     | Yes              | No                | No               | No             |
| Video Support     | Yes              | No                | No               | No             |
| Structured Output | Yes              | Yes               | Yes              | Yes            |

### Analysis

**Gemini 2.5 Flash**

* Supports over 1 million tokens of context.
* Native support for PDF, image, audio, and video processing.
* Can process up to 3,000 document pages per file.
* Well suited for multimodal document workflows.

**Claude Sonnet 4.6**

* Provides a 1 million token context window.
* Strong long-context reasoning capabilities.
* Particularly effective for large research documents, contracts, and codebases.
* Optimized for deep reasoning, coding tasks, and long-context analysis.


**GPT-5.4**

* Largest context window among evaluated models.
* Strong support for structured outputs, tools, file search, and enterprise integrations.
* Suitable for large-scale professional knowledge workflows.

**GPT-5.4 Mini**

* Reduced context window compared to frontier models.
* Lower operating costs.
* Useful for lightweight document analysis and sub-agent tasks.

### Recommendation

For this prototype, Gemini 2.5 Flash provides the best balance between:

1. Cost efficiency.
2. Large-context document processing.
3. Native multimodal support.
4. Scalability for Retrieval-Augmented Generation (RAG).

These characteristics make it an appropriate choice for an AI Research Assistant that processes PDFs, OCR output, and large research documents.

## AI Platform Comparison Summary

### Google Gemini 2.5 Flash

| Category | Details |
|----------|----------|
| Capabilities | Native Embeddings, Multimodal (PDF, Images, Audio, Video), Function Calling, Structured Output |
| Pricing | Input: $0.30 / 1M tokens, Output: $2.50 / 1M tokens |
| Scalability | Context Caching, High-Volume Processing, Cloud-Native Deployment |
| Ease of Integration | Google AI Studio, Vertex AI, Python SDK, Google Cloud Ecosystem |
| Limitations | Reasoning quality can be lower than premium reasoning-focused models |
| Best Use Cases | RAG Systems, OCR Workflows, Document Analysis, Multimodal Applications |

---

### Claude Sonnet 4.6

| Category | Details |
|----------|----------|
| Capabilities | Advanced Reasoning, Coding, Long-Context Analysis, Tool Usage |
| Pricing | Input: $3.00 / 1M tokens, Output: $15.00 / 1M tokens |
| Scalability | Prompt Caching, Enterprise Controls, Large-Context Workloads |
| Ease of Integration | Official SDKs, Enterprise Integrations |
| Limitations | No Native Audio/Video Support, Highest Operating Cost |
| Best Use Cases | Research Workflows, Coding Assistants, Complex Reasoning, Enterprise Applications |

---

### GPT-5.4

| Category | Details |
|----------|----------|
| Capabilities | Strong Reasoning, Structured Outputs, Tool Calling, File Search |
| Pricing | Input: $2.50 / 1M tokens, Output: $15.00 / 1M tokens |
| Scalability | Enterprise Infrastructure, Large-Context Support |
| Ease of Integration | Mature Ecosystem, Extensive Documentation, Broad Adoption |
| Limitations | Higher Cost Compared to Gemini |
| Best Use Cases | Enterprise AI Systems, Agent Workflows, Knowledge Assistants |

---

### GPT-5.4 Mini

| Category | Details |
|----------|----------|
| Capabilities | Lightweight Reasoning, Tool Calling, Multimodal Image Understanding |
| Pricing | Input: $0.75 / 1M tokens, Output: $4.50 / 1M tokens |
| Scalability | High-Volume Workloads, Sub-Agent Architectures |
| Ease of Integration | Same Ecosystem and APIs as GPT-5.4 |
| Limitations | Smaller Context Window, Reduced Reasoning Capability |
| Best Use Cases | Chatbots, Routing Agents, Lightweight AI Services |


## Executive Summary

| Model | Cost | Reasoning | Multimodal | Overall Fit |
|---------|---------|---------|---------|---------|
| Gemini 2.5 Flash | Excellent | Good | Excellent | Best Choice |
| Claude Sonnet 4.6 | Expensive | Excellent | Moderate | Strong Alternative |
| GPT-5.4 | Expensive | Excellent | Good | Enterprise Option |
| GPT-5.4 Mini | Good | Moderate | Good | Budget Option |


## Final Platform Recommendation

Three major AI providers were evaluated: OpenAI, Gemini, and Claude.

For this prototype, Gemini Embeddings were selected for semantic search because of their strong retrieval quality and generous free-tier availability.

Groq was selected for response generation due to its extremely low latency and zero-cost experimentation during development.

For a production-scale AI Research Assistant handling large document collections and long-context reasoning, Gemini 2.5 Flash would be the recommended primary model because of its large context window and multimodal capabilities.

Therefore:

* Prototype: Gemini Embeddings + Groq LLM
* Production Recommendation: Gemini 2.5 Flash + Vector Database


Claude Sonnet 4.6 remains an excellent alternative for advanced reasoning and enterprise security requirements, while OpenAI GPT-5.4 provides a strong ecosystem for structured outputs, tool use, and agentic workflows.

For the objectives of this prototype—document ingestion, OCR processing, semantic search, and grounded question answering—Gemini 2.5 Flash and Groq was selected for most balanced combination of capability, scalability, and cost efficiency.


## Research Sources

- https://platform.claude.com/docs/en/about-claude/models/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://ai.google.dev/gemini-api/docs/models
- https://ai.google.dev/gemini-api/docs/pricing
- https://platform.openai.com/docs/models
- https://platform.openai.com/docs/pricing

All pricing, context window, capability, and platform comparisons were verified using official vendor documentation as of June 2026.


## Architecture Diagram

![Architecture](AI-Assistant_workflow.drawio.png)


# AI Research Assistant

## Live Demo

https://ai-research-assistant-8g5s.onrender.com/

---

## Features

- PDF Upload
- Image OCR
- Semantic Search
- RAG Question Answering
- Source Attribution
- FastAPI Backend
- Groq LLM
- Gemini Embeddings

---

## API Endpoints

POST /documents/upload

POST /documents/{id}/process

POST /documents/ocr

POST /search

POST /rag

GET /documents

GET /documents/{id}

---

## Example Workflow

1. Upload PDF
2. Process Document
3. Generate Embeddings
4. Search Relevant Chunks
5. Ask Question
6. Receive Grounded Answer



## Tool Selection Rationale

| Component                       | Selected Tool               | Reason                                      |
| ------------------------------- | --------------------------- | ------------------------------------------- |
| LLM (Prototype)                 | Groq (Llama 3.1 8B Instant) | Fast inference and free for experimentation |
| LLM (Production Recommendation) | Gemini 2.5 Flash            | Large context window and multimodal support |
| Backend Framework               | FastAPI                     | Async architecture and automatic validation |
| Vector Storage (Prototype)      | In-Memory Dictionary        | Simple implementation for proof-of-concept  |
| Vector Database (Production)    | PostgreSQL + pgvector       | Scalable semantic search and persistence    |
| Embedding Model                 | Gemini Embeddings           | High-quality semantic embeddings            |
| OCR                             | Tesseract OCR               | Open-source and easy to integrate           |


## Architecture & Tool Selection

The AI Research Assistant requires support for asynchronous API calls, document uploads, vector search operations, and integration with external LLM providers. Therefore, selecting an appropriate backend framework is critical.

### FastAPI vs Flask

| Feature           | FastAPI                      | Flask                                 |
| ----------------- | ---------------------------- | ------------------------------------- |
| Async Support     | Native                       | Limited                               |
| Data Validation   | Built-in (Pydantic)          | External libraries required           |
| API Documentation | Automatic OpenAPI generation | Manual or third-party tools           |
| Performance       | High                         | Moderate                              |
| Scalability       | Excellent for I/O workloads  | Good for traditional web applications |
| Type Safety       | Built-in                     | Optional                              |

### Analysis

FastAPI was selected because the system performs multiple I/O-bound operations, including:

* PDF uploads
* OCR processing
* Embedding generation
* Vector database queries
* External LLM API requests

FastAPI's asynchronous architecture allows the application to efficiently handle concurrent requests while waiting for responses from external services.

Additionally, FastAPI's native Pydantic integration provides automatic request validation, reducing the likelihood of malformed data entering the RAG pipeline.

### Recommendation

FastAPI is the preferred backend framework for this prototype due to its strong performance, asynchronous architecture, automatic validation, and suitability for AI-powered applications.




