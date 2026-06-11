import requests

APP_ID = ""
API_KEY = ""
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 30

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("What exercise you have done today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)
