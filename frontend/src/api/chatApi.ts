const API_URL = "http://localhost:8000/recommend";
import { BotMessage } from "../types/BotMessage";

export async function sendChatMessage(question: string): Promise<BotMessage> {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });
  const data = await res.json();
  return {
    role: "bot",
    content: data.response,
    bookTitle: data.book?.title,
    fullSummary: data.full_summary,
    image_url: data.image_url,
  };
}
