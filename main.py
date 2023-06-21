import requests
from datetime import datetime

USERNAME = "shaahin"
TOKEN = "87Vu[P13z/hJXJ\z"

today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",

}

# response = requests.delete(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

print(pixel_config['date'])