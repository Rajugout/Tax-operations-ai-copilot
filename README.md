# 💼 Tax Operations AI Copilot

A **Multi-Agent Retrieval-Augmented Generation (RAG)** AI Assistant for
Seller Tax Operations.

## Project Overview

This project combines RAG with a Multi-Agent Architecture to resolve
seller tax queries using an uploaded PDF knowledge base.

## Features

-   Upload Tax Knowledge PDF
-   Gemini Embeddings
-   FAISS Vector Database
-   Multi-Agent Workflow
-   Source References
-   AI Copilot Dashboard

## Multi-Agent Workflow

-   Intent Agent
-   Retriever Agent
-   Root Cause Agent
-   Resolution Agent
-   Response Agent
-   Review Agent

## Tech Stack

Python, Streamlit, LangChain, Gemini 2.5 Flash, FAISS, PyPDF,
python-dotenv

## Installation

``` bash
pip install -r requirements.txt
streamlit run app.py
```

Create `.env`

``` text
GOOGLE_API_KEY=YOUR_API_KEY
```

## License

MIT
