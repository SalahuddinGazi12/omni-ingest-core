# OmniIngest Core
# OmniIngest Core

A lightweight, zero-shot multi-modal file ingestion and content-filtering engine built with Python and open-weights embeddings.

## Overview
OmniIngest eliminates bulk downloading and bandwidth waste by filtering files, documents, and visual assets before full sync. It scans directory streams, performs content inspection, and scores relevance against natural language queries using local semantic embeddings.

## Key Features
- **Local Embeddings:** Powered by `all-MiniLM-L6-v2` via `sentence-transformers` for zero-cost, local semantic similarity.
- **Multi-Modal Inspection:** Extracts text previews from source code/documents and inspects visual metadata via `Pillow`.
- **Manifest Export:** Generates structured JSON manifests for downstream sync and API pipelines.

## Where to Use
- **RAG & LLM Data Pipelines:** Pre-filter raw local folders (`.txt`, `.md`, `.csv`, `.json`, `.py`) before chunking and indexing into a vector database so only relevant documents are ingested.
- **Edge-to-Cloud Sync Optimization:** Run on local workstations or edge nodes to evaluate large directories and generate a lightweight sync manifest (`ingest_manifest.json`) before uploading over metered or low-bandwidth connections.
- **Automated Dataset Curation:** Quickly triage mixed directories of notes, logs, source code, and image assets against natural language criteria without sending private files to external APIs.
- **Enterprise Archive Auditing:** Scan legacy project directories to locate files matching specific compliance, financial, or technical topics completely offline.

## How to Use

### 1. Installation
Clone the repository and install the required dependencies (Python 3.10+ recommended):

```bash
git clone https://github.com/SalahuddinGazi12/omni-ingest-core
cd omni-ingest-core
pip install -r requirements.txt
```

### 2. Run the CLI Filter
Pass the target directory (`--dir`) and your natural language filter query (`--query`) to `main.py`:

```bash
python main.py --dir ./sample_data --query "financial report or invoice data"
```

### 3. CLI Arguments
| Argument | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `--dir` | `str` | Yes | Path to the local directory you want to scan recursively. |
| `--query` | `str` | Yes | Natural language description of the content you want to keep/sync. |

### 4. Review Output & Manifest
OmniIngest prints a color-coded relevance table in your terminal and automatically writes `ingest_manifest.json` in the working directory:

```json
[
  {
    "file": "q3_invoice.txt",
    "score": 0.6412,
    "matched": true,
    "type": ".txt"
  },
  {
    "file": "banner.png",
    "score": 0.1104,
    "matched": false,
    "type": ".png"
  }
]
```
Downstream scripts or sync tools can read `ingest_manifest.json` and transfer only files where `"matched": true`.
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
