# weather-alert-bot
Alert me if it's going to rain in the morning




# First Weather Alert Bot

This Python script checks the local weather forecast using the OpenWeatherMap API and prints a reminder if rain is expected. It's a simple automation project designed to practice using external APIs, managing environment variables, and building a real-world task into a script.

---

## Features

- Connects to OpenWeatherMap and retrieves weather data
- Looks for rain in the forecast and alerts the user
- Email alert feature included (commented out for safety)
- Uses a `.env` file to protect API keys and email credentials

---

## Setup Instructions

1. Clone the repository:

git clone https://github.com/KCrowe03/weather-alert-bot.git
cd weather-alert-bot


2. Create and activate a virtual environment:

python -m venv venv
source venv/Scripts/activate  # Use Git Bash


3. Install the dependencies:

pip install -r requirements.txt


4. Create a `.env` file:

OWM_API_KEY=your_openweathermap_api_key
CITY=YourCity
EMAIL_ADDRESS=youremail@example.com
EMAIL_PASSWORD=your_app_password


5. Run the script:

python main.py


---

## Notes

- The `.env` file is excluded from Git for security.
- A `.env.example` file is included to show how variables are used.
- The email feature is for practice and is not active by default.

---

## About Me

Coming soon. I'm currently working on more Python projects and building my portfolio.
```

