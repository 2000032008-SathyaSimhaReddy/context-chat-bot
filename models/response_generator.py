from sentence_transformers import SentenceTransformer
import faiss, numpy as np
class ResponseGenerator:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.responses = ["Hello!", "Goodbye!", "Sure, I can help.", "You're welcome!"]
        emb = self.model.encode(self.responses)
        self.index = faiss.IndexFlatL2(emb.shape[1])
        self.index.add(np.array(emb))
    def generate(self, q):
        qe = self.model.encode([q])
        _, i = self.index.search(np.array(qe), 1)
        return self.responses[i[0][0]]
