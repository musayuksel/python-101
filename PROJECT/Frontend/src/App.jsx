import "./App.css";

function App() {
  async function getData() {
    const response = await fetch("http://localhost:8000/");
    const data = await response.json();
    console.log(data);
  }

  getData();

  return <>Hello world!</>;
}

export default App;
