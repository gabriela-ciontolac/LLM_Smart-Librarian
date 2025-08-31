async def generate_book_image(title, summary):
    prompt = f"Copertă sugestivă sau scenă reprezentativă pentru cartea '{title}': {summary}"
    response = openai.images.generate(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response.data[0].url
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
from tools import get_summary_by_title

openai.api_key = os.getenv("OPENAI_API_KEY")
embedding_model = "text-embedding-3-small"

app = FastAPI()

# CORS pentru frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inițializare ChromaDB
client = chromadb.Client(Settings())
collection = client.get_collection(name="book_summaries")

def get_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model=embedding_model
    )
    return response.data[0].embedding

def search_books(query, top_k=1):
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

async def gpt_recommendation(user_query, book):
    prompt = f"Utilizatorul caută o carte: '{user_query}'. Recomandă-i cartea '{book['title']}' și explică de ce se potrivește, folosind un ton conversațional. Include rezumatul: {book['summary']}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content



@app.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    user_query = data.get("question", "")

    # Filtru limbaj nepotrivit
    bad_words = [
        "prost", "idiot", "tampit", "porc", "bou", "dement", "nesimtit", "ratat", "fraier"
    ]
    normalized = user_query.lower()
    if any(word in normalized for word in bad_words):
        return {
            "response": "Te rugăm să folosești un limbaj respectuos. Librarian AI nu poate răspunde la mesaje cu limbaj nepotrivit.",
            "book": None,
            "full_summary": None
        }

    results = search_books(user_query, top_k=1)
    if not results:
        return {"response": "Nu am găsit nicio carte potrivită."}
    book = results[0]
    gpt_response = await gpt_recommendation(user_query, book)
    full_summary = get_summary_by_title(book["title"])
    image_url = await generate_book_image(book["title"], full_summary)
    return {
        "response": gpt_response,
        "book": book,
        "full_summary": full_summary,
        "image_url": image_url
    }
