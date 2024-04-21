import requests
api_key = "53ac5ab22e8be59da04ede6edfcff77c"


parameters = {
    "lat":43.325989,
    "lon":-79.798302,
    "appid":"53ac5ab22e8be59da04ede6edfcff77c",
    "cnt":4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)

weather_data = response.json()
id = weather_data["list"][0]["weather"][0]["id"]

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
# if id < 700:
#     print("Bring Umbrella")