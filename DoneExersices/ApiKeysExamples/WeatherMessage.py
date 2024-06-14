#!/usr/bin/python
from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

KEY = "3afd900ff7562bec5125ffc62dd69a57"
MY_LAT = 42.015350
MY_LON = -4.540560

OWM_ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast"

wheathet_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": KEY,
    "cnt": 0,
}

data = requests.get(url= OWM_ENDPOINT, params=wheathet_params)
data = data.json()

city = data["city"]["name"]
state = data["city"]["country"]

f_data = data["list"][0]
temp = f_data["main"]["temp"]
sens_temp = f_data["main"]["feels_like"]

temp = temp - 273,15
temp = int(temp[0])
sens_temp = sens_temp - 273,15
sens_temp = int(sens_temp[0])

date = f_data["dt_txt"]
date = date.split()[0]
condition = f_data["weather"][0]["main"]
descript_condition = f_data["weather"][0]["description"]

send = f"- {date}\nActual weather in {city}/{state}\n{temp}ºC, with a feeling of {sens_temp}ºC\n{condition} - {descript_condition.capitalize()}"

TWILIOID = os.getenv("TWILIOID")
TWILIO_KEY = os.getenv("TWILIOKEY")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

client = Client(TWILIOID, TWILIO_KEY)

message = client.messages.create(
    from_=f"{TWILIO_VIRTUAL_NUMBER}",
    body=send,
    to=f"{TWILIO_NUMBER}"
)

