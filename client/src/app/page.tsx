"use client"
import React from 'react'
import { useState, useEffect } from 'react'


function page() {
  const [message, setMessage] = useState('')
 
  function askQuestion(query: string) {
    const bodyParams = JSON.stringify({ question: query})
    console.log(bodyParams)
    fetch('http://127.0.0.1:5000/chat/', { 
      method: "POST",
      body: bodyParams,
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((res) => res.json())
    .then(data => {
      setMessage(data.answer)
    })
  }
  useEffect(()=> {
    fetch('http://127.0.0.1:5000/')
    .then((res) => res.json())
    .then(data => {
      setMessage(data.message)
    })
  }, [])

  return (
    <div className='mx-10'>
      <div className='flex flex-col h-full justify-center align-center bg-slate-100'>
        <h2>Fale com o chatty por aqui:</h2>
        <textarea name="question" id="query"></textarea>
        <button
        className='bg-slate-300 my-10 w-1/4'
        onClick={() => { 
          const textarea = document.getElementById('query') as HTMLTextAreaElement
          askQuestion(textarea.value)
        }
        }>Perguntar</button>
      </div>

      <div className=' w-full h-full mt-20'>
        <p>{message ? message : 'Digitando ...'}</p>
      </div>
    </div>
  )
}

export default page