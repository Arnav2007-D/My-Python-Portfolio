import requests

print("WELCOME TO ARNAV'S WEATHER APP")
print("☀️--------☀️------☀️-------☀️-")
print("\n") 
API_KEY = "ef09ebef6b82620e7604b6644f8799f2"

user_input = input("Enter city: ")

weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={API_KEY}"
)

data = weather_data.json()

if str(data.get("cod")) == "404":
    print("No city found!")
elif str(data.get("cod")) != "200":
    print("API error:", data.get("message", "Unknown error"))
else:
    weather = data["weather"][0]["main"]
    temp = round(data["main"]["temp"])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°C")