import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv



load_dotenv()


class DataManager:
    
    def __init__(self):
        self.sheety_end_point = os.environ['SHEETY_ENDPOINT']
        self._sheety_username = os.environ['SHEETY_USERNAME']
        self._sheety_password = os.environ['SHEETY_PASSWORD']
        self._authorization = HTTPBasicAuth(self._sheety_username, self._sheety_password)
        self.destination_data = {}


    def get_sheety_data(self):
        sheety_reaponse = requests.get(
            url=self.sheety_end_point,
            auth=(self._authorization),
        )
        data = sheety_reaponse.json()
        self.destination_data = data["prices"]

        return self.destination_data

# ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        resp = requests.put(
            url=f"{ os.environ['SHEETY_PRICES_ENDPOINT']}/{row_id}",
            json=new_data,
            auth=self._authorization
        )

        print(resp.json())