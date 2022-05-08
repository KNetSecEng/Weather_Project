import requests
import json


def wetter():
    api_key = "d81d9d72e6493efd45ca40c540b2bf34"
    city = input("Hallo! Bitte gib eine Stadt ein: ")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'    
    data = requests.get(url).json()
    temperatur = data['main']['temp']
    feuchtigkeit = data['main']['humidity'] 
    print("Hier in", city, "ist gerade",temperatur, "grad und die Feuchtigkeit betraegt:", feuchtigkeit,"fi")
   

wetter()

    