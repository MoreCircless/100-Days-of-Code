import requests
import datetime



now = datetime.datetime.now()
date = now.strftime("%d/%m")
year = now.strftime("%y")

MY_LAT = 42.015350
MY_LON = -4.540560
LOCATION = "Europe/Madrid"

data = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LON}&tzid={LOCATION}")
f_data = data.json()

results = f_data["results"]
sunrise = results["sunrise"]
sunset = results["sunset"]
day_length = results["day_length"]
location = f_data["tzid"]

print(f"INFORMACION SOLAR del dia {date} de 20{year} \nCon el ajuste horario de: {location}\nSalida del sol: {sunrise}\nPuesta del sol: {sunset}\nCon una duracion total del dia de {day_length} horas")