import React, { useState, useRef } from "react";
import Message from "../components/Message";
import BotBlock from "../components/BotBlock";
import { sendChatMessage } from "../api/chatApi";
import type { BotMessage } from "../types/BotMessage";

const Chat: React.FC = () => {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState<BotMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [voiceMode, setVoiceMode] = useState(false);
  const [listening, setListening] = useState(false);
  const recognitionRef = useRef<any>(null);
  // Funcție pentru activare/dezactivare voice mode
  const toggleVoiceMode = () => {
    setVoiceMode((v) => !v);
    setListening(false);
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
  };

  // Funcție pentru pornire ascultare microfon
  const startListening = () => {
    if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
      alert('Browserul nu suportă Speech Recognition!');
      return;
    }
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = "ro-RO";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.onresult = (event: any) => {
      const transcript = event.results[0][0].transcript;
      setQuestion(transcript);
      setListening(false);
    };
    recognition.onend = () => {
      setListening(false);
    };
    recognition.onerror = () => {
      setListening(false);
    };
    recognitionRef.current = recognition;
    recognition.start();
    setListening(true);
  };

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;
    setMessages((msgs) => [...msgs, { role: "user", content: question }]);
    setLoading(true);
    try {
      const botMsg = await sendChatMessage(question);
      setMessages((msgs) => [
        ...msgs,
        botMsg,
      ]);
    } catch (err) {
      setMessages((msgs) => [
        ...msgs,
        { role: "bot", content: "Eroare la conectarea cu serverul." },
      ]);
    }
    setLoading(false);
    setQuestion("");
  };

  // Funcție pentru redare text-to-speech
  const speakText = (text: string) => {
    const synth = window.speechSynthesis;
    if (synth.speaking) synth.cancel();
    const utter = new window.SpeechSynthesisUtterance(text);
    utter.lang = "ro-RO";
    synth.speak(utter);
  };

  return (
    <div className="chat-container" style={{ maxWidth: 600, margin: "40px auto", padding: 24, background: "#fff", borderRadius: 8, boxShadow: "0 2px 8px #eee" }}>
      <h2>Recomandări de cărți AI</h2>
      <div style={{ marginBottom: 16 }}>
        <button
          style={{ padding: "6px 12px", borderRadius: 4, background: voiceMode ? "#646cff" : "#ccc", color: "#fff", border: "none", cursor: "pointer", marginRight: 8 }}
          onClick={toggleVoiceMode}
        >
          {voiceMode ? "Voice Mode activ" : "Activează Voice Mode"}
        </button>
        {voiceMode && (
          <button
            style={{ padding: "6px 12px", borderRadius: 4, background: listening ? "#646cff" : "#ccc", color: "#fff", border: "none", cursor: "pointer" }}
            onClick={startListening}
            disabled={listening}
          >
            {listening ? "Ascultă..." : "Vorbește"}
          </button>
        )}
      </div>
      <div className="chat-messages" style={{ minHeight: 200, marginBottom: 16 }}>
        {messages.map((msg, idx) => (
          msg.role === "user" ? (
            <Message key={idx} role={msg.role} content={msg.content} />
          ) : (
            <BotBlock
              key={idx}
              content={msg.content}
              bookTitle={msg.bookTitle}
              fullSummary={msg.fullSummary}
              image_url={msg.image_url}
              onSpeak={speakText}
            />
          )
        ))}
        {loading && <div style={{ textAlign: "center" }}>Se caută recomandarea...</div>}
      </div>
      <form onSubmit={sendMessage} style={{ display: "flex", gap: 8 }}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder={voiceMode ? "Vorbește sau tastează întrebarea..." : "Ex: Vreau o carte despre prietenie și magie"}
          style={{ flex: 1, padding: 8, borderRadius: 4, border: "1px solid #ccc" }}
          disabled={loading || listening}
        />
        <button type="submit" disabled={loading || !question.trim()} style={{ padding: "8px 16px" }}>
          Trimite
        </button>
      </form>
    </div>
  );
};

export default Chat;
