import requests
import os
from twilio.rest import Client


#account_ssd = "ACc049b8f9181b4e7b723400f9e0a11ae8".
account_ssd = os.environ.get("account_ssd")
auth_tocan = "cf0d0b387e8d90bd664d3fc622ea002d"

resource = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=19.075983&lon=72.877655&exclude=current,minutely,daily&appid=cf55771564381e0eb89148cda0a2ade0")
resource.raise_for_status()
data = resource.json()
wether_slice = data["hourly"][:12]
for hour_data in wether_slice:
    condition_weather = hour_data["weather"][0]["id"]
    if int(condition_weather) < 850:
        is_rain = True

if is_rain:
    print("will rain")
    client = Client(account_ssd, auth_tocan)
    message = client.messages.create(
                                  body="Hi this is a test messege",
                                  from_="+15136471337",
                                  to="+918805991079"
                              )

    print(message.status)
#print(data["hourly"][0]["weather"][0]["id"])