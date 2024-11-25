'use strict'

function askNumbers() {
  const numbers = [];

  while (true) {
  const number = parseInt(prompt('Please enter a number: (enter 0 to stop)'));

  if (number === 0) {
    break;
  }
  numbers.push(number)
  }
  numbers.sort((a, b) => b-a);
  console.log('Numbers from largest to smallest;', numbers);
}

askNumbers()