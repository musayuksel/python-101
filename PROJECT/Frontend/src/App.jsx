import { useEffect, useState } from "react";
import "./App.css";
import Question from "./components/Question";
import { Link, Route, Routes } from "react-router-dom";

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
      <h1>Subject: {currentQuiz?.title}</h1>
      <h2>Total question: {currentQuiz.questions?.length}</h2>

      <Routes>
        <Route
          path="/"
          element={
            <button>
              <Link to="/quiz">Start</Link>
            </button>
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
                  setCurrentQuestionIndex(currentQuestionIndex + 1);
                }}
              >
                Next
              </button>
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
