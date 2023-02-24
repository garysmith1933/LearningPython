import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [facts, setFacts] = useState([])

  useEffect(() => {
    fetch("http://localhost:8080/data")
    .then(res => res.json())
    .then(
      data => {
        console.log(data)
        setFacts(data)
      }
    )
  },[])

  const data = facts.length === 0 ?
      <p>Loading...</p> 
:
    facts.map((fact) => {
    const [idx, text] = fact
    return <li key={idx}> {text} </li>
  })


  return (
    <div className="App">
     <h1>Think you know me?</h1>
     <h4>Try out this quiz and see how you do!</h4>
     <ul>
      {data}
     </ul>
    </div>
  );
}

export default App;
