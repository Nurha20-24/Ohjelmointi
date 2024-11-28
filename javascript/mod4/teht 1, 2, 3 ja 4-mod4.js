'use strict'

document.querySelector('form').addEventListener('submit', function(evt){
    evt.preventDefault();

  const searchW =document.getElementById('query').value;
    console.log('Searching for:', searchW)
    getTvShows(searchW)
});

async function getTvShows(searchW) {
  const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchW}`)
  const data = await response.json();
  console.log('Api response', data)
  createArticle(data);
}

function createArticle(data){
  document.getElementById('results').innerHTML ="";

  for (const movie of data){
    console.log(movie.show.name);

    const article = document.createElement('article');

    const name = document.createElement('h2');
    name.innerText = movie.show.name;

    const link = document.createElement('a');
    link.innerText = movie.show.url
    link.href = movie.show.url
    link.target = "_blank";

    const img = document.createElement('img');
    img.alt = movie.show.name;
    img.src = movie.show.image ? movie.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';

    const summary = document.createElement('div');
    summary.innerHTML = movie.show.summary;

    article.appendChild(name);
    article.appendChild(link);
    article.appendChild(img);
    article.appendChild(summary);

    document.getElementById('results').appendChild(article);
  }
}

