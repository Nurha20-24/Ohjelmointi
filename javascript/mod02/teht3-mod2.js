'use strict'

const nlist = document.querySelector('.doglist');

const num = 6;
const names = [];

function askNames() {
  for (let i = 0; i < num; i++) {
    let name = prompt(`Please enter dog ${i + 1} name: `);
    names.push(name);
  }
    names.reverse();
}

function printNames() {
  for (let name of names) {
    let liElement = document.createElement('li');
    liElement.innerHTML = name;
    nlist.appendChild(liElement);
  }
}

askNames();
printNames();