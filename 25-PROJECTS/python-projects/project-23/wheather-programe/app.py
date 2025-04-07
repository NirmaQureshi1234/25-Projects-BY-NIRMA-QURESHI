import requests

# API Key
API_KEY = "2203925c7924239c97ac46a544442c31"

# Base URL for OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather(city):
    params = {
        "q": city,       # City name
        "appid": API_KEY,  # API key
        "units": "metric"  # Units for temperature (metric for Celsius)
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] == 200:  # Check if city is found
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Condition": data["weather"][0]["description"].title(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s",
        }
        return weather
    else:
        return {"Error": "City not found!"}

# User input for city name
city = input("Enter city name: ")
weather_info = get_weather(city)

# Display weather details
for key, value in weather_info.items():
    print(f"{key}: {value}")