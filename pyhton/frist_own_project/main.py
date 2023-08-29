import requests
from datetime import datetime
gender = "male"
weight_kg = "69"
hight_cm = "175"
age = "21"
App_id = "93bd5c67"
nutra_key = "70a37ccaa2a4f014b08693428145261d"
exercise_text = input("Tell me which exercises you did: ")
header = {
    "x-app-id":App_id,
    "x-app-key":nutra_key,
}
params_exrice = {
    "query":exercise_text,
    "gender":gender,
    "weight_kg":weight_kg,
    "height_cm":hight_cm,
    "age":age,
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5707b3df4d99dd34879be68ce5c7ff50/myWorkouts/workouts"

response = requests.post(exercise_endpoint, json=params_exrice, headers=header)
result = response.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_input ={
        "workout":{
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheet_response = requests.post(sheet_endpoint, json=sheet_input)
    print(sheet_response.text)