'use strict';

// Exercise 1.

console.log("I'm printing to console!");





// Exercise 2.

let name = prompt('Please, type you name.');
document.querySelector('#target').innerHTML += `Hello, ${name} !<br><br>`;




// Exercise 3

let num1 = parseInt(prompt('Please, type first integer'));
let num2 =  parseInt(prompt('Please, type second integer'));
let num3 =  parseInt(prompt('Please, type third integer'));

let sum = num1 + num2 + num3;
let product = num1 * num2 * num3;
let average = sum / 3;

document.querySelector('#target').innerHTML +=
             `Sum = ${sum} <br>`+
             `Product = ${product} <br>`+
             `Average = ${average} <br><br>`;





// Exercise 4

const studentName = prompt('Enter your name');
const classRoom = Math.floor(Math.random()*6) +1;

let HogwartsSchool;

if (classRoom === 1) {
  HogwartsSchool = `${studentName}, you are in Ravenclaw.`
}
else if (classRoom === 2) {
 HogwartsSchool = `${studentName}, you are in Hufflepuff.`
}
else if (classRoom === 3) {
  HogwartsSchool = `${studentName}, you are in  Gryffindor.`
}
else if (classRoom === 4) {
  HogwartsSchool = `${studentName}, you are in Slytherin.`
}
else if (classRoom === 5) {
  HogwartsSchool=`${studentName}, you are in Ravenclaw.`
}
else if (classRoom === 6) {
  HogwartsSchool = `${studentName}, you are in Gryffindor.`
}
else {
  HogwartsSchool = 'Wrong typing';
}
document.querySelector('#target').innerHTML += `${HogwartsSchool}<br><br>`;





// Exercise 5

const year = prompt('Enter a year');
let leapYear;
if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
  leapYear = `${year} is a leap year`
} else {
  leapYear = `${year} is not a leap year`
}
document.querySelector('#target').innerHTML += `${leapYear}<br><br>`;





//Exercise 7

const throwCounts = [];
let totalSum = 0;
const diceRolls = parseInt(prompt('Enter a number for dice rolls'));

for (let i = 0; i < diceRolls; i++) {
  const randomNumber = Math.floor(Math.random() * 6) + 1;
  totalSum += randomNumber;
  throwCounts.push(randomNumber);
}
document.querySelector('#target').innerHTML += `Sum of the result is ${totalSum}<br><br>`;





















