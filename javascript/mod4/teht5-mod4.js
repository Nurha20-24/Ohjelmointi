'use strict'

async function getRandomJoke() {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');

    if (!response.ok) {
      throw new Error(response.statusText)
    }
    const joke = await response.json();
    console.log('Chuck Norris Joke: ', joke.value);

  } catch (error) {
    console.log(error);
  }
}

getRandomJoke();