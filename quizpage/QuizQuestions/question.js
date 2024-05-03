
const startingMinutes = 1;
let time = startingMinutes * 60;

const countdown = document.getElementById("countdown") 

setInterval(updatecount, 1000)

function updatecount (){
  const minutes = Math.floor(time / 60);
  let second = time % 60;

  countdown.innerHTML = `${minutes}:${second}`;
  time--;
  if(countdown.innerHTML == "-1:-1" ){
    clearInterval(countdown)
    alertsc.style.display = "block"
        htmlcard.style.display = "none"

        alertsc.innerHTML=(`You've scored ${score} / ${quizData.length} <br /> <a href="main.html">Go Back </a>`);
        window.localStorage.setItem("html",`${score} / ${quizData.length} `)
  }
}





  // document.documentElement.requestFullscreen()
  // .then(() => console.log('ful screen activated'))
  // .catch(() => console.log("err" = "error"))




const quizData = [
    {
      question: "What does the len() function in Python do?",
      a: "Returns the number of items in a list",
      b: "Returns the length of a string",
      c: "Returns the size of a file",
      d: "Returns the memory usage of an object",
      correct: "a",
    },
    {
      question: "Which of the following data types is immutable in Python?",
      a: "List",
      b: "Dictionary",
      c: "Tuple",
      d: "Set",
      correct: "c",
    },
    {
      question: "What does the continue keyword do in a loop?",
      a: "Terminates the loop",
      b: "Skips the rest of the code inside the loop for the current iteration and continues with the next iteration",
      c: "Breaks the loop",
      d: "Restarts the loop from the beginning",
      correct: "b",
    },
    {
      question: "Which method is used to add an element to the end of a list in Python?",
      a: "append()",
      b: "extend()",
      c: "add()",
      d: "insert()",
      correct: "a",
    },
    {
      question: "What is the purpose of the __init__ method in Python classes?",
      a: "To initialize the class variables",
      b: "To define the constructor of the class",
      c: "To destroy an object",
      d: "To return the string representation of an object",
      correct: "b",
    },
  ];
  
  const answerEls = document.querySelectorAll(".answer");
  const aText = document.getElementById("aText");
  const bText = document.getElementById("bText");
  const cText = document.getElementById("cText");
  const dText = document.getElementById("dText");
  const questionEl = document.getElementById("question");
  const submitBtn = document.getElementById("submit");
  
  let currentQuiz = 0;
  let score = 0;
  
  quizLoad();
  
  function quizLoad() {
    deSelectInput();
  
    const currentQuizData = quizData[currentQuiz];
  
    questionEl.innerText = currentQuizData.question;
    aText.innerText = currentQuizData.a;
    bText.innerText = currentQuizData.b;
    cText.innerText = currentQuizData.c;
    dText.innerText = currentQuizData.d;
  }
  
  function getSelection() {
    let answer = undefined;
  
    answerEls.forEach((answerEl) => {
      if (answerEl.checked) {
        answer = answerEl.id;
      }
    });
    return answer;
  }
  
  function deSelectInput() {
    answerEls.forEach((answer) => {
      answer.checked = false;
    });
  }
  
var alertsc = document.getElementById('alertsc')
var htmlcard = document.getElementById('htmlcard')

  submitBtn.addEventListener("click", () => {
    
    const answer = getSelection();
    alertsc.innerHTML=(` You've scored ${score} / ${quizData.length} <br /> <a href="../QuizHome.html">Go Back </a>`)
    window.localStorage.setItem("html",`${score} / ${quizData.length} `)
  
    if (answer) {
      if (answer === quizData[currentQuiz].correct) {
        score++;
      }
  
      currentQuiz++;
  
      if (currentQuiz < quizData.length) {
        quizLoad();
      } else {
        alertsc.style.display = "block"
        htmlcard.style.display = "none"
       
      
      }
    }
     
  });
  

  



