import requests

#creating a function to get whether from the API.
def get_weather(city):
    api_key = '05bcbfc59881064b181c0aaa60fd15dc'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return weather, temperature, humidity, wind_speed
    else:
        return None
#get user city
city = input("Enter a city name: ")
weather_info = get_weather(city)
if weather_info:
    weather, temperature, humidity, wind_speed = weather_info
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Failed to retrieve weather information.")