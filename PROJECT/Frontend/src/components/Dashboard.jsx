import { useEffect, useState } from "react";
import { baseAPILink } from "../App";

export default function Dashboard() {
  const [currentQuizScores, setCurrentQuizScores] = useState([]);

  useEffect(() => {
    async function getScores() {
      const response = await fetch(`${baseAPILink}/user_scores`);
      const data = await response.json();
      setCurrentQuizScores(data.user_scores);
    }
    getScores();
  }, []);

  return (
    <ul className="dashboard-container">
      <li style={{ fontWeight: "bold" }}>
        <p>NAME</p>
        <p>SCORE</p>
      </li>
      {currentQuizScores.map((user) => (
        <li key={`${user.name}-${user.score}`}>
          <p>{user.name}</p>
          <p>{user.score}</p>
        </li>
      ))}
    </ul>
  );
}
