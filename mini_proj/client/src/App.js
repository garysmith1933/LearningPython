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
  const [score, setScore] = useState(0)

  useEffect(() => {
    fetch("http://localhost:8080/data")
    .then(res => res.json())
    .then(
      data => {
        console.log(data)
        setQuestions(data)
      }
    )
  },[])

  const nextQuestion = () => {
    setCurrent(current + 1)
    const elements = document.getElementsByClassName('options')
    console.log(elements)

    Array.from(elements).forEach(el => {
      el.classList.remove("correct")
      el.classList.remove("incorrect")
    })
  }


  const data = questions.length === 0 ?
      <p>Loading...</p> 
:
    <div id='question-container'>
        <div className='questions'>
          <div className='options' id="option1" onClick={() => isCorrect("option1", questions[current][2], questions[current][5])}>{questions[current][2]}</div>
            <div className='options' id="option2" onClick={() => isCorrect("option2", questions[current][3], questions[current][5])}>{questions[current][3]}</div>
            <div className='options' id="option3" onClick={() => isCorrect("option3", questions[current][4], questions[current][5])}>{questions[current][4]}</div>
            <div className='options' id="option4" onClick={() => isCorrect("option4", questions[current][5], questions[current][5])}>{questions[current][5]}</div>
          </div>
        </div>
  
  return (
    <div className="App">
     <h1>Think you know me?</h1>
     <h4>Try out this quiz and see how you do!</h4>
     {current < 4 ?
      <ul>
          {data}
          {console.log(current)}
          <button onClick={() => nextQuestion()}> Next </button>
        </ul>
        : 'game over' } 
    
    </div>
  );
}

export default App;
