import requests
import json
import pyttsx3
import streamlit as st

def get_weather(city):
    api_key = "fc0e8e2302014754a7872400242504"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        temperature = weather_data["current"]["temp_c"]
        return temperature
    else:
        st.error("Failed to fetch weather data")
        return None

def speak_weather(city, temperature):
    engine = pyttsx3.init()
    engine.say(f'The weather in {city} is {temperature} degree Celsius')
    engine.runAndWait()

st.title("Weather Speaker")
st.write("Welcome to RoboSpeaker 2.1. Created by Gagan Sharma")

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if city:
        temperature = get_weather(city)
        if temperature is not None:
            st.success(f'The weather in {city} is {temperature} degree Celsius')
            speak_weather(city, temperature)
    else:
        st.warning("Please enter a city name")
