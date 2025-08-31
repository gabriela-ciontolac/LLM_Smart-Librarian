# LLM Smart Librarian

LLM Smart Librarian is an AI-powered book recommendation web app. Users can ask for book suggestions, receive detailed summaries, listen to recommendations via text-to-speech, and view AI-generated cover images.

## Features

- **Semantic Book Search:** Finds the best book match for your query using embeddings and ChromaDB.
- **AI Recommendations:** Uses GPT to generate conversational recommendations and summaries.
- **Text-to-Speech:** Listen to recommendations and summaries directly in the browser.
- **Image Generation:** Displays an AI-generated cover or scene for each recommended book.
- **Voice Input:** Ask for recommendations using your microphone.

## Project Structure

```
backend/
  app.py                # FastAPI backend, recommendation logic
  tools.py              # Book summaries and utility functions
  load_summaries.py     # Loads book summaries into ChromaDB
  book_summaries.md     # Source book summaries
  requirements.txt      # Python dependencies

frontend/
  src/
    pages/ChatBot.tsx   # Main chat interface
    api/chatApi.ts      # API calls to backend
    components/         # UI components
    types/              # TypeScript types
  package.json          # Frontend dependencies
  vite.config.ts        # Vite config
```

## Setup

### Backend

1. Install dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in `.env`:
   ```
   OPENAI_API_KEY=your-key-here
   ```
3. Load book summaries into ChromaDB:
   ```sh
   python load_summaries.py
   ```
4. Start the FastAPI server:
   ```sh
   uvicorn app:app --reload
   ```

### Frontend

1. Install dependencies:
   ```sh
   cd frontend
   npm install
   ```
2. Start the development server:
   ```sh
   npm run dev
   ```
3. Open [http://localhost:5173](http://localhost:5173) in your browser.

## Usage

- Type or speak your query (e.g., "Vreau o carte despre prietenie și magie").
- View the recommended book, summary, and generated image.
- Click "Ascultă recomandarea" to listen to the summary.

## Requirements

- Node.js & npm
- Python 3.10+
- OpenAI API key