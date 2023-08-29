import requests
from datetime import datetime
# https://pixe.la/@shubham09
token= "s780fdsad6532dc783d"
username= "shubham09"
graph = "graphs1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# respons = requests.post(url=pixela_endpoint, json=user_params)
# print(respons.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graphs1",
    "name": "my frist graph",
    "unit": "km",
    "type":"float",
    "color":"ajisai"
}
header = {
    "X-USER-TOKEN":token
}

# responce = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(responce.text)
today = datetime(year=2022, month=7, day=30)
add_pxiel_end = f"{graph_endpoint}/{graph}"
add_pxiel = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"8.4"
}
# responce = requests.post(url=add_pxiel_end,json=add_pxiel, headers=header)
# print(responce.text)
update_end = f"{add_pxiel_end}/{today.strftime('%Y%m%d')}"
update_pxiel = {
    "quantity":"7.6"
}
responce = requests.put(url=update_end, json=update_pxiel, headers=header)
print(responce.text)