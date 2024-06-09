import requests 
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "morecircless"
TOKEN = "dedededede"


user_params = {
    "token": "dedededede",
    "username": "morecircless",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# * Create User
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
# * Create Graph
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_config = {
#     "id": "grafico1",
#     "name": "Study Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color":"ajisai",
# }

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
date = datetime.now()
date = date.strftime("%Y%m%d")

GRAPH_ID = "grafico1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_request ={
    "date": date,
    "quantity": "4.0",
}

# * POST A PIXEL
# response = requests.post(url=GRAPH_ENDPOINT,json=pixel_request, headers=headers)
# print(response.text)

# # * UPDATE PIXEL
# response = requests.put(url=f"{GRAPH_ENDPOINT}/{date}", json=pixel_request, headers=headers)
# print(response.text)

# * DELETE PIXEL 
url = f"/{USERNAME}/graphs/{GRAPH_ID}/{date}"

response = requests.delete(url=f"{PIXELA_ENDPOINT}{url}", headers=headers)
print(response.text)