import requests


params = {
    "amount" : 10,
    "type" : "boolean"
}
URL = "https://opentdb.com/api.php"

question_resp = requests.get(URL, params=params)
question_resp.raise_for_status()

data_json = question_resp.json()
question_data = data_json['results']
# print(question_data)