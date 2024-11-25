'use strict'

const dlist = document.querySelector('.rlist');

function rollDice(sides) {
  const rolls = [];

  while (true) {
    const dice = Math.floor(Math.random() * sides) + 1;
    rolls.push(dice);

    let liElement = document.createElement('li')
    liElement.innerHTML = `Rolled: ${dice}`;
    dlist.appendChild(liElement);

    if (dice === sides) {
      break;
    }
  }
  console.log("All rolls:", rolls);
}
let sides = parseInt(prompt('Please enter the number of sides on the dice: '))

if (isNaN(sides) || sides <= 0) {
  alert('You entered invalid number. Please enter a valid number of sides greater than 0.')
} else {
  rollDice(sides)
}
