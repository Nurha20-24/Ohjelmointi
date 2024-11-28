'use strict';
console.log('moro');

// taulukot eli arrays
const items = [1, 2, 3, 4, 5,{name: 'Ulla'},[3, 4, 5],'merkkijono'];
console.log(items);

// alkio viitataan ihan perus indeksillaa

console.log(items[0])
items[0] = 99;
console.log(items)
items[9] = 'Olen uusi jäsen';
console.log(items[6]);
console.log('Taulukon pituus: ', items.length)

// Taulukoiden läpikänti loopin avulla
console.log('---------------');
console.log('Perinteinen for-i looppi');

for (let i = 0; i < items.length; i++) {
  console.log(i, items[i])
}

console.log('------------');
console.log('Läpiäynti for/in rakenteella, joilla saadaan avain/indeksi ja ')
for (const index in items) {
  console.log(index, items[index])
}

console.log('-------------------');
console.log('Läpikäynti for/of rakenteella, jolla saadan arvot')
for (const item of items) {
  if (item != undefined) 
  console.log(item);
}
const names = ['Frank', 'Scott', 'Jasmine', 'Don' ];
const ages = [23, 28, 32, 101];

 for (let name of names) {
  console.log(`Name: ${name}`);
}
// järjestää aakkosjärjestykseen
names.sort();
console.log(names);
names.reverse();
console.log(names);

// ei toimi numeroiden kanssa sellaisenaan
ages.sort()
console.log(ages)

// tämä toimi numeroiden kanssa
ages.sort((a,b) => a-b);
console.log(ages)

ages.sort((a,b) => b - a);
console.log(ages)


// Lisätään nimi taulukkoon
names.push('Iines');

// palauttaa taulukon pituuden
const newLength = names.push('Ulla');
console.log(names)
console.log(names)
console.log('Taulukon pituus', newLength);

// Lisätään taulukon alkuun
names.unshift('Matti');
console.log(names) 

// Poistetaan taulukon vika ja otetaan muttujaan talteen
const lastName = names.pop();
console.log('Poistettiin: ', lastName)
console.log(names)

// Poistetaan taulukon eka ja otetaan muttujaan talteen
const firstName = names.shift();
console.log('Poistettiin: ', firstName);
console.log(names);

// etsitään onko taulukossa ko. arvo palutaa true/false
console.log(names.includes('Scott'));

// object literal eli olio
// samakaltainen kun pythonon sanakirja
const duck = {
  name: 'Aku',
  age: '313'
}

console.log(duck);
console.log(duck['age'])

//muutetaan arvoja
duck['age'] = 36
duck.name = 'Aku Ankka'
let moikkaus = `Moikkamoi ja tänne muuttuja ${duck.name}`;
let moikkaus2 = duck.name + ' on ' + duck.age + 'ikäinen ja motto: ' + duck.profession
console.log(duck);
console.log(moikkaus)
console.log(moikkaus)

// Lisätään uusia ominaisuuksia
duck.profession = 'working like a duck';
console.log(duck.profession);
console.log(duck);

// metodin luominen olioon ns. nimettömänä funktiona

const duck2 = {
  name: 'Iiines',
  age: 34,
  getInfo: function() {
    return this.name + ' on ' + this.age + '-vuotias';
  }
}
console.log(duck2.getInfo())

// JS funktioit

//perinteinen funktiomäärittely

function greet(name) {
  console.log(`Greet ${name}!!!!`)
  return
}
//funktion expression, Funktio joka on anonyymi mutta tallennetaan muuttujaan
const greet2 = function(name) {
  console.log(`Greetings again ${name}!!!`)
}
// arrow funktio / nuolifunktio, edellistä yksinkertaisempi ja lyhyempi
const greet3 = (name) => {
  console.log(`Greetings a third time ${name}!!!!`)
}
greet('Ulla');
greet2('Ulla')
greet3('Ulla')

const nimi = 'Matti';

function logName() {
  const nimi2 = 'Ulla'
  console.log(nimi);
  console.log(nimi2)
}



logName();








