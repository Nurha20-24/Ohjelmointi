'use strict'

document.querySelector('#jokeForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const searchQ = document.querySelector('input[name=q]').value
  searchJokes(searchQ)
})
async function searchJokes(query) {
  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
    if (!response.ok) throw new Error('Invalid input!');

    const dataa = await response.json();
    const jokes = dataa.result;

    const container = document.getElementById('container');
    container.innerHTML = '';

    for (const joke of jokes) {
      const article = document.createElement('article');
      const p = document.createElement('p');
      p.innerText = joke.value;
      article.appendChild(p);
      container.appendChild(article);
    }

  } catch (e) {
    console.log('error', e)
  }
}



