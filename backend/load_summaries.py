import os
import openai
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# Configurare OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
embedding_model = "text-embedding-3-small"

# Citire rezumate din fișier
summaries = []
with open("book_summaries.md", encoding="utf-8") as f:
    lines = f.readlines()
    current_title = None
    current_summary = []
    for line in lines:
        if line.startswith("## Title:"):
            if current_title and current_summary:
                summaries.append({
                    "title": current_title,
                    "summary": " ".join(current_summary).strip()
                })
            current_title = line.replace("## Title:", "").strip()
            current_summary = []
        else:
            if line.strip():
                current_summary.append(line.strip())
    if current_title and current_summary:
        summaries.append({
            "title": current_title,
            "summary": " ".join(current_summary).strip()
        })

# Inițializare ChromaDB
client = chromadb.Client(Settings())
collection = client.create_collection(name="book_summaries")

# Funcție pentru generare embedding
def get_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model=embedding_model
    )
    return response.data[0].embedding

# Încarcă rezumatele în ChromaDB
for idx, book in enumerate(summaries):
    embedding = get_embedding(book["summary"])
    collection.add(
        ids=[str(idx)],
        embeddings=[embedding],
        documents=[book["summary"]],
        metadatas=[{"title": book["title"]}]
    )

# Retriever semantic

def search_books(query, top_k=3):
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return [
        {
            "title": r["title"],
            "summary": d
        }
        for r, d in zip(results["metadatas"], results["documents"])
    ]

if __name__ == "__main__":
    # Exemplu de căutare semantică
    tema = "prietenie și aventură"
    rezultate = search_books(tema)
    for rez in rezultate:
        print(f"Titlu: {rez['title']}\nRezumat: {rez['summary']}\n")
