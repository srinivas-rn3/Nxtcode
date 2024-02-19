import requests

def get_weather(api_key,city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params ={
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status()
        weather_data = response.json()
        print(weather_data)
        return weather_data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error:{errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connection:{errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error:{errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error:{err}")
    return None 
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']},{weather_data['sys']['country']}")
        print(f"Temperature:{weather_data['main']['temp']}°C")
        print(f"Humidity:{weather_data['main']['humidity']}%")
        print(f"Wind Speed:{weather_data['wind']['speed']}m/s")
        print(f"Conditions:{weather_data['weather'][0]['description']}")
    else:
        print("Failed to retrieve weather data.")
def main():
    api_key='47d244805373d83af4de0b0f073b1d73'
    city = input("Enter the city: ")
    weather_data = get_weather(api_key,city)
    display_weather(weather_data) 

if __name__=="__main__":
    main()