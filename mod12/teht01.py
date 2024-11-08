# Tehtävä 1
import requests

url = 'https://api.chucknorris.io/jokes/random'
vastaus =requests.get(url).json()

print(vastaus["value"])