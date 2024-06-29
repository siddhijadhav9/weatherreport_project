import requests

def get_weather_forecast(city):
    api_key = '38b99bbe57c19d30081034907de0bc40'  
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change the units to 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['cod'] == 200:
            main = data['main']
            weather = data['weather'][0]
            temperature = main['temp']
            description = weather['description']
            
            return f'Current weather in {city}: {description}, Temperature: {temperature}°C'
        else:
            return f'Error: {data["message"]}'
    
    except Exception as e:
        return f'Error fetching weather data: {str(e)}'

# Example usage:
city=input("Please enter city: ")
forecast = get_weather_forecast(city)
print(forecast)