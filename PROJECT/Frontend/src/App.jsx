import { useEffect, useState } from "react";
import "./App.css";
import Question from "./components/Question";
import { Link, Route, Routes, useNavigate } from "react-router-dom";
import andLogo from "./assets/and-logo.png";
import Dashboard from "./components/Dashboard";

export const baseAPILink = "http://127.0.0.1:8000/api";
function App() {
  const [currentQuiz, setCurrentQuiz] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [correctAnsCounter, setCorrectAnsCounter] = useState(0);

  const navigate = useNavigate();
  useEffect(() => {
    async function getData() {
      const response = await fetch(`${baseAPILink}/current_quiz`);
      const data = await response.json();
      setCurrentQuiz(data.current_quiz);
    }
    getData();
  }, []);

  async function handleSubmit() {
    const response = await fetch(`${baseAPILink}/user_scores`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "Musa Yuxel",
        score: correctAnsCounter,
      }),
    });
    if (response.status === 201) {
      alert("Your score is saved!");
      navigate("/");
    }
  }

  return (
    <>
      <header>
        <Link to="/" className="logo_link">
          <img src={andLogo} alt="and-logo" className="logo_img" />
        </Link>
        <nav>
          <Link className="dashboard-link" to="/">
            Dashboard
          </Link>
        </nav>
      </header>
      <h1>Subject: {currentQuiz?.title}</h1>
      <h2>Total question: {currentQuiz.questions?.length}</h2>
      <h2>Correct answer: {correctAnsCounter}</h2>

      <Routes>
        <Route
          path="/"
          element={
            <>
              <Dashboard />
              <Link to="/quiz">
                <button>Start</button>
              </Link>
            </>
          }
        />
        <Route
          path="/quiz"
          element={
            <>
              <Question
                question={currentQuiz?.questions?.[currentQuestionIndex]}
                setCurrentQuestionIndex={setCurrentQuestionIndex}
                setCorrectAnsCounter={setCorrectAnsCounter}
              />
              <button
                onClick={() => {
                  setCurrentQuestionIndex(currentQuestionIndex - 1);
                }}
              >
                Prev
              </button>
              {currentQuestionIndex === currentQuiz?.questions?.length - 1 && (
                <button onClick={handleSubmit}>Submit</button>
              )}
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
