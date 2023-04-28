import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    async function getData() {
      const response = await fetch("http://127.0.0.1:8000/api/questions");
      const data = await response.json();
      console.log({ data });
      setQuestions(data);
    }
    getData();
  }, []);

  return <>Hello world!</>;
}

export default App;
