#!/usr/bin/python

import requests


KEY = "3afd900ff7562bec5125ffc62dd69a57"


MY_LAT = 42.015350
MY_LON = -4.540560

OWM_ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast"

wheathet_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": KEY,
    "cnt": 4,
}


data = requests.get(url= OWM_ENDPOINT, params=wheathet_params)
f_data = data.json()

# status = f_data["list"][0]["weather"]
# print(status)

rain = False

for hour_data in f_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        rain = True
        

if rain:
    print("GET A UMBRELLA!")
else:
    print("NO UMBRELLA NECESARY")