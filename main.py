import requests
import os
from twilio.rest import Client
api_key = "53ac5ab22e8be59da04ede6edfcff77c"
account_sid = 'ACd545d5faf334286ffg7e5c5298f7f895'
auth_token = '529bdg4t3b7a8a8d49jd5wc8e97d2c1a'

parameters = {
    "lat":43.325989,
    "lon":-79.798302,
    "appid":"53ac5ab22er7e59dd24ede6ejfcfte7c",
    "cnt":4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)

weather_data = response.json()
id = weather_data["list"][0]["weather"][0]["id"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Hello Nik Patel",
                         from_='+12513879789',
                         to='+18957452358'
                     )
    print(message.sid)