import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get values from the .env file
api_key = os.getenv("OWM_API_KEY")
city = os.getenv("CITY")

# ✅ TEMP: Print the API key to check if it loaded
print("Loaded API Key:", api_key)

# Make the API request
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
response = requests.get(url)

# Print the raw weather data
print("Raw weather data:")
print(response.json())
