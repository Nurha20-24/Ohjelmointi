'use strict'
//Write a program that prompts the user for numbers.
// When the user enters one of the numbers he previously entered,
// the program will announce that the number has already been given
// and stops its operation and then prints all the given numbers to the
// console in ascending order.

function askNumbers() {
 const numbers = [];
  while (true) {

    const number = parseInt(prompt('Please enter a number: '))
    if (numbers.includes(number)) {
      console.log(`The number ${number} has already given`)
      break;
    }
    numbers.push(number)
  }
  numbers.sort((a,b) => a - b);
  console.log('All the numbers in ascending order:', numbers)
}
askNumbers()