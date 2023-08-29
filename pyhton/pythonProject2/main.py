import requests

parmiters = {
    "amount":10,
    "type":"boolean",
}

responce = requests.get("https://opentdb.com/api.php",params=parmiters)
responce.raise_for_status()
data = responce.json()
print(data["results"])
