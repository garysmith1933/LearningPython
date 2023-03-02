import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [questions, setQuestions] = useState([])
  const [current, setCurrent] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)

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

  const isCorrect = (element, choice, answer) => {
    const el = document.getElementById(`${element}`)

    if (choice === answer) {
      if (el.classList.contains("correct")) return
      
      el.classList.add("correct")
      setScore(score + 1)
    }
  
    else {
      el.classList.add("incorrect")
    }

    setAnswered(true)
  }

  const nextQuestion = () => {
    if (answered === false) return;

    const elements = document.getElementsByClassName('options')
    console.log(elements)

    Array.from(elements).forEach(el => {
      el.classList.remove("correct")
      el.classList.remove("incorrect")
    })

    setCurrent(current + 1)
    setAnswered(false)
  }


  const data = questions.length === 0 ?
      <p>Loading...</p> 
:
  current < 5 ?
    <div id='question-container'>
        <div className='questions'>
          <div className='options' id="option1" onClick={() => isCorrect("option1", questions[current][2], questions[current][5])}>{questions[current][2]}</div>
            <div className='options' id="option2" onClick={() => isCorrect("option2", questions[current][3], questions[current][5])}>{questions[current][3]}</div>
            <div className='options' id="option3" onClick={() => isCorrect("option3", questions[current][4], questions[current][5])}>{questions[current][4]}</div>
            <div className='options' id="option4" onClick={() => isCorrect("option4", questions[current][5], questions[current][5])}>{questions[current][5]}</div>
          </div>
          <button onClick={() => nextQuestion()}> Next </button>
        </div>
  : <p> Your final score is {score}/{questions.length}! Thanks for playing! </p>
  
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
