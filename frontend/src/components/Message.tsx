import React from "react";

interface MessageProps {
  role: string;
  content: string;
}

const Message: React.FC<MessageProps> = ({ role, content }) => (
  <div style={{ textAlign: role === "user" ? "right" : "left", margin: "8px 0" }}>
    <span style={{ fontWeight: role === "user" ? "bold" : "normal" }}>
      {role === "user" ? "Tu:" : "Librarian AI:"}
    </span>
    <div>{content}</div>
  </div>
);

export default Message;
