'use strict'

const rlist = document.querySelector('.dlist');

function diceRoll() {
  const rolls = [];

  while (true) {
    const dice = Math.floor(Math.random() * 6) + 1;
    rolls.push(dice);

    let liElement = document.createElement('li')
    liElement.innerHTML = `Rolled: ${dice}`;
    rlist.appendChild(liElement);

    if (dice === 6) {
      break
    }

  }
  console.log("All roles:", rolls);
}

diceRoll()