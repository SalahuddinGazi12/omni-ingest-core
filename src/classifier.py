from sentence_transformers import SentenceTransformer, util


class SemanticFilter:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Uses a lightweight, free open-source embedding model."""
        self.model = SentenceTransformer(model_name)

    def compute_similarity(self, target_query: str, content_preview: str) -> float:
        """Returns cosine similarity score between query and document text."""
        embeddings = self.model.encode([target_query, content_preview])
        score = util.cos_sim(embeddings[0], embeddings[1]).item()
        return round(score, 4)
