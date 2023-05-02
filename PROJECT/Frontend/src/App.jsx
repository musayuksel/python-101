import { useEffect, useState } from "react";
import "./App.css";
import Question from "./components/Question";
import { Link, Route, Routes, useNavigate } from "react-router-dom";
import andLogo from "./assets/and-logo.png";
import Dashboard from "./components/Dashboard";

// export const baseAPILink = "http://127.0.0.1:8000/api";
export const baseAPILink = "https://survey-demo-api.ew.r.appspot.com/api";
function App() {
  const [currentQuiz, setCurrentQuiz] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [correctAnsCounter, setCorrectAnsCounter] = useState(0);
  const [userName, setUserName] = useState({ name: "Musa Yuxel" });
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
        name: userName,
        score: correctAnsCounter,
      }),
    });
    if (response.status === 201) {
      alert("Your score is saved!");
      setCurrentQuestionIndex(0);
      setCorrectAnsCounter(0);
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
      <h2>
        Total question: {currentQuestionIndex} / {currentQuiz.questions?.length}
      </h2>
      <p>Correct answer: {correctAnsCounter}</p>

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
                isLastQuestion={
                  currentQuestionIndex === currentQuiz?.questions?.length - 1
                }
              />
              {currentQuestionIndex === currentQuiz?.questions?.length - 1 && (
                <section className="submit-container">
                  <input
                    onChange={(e) => setUserName(e.target.value)}
                    type="text"
                    placeholder="full name"
                  />

                  <button onClick={handleSubmit}>Submit</button>
                </section>
              )}
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
