import requests
from datetime import datetime
USERNAME = "anirbanchoudhury"
TOKEN = "klfhdsoifhwofh"
# Creating an user to pixela
pixela_endpoint = "https://pixe.la/v1/users"
HEADERS = {"X-USER-TOKEN": TOKEN}
GRAPH_ID = "graph1"
user_prams = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# creating an user. run the code once only.
# response = requests.post(url=pixela_endpoint, json=user_prams)
# print(response.text)


# creating a graph.
# pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Hour",
#     "type": "float",
#     "color": "shibafu",
# }
# headers = {"X-USER-TOKEN": TOKEN}

# graph_response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)


# Post a pixel in graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# today = datetime(year=2026, month=6, day=10)

# Static data
# pixel_params = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"6.5",
#     "optionalData":'{"message":"Completed the pixela graph!"}'
# }

# quantity via input
pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How may hour have you done coding today?"),
    "optionalData":'{"message":"Completed the pixela graph!"}'
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HEADERS)

print(pixel_response.text)