# OmniIngest Core

A lightweight, zero-shot multi-modal file ingestion and content-filtering engine built with Python and open-weights embeddings.

## Overview
OmniIngest eliminates bulk downloading and bandwidth waste by filtering files, documents, and visual assets before full sync. It scans directory streams, performs content inspection, and scores relevance against natural language queries using local semantic embeddings.

## Key Features
- **Local Embeddings:** Powered by `all-MiniLM-L6-v2` via `sentence-transformers` for zero-cost, local semantic similarity.
- **Multi-Modal Inspection:** Extracts text previews from source code/documents and inspects visual metadata via `Pillow`.
- **Manifest Export:** Generates structured JSON manifests for downstream sync and API pipelines.

## Quickstart
```bash
git clone https://github.com/SalahuddinGazi12/omni-ingest-core
cd omni-ingest-core
pip install -r requirements.txt
python main.py --dir ./sample_data --query "financial report or invoice data"
```
