import { useEffect, useState } from "react";
import "./App.css";
import Question from "./components/Question";
import { Link, Route, Routes } from "react-router-dom";
import andLogo from "./assets/and-logo.png";
function App() {
  const [currentQuiz, setCurrentQuiz] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

  useEffect(() => {
    async function getData() {
      const response = await fetch("http://127.0.0.1:8000/api/current_quiz");
      const data = await response.json();
      setCurrentQuiz(data.current_quiz);
    }
    getData();
  }, []);

  return (
    <>
      <header>
        <Link to="/" className="logo_link">
          <img
            src={andLogo}
            alt="Page logo with letter M & Y"
            className="logo_img"
          />
        </Link>
        <nav>
          <Link className="dashboard-link" to="/">
            Dashboard
          </Link>
        </nav>
      </header>
      <h1>Subject: {currentQuiz?.title}</h1>
      <h2>Total question: {currentQuiz.questions?.length}</h2>

      <Routes>
        <Route
          path="/"
          element={
            <Link to="/quiz">
              <button>Start</button>
            </Link>
          }
        />
        <Route
          path="/quiz"
          element={
            <>
              <Question
                question={currentQuiz?.questions?.[currentQuestionIndex]}
              />
              <button
                onClick={() => {
                  setCurrentQuestionIndex(currentQuestionIndex - 1);
                }}
              >
                Prev
              </button>
              <button
                onClick={() => {
                  setCurrentQuestionIndex(currentQuestionIndex + 1);
                }}
              >
                Next
              </button>
              {currentQuestionIndex === currentQuiz?.questions?.length - 1 && (
                <button>Submit</button>
              )}
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
