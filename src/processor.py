import os
from PIL import Image


def extract_file_content(filepath: str, max_chars: int = 1000) -> dict:
    ext = os.path.splitext(filepath)[1].lower()
    data = {"path": filepath, "type": ext, "content": "", "metadata": {}}

    try:
        if ext in [".txt", ".md", ".py", ".json", ".csv"]:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                data["content"] = f.read(max_chars)
        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            with Image.open(filepath) as img:
                data["metadata"] = {"size": img.size, "format": img.format}
                data["content"] = f"Image file format {img.format} dimensions {img.size[0]}x{img.size[1]}"
        else:
            data["content"] = f"Binary file with extension {ext}"
    except Exception as e:
        data["content"] = f"Extraction error: {str(e)}"

    return data
