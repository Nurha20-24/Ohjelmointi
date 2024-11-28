/*
const button = document.querySelector("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}
function changeBackground() {
   document.body.style.backgroundColor = `rgb(${random(250)} ${random(250)} ${random(250)} )`;

}
button.addEventListener("click", changeBackground)

button.removeEventListener("click", changeBackground)

//addEventListener(type, listener)

//myElement.addEventListener("click", functionA);




const form = document.querySelector("form");
const fname = document.querySelector("#firstname");
const lname = document.querySelector("#lastname");
const para = document.querySelector("p");

form.addEventListener("submit", (e) => {
  if (fname.value === "" || lname.value === "") {
    e.preventDefault();
    para.textContent = "You need to fill in both names!";
  }
})


 *

const button = document.querySelector('button');
//button.addEventListener('click', function(evt) {
function popup (evt) {
  alert('element ' + evt.currentTarget.tagName + ' was clicked');
}
//button.onclick = popup;
button.addEventListener('click', popup)




const button = document.querySelector('button');

function A () {
  alert('This is function A');
  button.removeEventListener('click', A);
  button.addEventListener('click', B);
}
function B() {
  alert('this is function B');
}

button.addEventListener('click', A);



//select the elements
const form = document.querySelector('form');
const fname = document.querySelector('input[name=fName]');
const lname = document.querySelector('input[name=lName]')
const p = document.querySelector('p');

//when the form is submitted
form.addEventListener('submit', function(evt) {
//...prevent the default action.
  evt.preventDefault();
  p.innerText = `Your name is ${fname.value} ${lname.value}`
});

 */
