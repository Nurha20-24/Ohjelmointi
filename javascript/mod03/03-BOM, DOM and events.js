'use strict'

// haetaan viittaus johon solmuun (node) DOMissa
const h1Elem =document.querySelector('h1');
console.log(h1Elem);

// Muokataa DOMia
const title = h1Elem.textContent;
h1Elem.textContent = title + ' + lisäys otsikko';
h1Elem.style.fontSize = '22px';
h1Elem.classList.add('text')

//piilotetaan elementti css: avulla
h1Elem.classList.add('hidden')

//näytetään taas
h1Elem.classList.remove('hidden')

// ylemmän tason parent-elementin piilostus (koko body piilotus parentin kautta)
//h1Elem.parentElement.classList.add('hidden');

// lisätään sisältöä sivulle

const pElem= document.createElement('p')
document.querySelector('main').append(pElem);

pElem.textContent = 'Uusi kappale by JS!';

// haetaan viittaus useampaan elementtin/nodeen kerralla
const paragraphs= document.querySelectorAll('p');
//console.log(paragraphs)

paragraphs[2].textContent = 'Kolmas kappale.';

for (const p of paragraphs) {
  p.textContent = 'päivitetty!';
}



// Tehdään järjestetty lista jossa 5 alkiota
const listContents = ['kynä', 'kumi', 'reppu', 'pulpetti'];

// haetaan viittaus diviin id:n avulla
const listDiv = document.querySelector('#list');

// funktio jolla voi tulostaa taulukon sisällön ol-listaksi DOMiin
// ottaa paramatetrina taulukon, jonka alkioista lista luodaan
function renderList(items) {
  // tyhjennetää div ennen uuden ol-elementin lisäystä
  listDiv.innerHTML = '';
  const olElement = document.createElement('ol');
  for (let i = 0; i < items.length; i++) {
    const newLi = document.createElement('li');
    newLi.textContent = items[i];
    olElement.append(newLi);
}
listDiv.append(olElement);
}







//renderList(listContents);
//listContents.push('tietskari');



// BOM-rajapinta (window-olio)
// luetaan selaimen "sijainti" (URL)
window.console.log(window.location.href)
// siirrytään johonkin toiseen osoitteeseen
//window.location.href = 'https://www.google.fi';

const printButton = document.querySelector('#print');
printButton.addEventListener('click', function(event) {
  console.log('print & sort button clicked, event: ', event);
  listContents.sort()
  renderList(listContents);

// asioiden lisäys liställe

  const addButton = document.querySelector('#add');
  addButton.addEventListener('click', () => {
    const newItem = window.prompt('Lisää jotain listaan?')
    listContents.push(newItem);
    renderList(listContents);

  });

//Hiiritapahtumia
  document.addEventListener('mousemove', function(event) {
    document.querySelector('#output').textContent = `Hiiren
      osoittimen kooordinaatit: ${event.clientX}, ${event.clientY}`;
    // näytetään h1, kun hiiri menee riittävän alas dokumentilal
    if (event.clientY < 300) {
      h1Elem.classList.remove('hidden');
    }
  });
})

















