# Arnav's Weather App 🌤️
 -  Fetches real-time weather data using OpenWeatherMap API.

## Features
- Enter any city worldwide
- Displays current weather condition & temperature (°C)
- API error handling for bad responses

## How it works
- Uses `requests.get()` to call OpenWeatherMap API
- Checks `cod` status (200=success, 404=not found)
- Extracts `weather[0]["main"]` & `main["temp"]` from JSON

## What I learned 
- Learning how to work with API's
- Making API calls with `requests` library
- Error handling with status codes
## Future Improvements
-  Add wind speed, humidity
-  weather graph ( a simple one)


