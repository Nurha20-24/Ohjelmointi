'use strict';

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },

];

const createElement = document.createElement('select')

for (const student of students) {
  const optionElement = document.createElement('option')
  optionElement.value = student.id
  optionElement.name = student.name
  createElement.appendChild(optionElement);
}

document.getElementById('target').appendChild(createElement)
