import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [facts, setFacts] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:8080/data")
    .then(res => res.json())
    .then(
      data => {
        setFacts(data.facts)
      }
    )
  },[])

  const [ fact1, fact2, fact3 ] = facts

  console.log(facts)
     //still have to handle when there is not facts
  return (
    <div className="App">
     <h1>Heres a few random facts</h1>

     <ul>
      <li>{fact1}</li>
      <li>{fact2}</li>
      <li>{fact3}</li>
     </ul>
    </div>
  );
}

export default App;
