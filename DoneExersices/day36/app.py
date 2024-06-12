import requests
from datetime import time, datetime

exercise_text = input("What exercise do you have done?")
# GENDER = 
# WEIGHT_KG = 
# HEIGHT_CM = 
AGE = 22

KEYID = "8d288191"
KEYNUTRITION = "151504f809ba41cbdf6ed43bf4b014fe"
HOSTNUTRITION = "https://trackapi.nutritionix.com"
NATURALENDPOINT = "/v2/natural/exercise"

nutrition_header = {
    "x-app-id": KEYID,
    "x-app-key":  KEYNUTRITION,
}

inputs = {
    "query": exercise_text,
    # "gender": GENDER,
    # "weight_kg": WEIGHT_KG,
    # "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=f"{HOSTNUTRITION}{NATURALENDPOINT}",json=inputs, headers=nutrition_header )
print(f"{HOSTNUTRITION}{NATURALENDPOINT}")
result = response.json()
print(result)

exercise = result["exercises"][0]["name"]
calories = result["exercises"][0]["nf_calories"]
duration = result["exercises"][0]["duration_min"]

sheetyendpoint = "https://api.sheety.co/69a2bf64984654c01496c348a088ac7b/copiaDeMyWorkouts/workouts"

day = datetime.now().strftime("%d/%m/%y")
hour = datetime.now().strftime("%H:%M")

postcontent = {
    "workout": {
        "date": day,
        "time": hour,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

postquery = requests.post(url=sheetyendpoint, json=postcontent)












