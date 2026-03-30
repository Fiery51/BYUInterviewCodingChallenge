import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Checking backend...");
  const [question, setQuestion] = useState("");
  const [answers, setAnswers] = useState([]);
  const [difficulty, setDifficulty] = useState("");
  const [questionNumber, setQuestionNumber] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const [score, setScore] = useState(0);
  const [percentage, setPercentage] = useState(0);
  const [gameStarted, setGameStarted] = useState(false);
  const [gameOver, setGameOver] = useState(false);
  const [answeredCurrent, setAnsweredCurrent] = useState(false);
  const [answerFeedback, setAnswerFeedback] = useState("");

  useEffect(() => {
    fetch("/api/health")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => setStatus(`Connected: ${data.service}`))
      .catch(() => setStatus("Backend unavailable"));
  }, []);

  function loadQuestionFromPayload(payload) {
    const currentQuestion = payload.question;
    setQuestion(currentQuestion?.question ?? "");
    setAnswers(Array.isArray(currentQuestion?.answers) ? currentQuestion.answers : []);
    setQuestionNumber(currentQuestion?.questionNumber ?? 0);
    setScore(payload.score ?? 0);
    setTotalQuestions(payload.totalQuestions ?? 0);
    setPercentage(payload.percentage ?? 0);
    setGameOver(Boolean(payload.gameOver));
    setAnsweredCurrent(false);
    setAnswerFeedback("");
  }

  async function startGame(nextDifficulty) {
    try {
      const res = await fetch(`/api/questions/${nextDifficulty}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data.error) throw new Error(data.error);

      setDifficulty(nextDifficulty);
      setGameStarted(true);
      loadQuestionFromPayload(data);
      setStatus(`Game started: ${nextDifficulty}`);
    } catch {
      setStatus(`Failed to start ${nextDifficulty} game`);
    }
  }

  async function submitAnswer(answer) {
    if (!gameStarted || gameOver) {
      return;
    }
    if (answeredCurrent) {
      setStatus("Current question already answered. Click Next Question.");
      return;
    }

    try {
      const res = await fetch("/api/answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answer }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data.error) throw new Error(data.error);

      setAnsweredCurrent(true);
      setScore(data.score ?? 0);
      setTotalQuestions(data.totalQuestions ?? 0);
      setPercentage(data.percentage ?? 0);
      setAnswerFeedback(data.result === "correct" ? "Correct!" : "Incorrect.");
      setStatus(`Question ${data.questionNumber}: ${data.result}`);
    } catch {
      setStatus("Failed to submit answer");
    }
  }

  async function nextQuestion() {
    if (!gameStarted || gameOver) {
      return;
    }

    try {
      const res = await fetch("/api/next", { method: "POST" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      if (data.error) throw new Error(data.error);

      setScore(data.score ?? 0);
      setTotalQuestions(data.totalQuestions ?? 0);
      setPercentage(data.percentage ?? 0);

      if (data.gameOver || !data.question) {
        setGameOver(true);
        setQuestion("");
        setAnswers([]);
        setAnswerFeedback("");
        setStatus(
          `Game complete! Final score: ${data.score}/${data.totalQuestions} (${data.percentage}%).`
        );
        return;
      }

      loadQuestionFromPayload(data);
      setStatus(`Question ${data.question.questionNumber} of ${data.totalQuestions}`);
    } catch {
      setStatus("Failed to load next question");
    }
  }

  return (
    <main className="app">
      <h1>Trivia!</h1>
      <div id="buttonContainer">
        <button id="easy" onClick={() => startGame("easy")}>Start Easy Game</button>
        <button id="medium" onClick={() => startGame("medium")}>Start Medium Game</button>
        <button id="hard" onClick={() => startGame("hard")}>Start Hard Game</button>
      </div>

      <p>
        Difficulty: {difficulty || "-"} | Question: {questionNumber}/{totalQuestions || 0}
      </p>

      {gameOver && (
        <><p>
          Final Score: {score}/{totalQuestions || 0} ({percentage}%)
        </p><p>Game Over!</p>
        <p>Click a difficulty to start a new game.</p></>
        
      )}

      <div id="progressButtons">
        <button id="next" onClick={nextQuestion} disabled={!gameStarted || gameOver}>
          Next Question
        </button>
      </div>

      <h3>{question}</h3>
      {answerFeedback && <p>{answerFeedback}</p>}
      <div id="quizButtons">
        {answers.map((answer, i) => (
          <button
            key={i}
            onClick={() => submitAnswer(answer)}
            disabled={!gameStarted || gameOver || answeredCurrent}
          >
            {answer}
          </button>
        ))}
      </div>
    </main>
  );
}

export default App;
