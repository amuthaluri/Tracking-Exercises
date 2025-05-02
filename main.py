import os
import requests
from datetime import datetime

GENDER = "YOUR GENDER"
WEIGHT_KG =" YOUR WEIGHT"
AGE = "YOUR AGE"
HEIGHT_CM = "YOUR HEIGHT"
BASIC_USERNAME = "amuthaluri"
BASIC_PASSWORD = "sasha@1234567"

APP_ID = "16cca952"
API_KEY = "3283d972d9db04180182bf840188a789"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Exercise_param = {
# "query":input("Tell me which exercise you did :")
# }
exercise_text = input("Tell me which exercise you did? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
"weight_kg": 64,
"height_cm": 100,
"age": 25,
"gender": GENDER
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

result = response.json()
print(result)

sheet_endpoint = "https://api.sheety.co/6f3f1d7d2037bdb6ca86fa889e9ef043/copyOfMyWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(
            f'{BASIC_USERNAME}',
            f'{BASIC_PASSWORD}',
        ))
    print(sheet_response.text)

