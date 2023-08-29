import requests
MY_LAT = 19.075983
MY_LNG = 72.877655
#responce = requests.get(url="http://api.open-notify.org/iss-now.json")
#responce.raise_for_status()
#data = responce.json()
#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]
#iss_position = (longitude, latitude)
#print(iss_position)

parmiters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
}

responce = requests.get("https://api.sunrise-sunset.org/json",)
responce.raise_for_status()
