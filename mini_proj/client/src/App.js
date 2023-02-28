import './App.css';
import { useState, useEffect } from 'react';

const isCorrect = (choice, answer) => {
  if (choice === answer) {
    console.log("correct")
  }

  else {
    console.log('WRONG')
  }
}

function App() {
  const [questions, setQuestions] = useState([])

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

  const data = questions.length === 0 ?
      <p>Loading...</p> 
:
    questions.map((question) => {
    const [idx, title, option1, option2, option3, answer] = question
    // return <li key={idx}> {title} </li>
    return <div key={idx} id='question-container'>
              <h3 className='question-title'>{title}</h3>
              <div className='questions'>
                  <div className='options' onClick={() => isCorrect(option1, answer)}>{option1}</div>
              
                <div className='options'>{option2}</div>
                <div className='options'>{option3}</div>
                <div className='options'>{answer}</div>
              </div>
          </div>
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
