from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)  # FAISS index for 384-dimensional embeddings

def add_to_index(text):
    sentences = text.split(".")
    embeddings = model.encode(sentences)
    index.add(np.array(embeddings))
    return sentences, index

def get_relevant_context(question, sentences, index):
    question_embedding = model.encode([question])
    D, I = index.search(np.array(question_embedding), k=5)
    return " ".join([sentences[i] for i in I[0]])
