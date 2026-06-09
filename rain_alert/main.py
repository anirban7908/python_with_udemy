import requests
from twilio.rest import Client
import os
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
weather_url = "https://api.openweathermap.org/data/2.5/forecast"
# lat = 22.5726459
# lon = 88.3638953
lat = 27.235901
lon = 94.104599

params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "cnt": 4
}

weather_api_request = requests.get(url=weather_url, params=params)
weather_api_request.raise_for_status()

weather_data = weather_api_request.json()
weather_list = weather_data['list']

report = "The weather will be fine today"
will_it_rain = False
for weather in weather_list:
    if weather['weather'][0]["id"] < 700:
        will_it_rain = True
        report = "It's going to rain today. Remember to bring an umbrella!☔ "
if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= report,
        from_="+15054085683",
        to="+917908000130",
    )
    print(message.status)
        
