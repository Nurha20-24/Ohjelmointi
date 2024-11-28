'use strict'

const element = document.querySelector('#target');

const li1 = document.createElement('li');
li1.textContent = 'First item';

const li2 = document.createElement('li');
li2.textcontent = `Second item`;
li2.classList.add('my-item');

const li3 = document.createElement('li');
li3.textContent = `Third item`;

element.appendChild(li1);
element.appendChild(li2);
element.appendChild(li3);





