'use strict';
/*
Moduuli 1: koodeja
 */
const randomNumber = Math.random()
//const randomNumber = 0.503
console.log('arvottuo numero', randomNumber)

// ehtolause, ehdon täytyy olla aina true/false
// 49,9 % todennäköisyys kruuna/klaava
if (randomNumber < 0.495) {
    console.log("kruuna")
} else if (randomNumber > 0.505) {
    console.log("klaava")
} else {
    console.log("kolikko jää kantilleen")
}

 console.log("Suoritus jatkuu ehtolauseen jälkeen")
// arvotaan testin


const cabinClass = prompt("Enter the cabin class (A/B/C).");
switch (cabinClass) {
            case 'A':
                console.log('Top deck cabin with window.');
                break;
                case 'B':
                console.log('Top deck cabin without window.');
                break;
            case 'C':
                console.log('Windowless cabin under the car deck.');
                break;
            default:
                console.log("Invalid cabin class.");
}
// Toistorakenteet eli silmukat eli loopit
// 49,9 % todennäköisyys kruuna/klaava
// kuinka monta heitto menee, että kolikko jää kyljelleen.


for (let i = 0; i <= 100; i++) {
  let throwCount = 0
  let stillThrowing = true;
  while (stillThrowing);
  const randomNumber = Math.random()
  throwCount++;

if (randomNumber < 0.495) {
    console.log("kruuna")
} else if (randomNumber > 0.505) {
    console.log("klaava")
} else {
  console.log("kolikko jää kantilleen")
  console.log("heittojen lkm", throwCount);
  throwCounts.push(throwcount);
  stillThrowing = false;
}

}
console.log("heittojen lukumäärät", throwcounts);

//lasketaan heittomäärien ka for-silmukalla
let sum = 0;
for(let i= 0; i<throwCounts.length; i++) {
  sum = sum + throwCounts[i];
}
console.log("heittjen ka:", summa / throwCounts.length)