import os
import argparse
import json
from src.processor import extract_file_content
from src.classifier import SemanticFilter
from rich.console import Console
from rich.table import Table

console = Console()


def run_pipeline(input_dir: str, query: str, threshold: float = 0.25):
    console.print(f"[bold cyan]Scanning directory:[/bold cyan] {input_dir}")
    console.print(f"[bold green]Target Filter Query:[/bold green] '{query}'")

    clf = SemanticFilter()
    results = []

    for root, _, files in os.walk(input_dir):
        for file in files:
            path = os.path.join(root, file)
            parsed = extract_file_content(path)
            score = clf.compute_similarity(query, parsed["content"])

            is_match = score >= threshold
            results.append({
                "file": file,
                "score": score,
                "matched": is_match,
                "type": parsed["type"]
            })

    table = Table(title="OmniIngest Ingestion & Relevance Results")
    table.add_column("File Name", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Relevance Score", justify="right")
    table.add_column("Status", style="bold")

    for r in results:
        status = "[green]Keep (Sync)[/green]" if r["matched"] else "[dim]Ignore[/dim]"
        table.add_row(r["file"], r["type"], str(r["score"]), status)

    console.print(table)

    with open("ingest_manifest.json", "w") as f:
        json.dump(results, f, indent=2)
    console.print("\n[dim]Exported ingestion manifest to ingest_manifest.json[/dim]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OmniIngest Core CLI")
    parser.add_argument("--dir", type=str, required=True, help="Directory to scan")
    parser.add_argument("--query", type=str, required=True, help="Filter criterion")
    args = parser.parse_args()

    run_pipeline(args.dir, args.query)
