import os
import requests
from datetime import datetime
import time

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 30

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

exercise_endpoint = os.environ.get("EXERCISE_ENDPOINT")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

sheety_username = os.environ.get("SHEETY_USERNAME")
sheety_password = os.environ.get("SHEETY_PASSWORD")


headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

params = {
    "query": input("What exercise you have done today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)
today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
now_time = today.strftime("%H:%M:%S")
exercises = result["exercises"][0]

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

# print(todays_workouts)

headers = {
    "Content-Type": "application/json",
}

sheety_reaponse = requests.post(
    url=sheety_endpoint,
    json=sheet_inputs,
    headers=headers,
    auth=(sheety_username, sheety_password),
)
sheety_result = sheety_reaponse.json()
print(sheety_result)
