import requests
import json
import pyttsx3

city = input("Enter city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=fc0e8e2302014754a7872400242504&q={city}&aqi=no"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]['temp_c']

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.1. Created by Gagan Sharma")
    engine = pyttsx3.init()
    engine.say(f'The weather in {city} is {w} degree Celsius')
    engine.runAndWait()

