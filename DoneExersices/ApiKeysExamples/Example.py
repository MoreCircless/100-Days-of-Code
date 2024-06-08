#!/usr/bin/python

import requests


KEY = "3afd900ff7562bec5125ffc62dd69a57"


MY_LAT = 42.015350
MY_LON = -4.540560

ex_rq = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LON}&appid={KEY}"


data = requests.get(url=ex_rq)
f_data = data.json()
print(f_data)

