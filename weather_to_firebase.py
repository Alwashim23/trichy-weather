import requests
import json

API_KEY = "42733499a593d1f9f404c6c3a25e2a28"
CITY = "Trichy"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
data = requests.get(url).json()

latest_weather = {
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "timestamp": data["dt"]
}

# Save as JSON (replace path with your repo path)
with open("latest_weather.json", "w") as f:
    json.dump(latest_weather, f)
