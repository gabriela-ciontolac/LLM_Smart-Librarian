export interface BotMessage {
  role: string;
  content: string;
  bookTitle?: string;
  fullSummary?: string;
  image_url?: string;
}
