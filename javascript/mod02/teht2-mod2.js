'use strict'
//Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants.
// Finally, the program prints the names of the participants on the
// web page in an ordered list (<ol>) in alphabetical order. (


const nlist = document.querySelector('.namelist');

const num = parseInt(prompt('Please enter a number of participants: '))
const names = [];

function askNames() {
  for (let i = 0; i < num; i++) {
    let name = prompt('Please enter a name');
    names.push(name);
  }
}

function printNames () {
  for (let name of names) {
    let liElement = document.createElement('li');
    liElement.innerHTML = name;
    nlist.appendChild(liElement);
  }
}

askNames()
printNames()
























