import os
import json
from  dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._serp_api_key = os.environ['SERPAPI_API_KEY']
        self.serp_endpoint = os.environ['SERPAPI_ENDPOINT']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "INR",
            "api_key": self._serp_api_key,
        }

        response = requests.get(url=self.serp_endpoint, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        # with open("api_response.json", "w", encoding="utf-8") as json_file:
        #     json.dump(data, json_file, indent=4, ensure_ascii=False)
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data