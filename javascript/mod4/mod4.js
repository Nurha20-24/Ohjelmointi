/*

console.log('script start');

// hakee pics.json-tiedoston samalta palvelmilta, millä tämä js-tiedosto on
// käsittelee taulukkodatan ja tekee kuva-elementit DOMiin

async function fetchImages() {
  const response = await fetch('pics.json');
  console.log('pic response', response);
  if (response.ok) {
     const pics = await response.json();
     console.log('kuvat:', pics)
     for (const pic of pics) {
       const imgElem= document.createElement('img')
       imgElem.src = pic.address;
       imgElem.alt = pic.description
       document.querySelector('#images').append(imgElem);
    }
  }

}
fetchImages();



// Chuck norris api esimerkki
async function getAJoke() {
  const outputElem = document.querySelector('#joke');

  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    console.log('joke response', response);
    if (!response.ok) {
      // status koodi jotain muuta kuin ok (ei 2xx)
      throw new Error(response.statusText)
    }
    const joke = await response.json();
    console.log('vitsi:', joke.value);
    outputElem.textContent = joke.value;

  } catch (error) {
    console.log(error);
    outputElem.textContent = 'Vitsin haku epäonnistui';
  }
}
// haetaan vitsi vain käyttäjän pyynnöstä
document.querySelector('#get-joke')
    .addEventListener('click', getAJoke)



// Esimerkki oman flask-serverin käytöstä
function fetchAirport(icao) {

  const response =  await fetch('http://localhost:5000/airport/' + icao);
  const airport = await response.json();
  console.log('airport data', airport)

  return airport
}

//fetchAirport(efhk)
const form = document.querySelector('#airport-form')
form.addEventListener('submit', async function (event) {
  event.preventDefault();
  // haetaan viittaus input-elementtii ja sen arvo (käyttäjän syöte)
  const userInput = form.querySelector('input').value;
  const airport = fetchAirport(userInput);
  console.log(airport)
});


console.log('script end');




 */
