import requests

print("WELCOME TO ARNAV'S WEATHER APP 🌤️")
print("☀️--------☀️------☀️-------☀️-")
print("\n") 

API_KEY = "ef09ebef6b82620e7604b6644f8799f2"  

while True:
    user_input = input("Enter city: ").strip()
    if user_input:
        break
    print("City name cannot be empty!")

try:
    print(f"Fetching weather for {user_input}...")
    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={API_KEY}",
        timeout=10
    )
    
    data = weather_data.json()
    
    if str(data.get("cod")) == "404":
        print("❌ No city found!")
    elif str(data.get("cod")) != "200":
        print("❌ API error:", data.get("message", "Unknown error"))
    else:
        weather = data["weather"][0]["main"]
        temp = round(data["main"]["temp"])
        
        print(f"🌤️ The weather in {user_input.title()} is: {weather}")
        print(f"🌡️  The temperature is: {temp}°C")
        
except requests.exceptions.RequestException:
    print("❌ No internet connection or API unavailable!")
except KeyError:
    print("❌ Invalid API response - check your API key")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

input("\nPress ENTER to exit...")
