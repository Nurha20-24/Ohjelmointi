'use strict';
//Open t3 folder in your IDE/editor. Add HTML by using innerHTML property. (2p)
// Add the following HTML code to the element with id="target".
// Add the values from 'names' array to the <li> elements in a for-loop.
// <li>John</li>
// <li>Paul</li>
// <li>Jones</li>
const names = ['John', 'Paul', 'Jones'];

const targetElement = document.querySelector('#target')

for (let name of names) {
  targetElement.innerHTML += `<li>${name}</li>`


}