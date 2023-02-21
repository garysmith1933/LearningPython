import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [facts, setFacts] = useState([])

  useEffect(() => {
    fetch("http://localhost:8080/data")
    .then(res => res.json())
    .then(
      data => {
        console.log(data.facts)
        setFacts(data.facts)
      }
    )
  },[])

  const data = facts.length === 0 ?
      <p>Loading...</p> 
:
    facts.map((fact, i) => {
    return <li key={i}> {fact} </li>
  })


  return (
    <div className="App">
     <h1>Heres a few random facts</h1>

     <ul>
      {data}
     </ul>
    </div>
  );
}

export default App;
