import { useEffect, useState } from "react";

function App() {
  buttonContainer = document.getElementById("quizButtons");
  question = document.getElementById("question");
  button1 = buttonContainer.children[0];
  button2 = buttonContainer.children[1];
  button3 = buttonContainer.children[2];
  button4 = buttonContainer.children[3];
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    fetch("/api/health")
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        setStatus(`Connected: ${data.service}`);
      })
      .catch(() => {
        setStatus("Backend unavailable");
      });
  }, []);


  async function getEasyQuestion(){
    try {
      const res = await fetch('/api/questions/easy', {
        method: 'GET',
      });
      const data = await res.json().catch((err) => {});
      button1 = data
    } catch (error) {
      throw new Error('Failed to get new question');
    }
  }




  return (
    <main className="app">
      <h1>Trivia!</h1>
      <button id="easy" onClick={getEasyQuestion}>Load Easy</button>
      <h3 id="question"></h3>
      <div id="quizButtons">
        <button>

        </button>
        <button>

        </button>
        <button>

        </button>
        <button>

        </button>
      </div>
    </main>
  );
}

export default App;
