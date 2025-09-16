import requests
import json
from datetime import datetime

# ===== USER SETTINGS =====
API_KEY = "42733499a593d1f9f404c6c3a25e2a28"  # <-- Put your OpenWeather API key
CITY = "Trichy"
# Path to save JSON file (should be in your GitHub repo for the website)
JSON_FILE_PATH = "latest_weather.json"
# =========================

# Fetch weather from OpenWeather
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Prepare the latest weather snapshot
latest_weather = {
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "timestamp": datetime.now().isoformat()
}

# Save to JSON file
with open(JSON_FILE_PATH, "w") as f:
    json.dump(latest_weather, f, indent=4)

print("✅ latest_weather.json updated!")
