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
    except requests.exception.HTTPError as errh:
        print(f"HTTP Error:{errh}")
    except requests.exception.ConnectionError as errc:
        print(f"Error Connection:{errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error:{errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error:{err}")
    return None 
def main():
    api_key='47d244805373d83af4de0b0f073b1d73'
    city = input("Enter the city: ")
    weather_data = get_weather(api_key,city)

    
if __name__=="__main__":
    main()