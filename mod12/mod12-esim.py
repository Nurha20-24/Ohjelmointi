import requests

def search_show(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        #print(e)
        return

    if response.status.code != 200:
        print(f"HTTP-yhteysvirhe {response.status.code}")
        return

    response_body = response.json()
    print(response_body)
    if len(response_body) < 1:
        print("Ei tuloksia.")
        return

#Iteroidaan response body (http-vastauksen runko) silmukalla
    print("Kaikki Hakutulokset\n-------------")
    for item in response_body:
        print(item["show"] ["name"])
        print(f"{item['show']['type']}")
        print(f"TV-Ohjelma tyyppi: {item['show']['type']}")
        #for genre in item['show']['genres']:
           #print(genre)
search_show = (input("Anna TV-hakusana: "))

...
import json
import requests

city = 'Helsinki'
API_key = "0cae9a892ceb83c2a1c5990b762996a2"
kieli = '&units=metric&lang=FI'


def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=FI'
    #url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}{kieli}'
    #url = f"https://api.openweathermap.org/data/3.0/weather?&appid={API_key}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        #print(e)
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return
    print(json.dumps(response_body, indent=2))
    lämpötilä = response_body['main']['temp']
    print(f'Lämpötilä nyt helsingissä on {lämpötilä} asteina')
    kuvaus = response_body['weather'][0]['description']
    print(f" Sääkuvaus {kuvaus}")


get_weather()