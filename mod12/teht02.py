# Tehtävä 2
import requests
import json
city_name = input("Mikä on kaupunkisi nimi?: ")
API_key = "0cae9a892ceb83c2a1c5990b762996a2"
lampotila_celsius = '&units=metric&lang=FI'

def get_weather ():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=FI'

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("HTTP ei toimi")
            return
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe")
        return

    json_response = response.json()
    lampotila =json_response['main']['temp']
    saa_kuvaus = json_response['weather'][0]['description']
    print(f"({city_name}) kaupungin lämpötilä on {lampotila} celsiusastetta ja {saa_kuvaus}.")

get_weather()
