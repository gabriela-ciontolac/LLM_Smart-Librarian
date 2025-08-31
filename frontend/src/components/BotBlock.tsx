import React from "react";
import BookSummary from "./BookSummary";

interface BotBlockProps {
  content: string;
  bookTitle?: string;
  fullSummary?: string;
  image_url?: string;
  onSpeak?: (text: string) => void;
}

const BotBlock: React.FC<BotBlockProps> = ({ content, bookTitle, fullSummary, image_url, onSpeak }) => (
  <>
    <div>{content}</div>
    {bookTitle && fullSummary && (
      <>
        <BookSummary title={bookTitle} summary={fullSummary} />
        {image_url && (
          <img
            src={image_url}
            alt={`Imagine generată pentru ${bookTitle}`}
            style={{ marginTop: 12, maxWidth: "100%", borderRadius: 8, boxShadow: "0 2px 8px #eee" }}
          />
        )}
        {onSpeak && (
          <button
            style={{ marginTop: 8, padding: "6px 12px", borderRadius: 4, background: "#646cff", color: "#fff", border: "none", cursor: "pointer" }}
            onClick={() => onSpeak(`${content}\n${bookTitle}: ${fullSummary}`)}
          >
            Ascultă recomandarea
          </button>
        )}
      </>
    )}
  </>
);

export default BotBlock;
