import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Checking backend...");
  const [question, setQuestion] = useState("");
  const [answers, setAnswers] = useState(["", "", "", ""]);

  useEffect(() => {
    fetch("/api/health")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => setStatus(`Connected: ${data.service}`))
      .catch(() => setStatus("Backend unavailable"));
  }, []);

  async function getEasyQuestion() {
    try {
      const res = await fetch("/api/questions/easy");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const data = await res.json(); 

      setQuestion(data.question ?? "");
      setAnswers(Object.values(data.answers ?? {}));
    } catch {
      setStatus("Failed to load easy question");
    }
  }

  async function getMediumQuestion() {
    try {
      const res = await fetch("/api/questions/medium");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const data = await res.json(); 

      setQuestion(data.question ?? "");
      setAnswers(Object.values(data.answers ?? {}));
    } catch {
      setStatus("Failed to load medium question");
    }
  }

  async function getHardQuestion() {
    try {
      const res = await fetch("/api/questions/hard");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const data = await res.json(); 

      setQuestion(data.question ?? "");
      setAnswers(Object.values(data.answers ?? {}));
    } catch {
      setStatus("Failed to load hard question");
    }
  }

  async function submitAnswer(answer) {
    try {
      const res = await fetch("/api/answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answer }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const data = await res.json(); 
      setStatus(`Your answer is ${data.result}`);
    } catch {
      setStatus("Failed to submit answer");
    }
  }

  return (
    <main className="app">
      <h1>Trivia!</h1>
      <p>{status}</p>
      <button id="easy" onClick={getEasyQuestion}>Load Easy</button>
      <button id="medium" onClick={getMediumQuestion}>Load Medium</button>
      <button id="hard" onClick={getHardQuestion}>Load Hard</button>

      <h3>{question}</h3>
      <div id="quizButtons">
        {answers.map((answer, i) => (
          <button key={i} onClick={() => submitAnswer(answer)}>
            {answer}
          </button>
        ))}
      </div>
    </main>
  );
}

export default App;
