import './css/App.css';
import './css/Questions.css'
import './css/Mobile.css'
import { useState, useEffect } from 'react';


const judgeScore = (score) => {
  const scores = {
    0: '0/5...uhhh how did you get 0, there is literally 5 questions with 4 options each and somehow you guessed wrong EVERY SINGLE TIME!? HOWWWWW!?!?',
    1: '1/5 Hey you got 1...NOW GO GET MORE!', 
    2: '2/5 Meh, you can do better.',
    3: '3/5 You got more right than you did wrong! Not bad, but not great either!',
    4: '4/5 Off by one, but 4 is pretty dang good',
    5: '5/5 You got them all right!! You"re not stalking me are you?'
  }

  return scores[score]
}

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

      if (answered === false) {
        setScore(score + 1)
      }
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
      <div className='header'>
        <h1>Think you know me?</h1>
        <h4>Try out this quiz and see how you do!</h4>
      </div>

        <div className='questions'>
          <div className='options' id="option1" onClick={() => isCorrect("option1", questions[current][2], questions[current][5])}>{questions[current][2]}</div>
            <div className='options' id="option2" onClick={() => isCorrect("option2", questions[current][3], questions[current][5])}>{questions[current][3]}</div>
            <div className='options' id="option3" onClick={() => isCorrect("option3", questions[current][4], questions[current][5])}>{questions[current][4]}</div>
            <div className='options' id="option4" onClick={() => isCorrect("option4", questions[current][5], questions[current][5])}>{questions[current][5]}</div>
          </div>
          
          <button id='next' onClick={() => nextQuestion()}> Next </button>
        </div>
  : <div id='question-container'>
      <p>{judgeScore(score)}</p>
      <p>Thanks for playing!</p>
    </div>
    
  
  return (
    <div className="App">
        {data}
    </div>
  );
}

export default App;
