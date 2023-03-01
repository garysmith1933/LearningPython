import './App.css';
import { useState, useEffect } from 'react';

const isCorrect = (element, choice, answer) => {
  const el = document.getElementById(`${element}`)
  console.log(choice, answer)
  if (choice === answer) {
    el.classList.add("correct")
  }

  else {
    el.classList.add("incorrect")
  }
}

function App() {
  const [questions, setQuestions] = useState([])
  const [current, setCurrent] = useState(0)
  const answer = 0
  let id, title, option1, option2, option3, option4


  useEffect(() => {
    fetch("http://localhost:8080/data")
    .then(res => res.json())
    .then(
      data => {
        console.log(data)
        setQuestions(data)
        option1 = questions[current][2]
      }
    )
  },[])


  const data = questions.length === 0 ?
      <p>Loading...</p> 
:
    <div id='question-container'>
      <h3 className='question-title'>{title}</h3>
        <div className='questions'>
          <div className='options' id="option1" onClick={() => isCorrect("option1", option1, answer)}>{questions[current][2]}</div>
            <div className='options' id="option2" onClick={() => isCorrect("option2", option2, answer)}>{questions[current][3]}</div>
            <div className='options' id="option3" onClick={() => isCorrect("option3", option3, answer)}>{questions[current][4]}</div>
            <div className='options' id="option4" onClick={() => isCorrect("option4", option4, answer)}>{questions[current][5]}</div>
          </div>
        </div>
  
  return (
    <div className="App">
     <h1>Think you know me?</h1>
     <h4>Try out this quiz and see how you do!</h4>
     <ul>
      {data}
      <button onClick={() => setCurrent(current + 1)}> Next </button>
     </ul>
    </div>
  );
}

export default App;
