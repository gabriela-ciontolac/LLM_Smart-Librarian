import React from "react";

interface BookSummaryProps {
  title: string;
  summary: string;
}

const BookSummary: React.FC<BookSummaryProps> = ({ title, summary }) => (
  <div style={{ background: "#f9f9f9", borderRadius: 6, padding: 16, marginTop: 12, boxShadow: "0 1px 4px #eee" }}>
    <h3 style={{ marginBottom: 8 }}>{title}</h3>
    <div style={{ whiteSpace: "pre-line" }}>{summary}</div>
  </div>
);

export default BookSummary;
