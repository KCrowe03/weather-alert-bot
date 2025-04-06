import os
import requests
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

# Load environment variables from .env
load_dotenv()

# Get values from the .env file
api_key = os.getenv("OWM_API_KEY")
city = os.getenv("CITY")

# Make the API request
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
response = requests.get(url)

# Print the raw weather data
print("Raw weather data:")
print(response.json())

# Get the weather description
data = response.json()
description = data["weather"][0]["description"]

# Check for rain
if "rain" in description.lower():
    print("It might rain today. Don’t forget an umbrella.")

    # Setup email details
    email_user = os.getenv("EMAIL_ADDRESS")
    email_pass = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "Rain Alert"
    msg["From"] = email_user
    msg["To"] = email_user
    msg.set_content("Heads up! The forecast says it might rain today. Bring an umbrella.")

    # Email sending is currently disabled for safety. Uncomment to enable.
    # with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as smtp:
    #     smtp.login(email_user, email_pass)
    #     smtp.send_message(msg)
    print("(Email sending is currently commented out)")
else:
    print("No rain expected today. You're good to go.")
