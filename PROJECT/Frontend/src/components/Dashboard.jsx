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
    <ul>
      {currentQuizScores.map((user) => (
        <li key={user.id}>
          <p>Name: {user.name}</p>
          <p>Score: {user.score}</p>
        </li>
      ))}
    </ul>
  );
}
