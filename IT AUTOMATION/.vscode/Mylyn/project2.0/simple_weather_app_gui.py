import requests 
import tkinter as tk
from tkinter import messagebox 

def get_weather(api,city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params ={
        'q': city,
        'appid': api,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data 
    except requests.exceptions.HTTPError as errh:
        messagebox.showerror("HTTP Error",f"HTTP Error:{errh}")
    except requests.exceptions.ConnectionError as errc:
        messagebox.showerror("Connection Error",f"Error Connecting:{errc}")
    except requests.exceptions.Timeout as errt:
        messagebox.showerror("Timeout Error",f"Timeout Error:{errt}")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error",f"Error:{err}")
    return None
def display_weather(weather_data):
    if weather_data:
        result_str = (
            f"Weather in {weather_data['name']},{weather_data['sys']['country']}:\n"
            f"Temperature:{weather_data['main']['temp']}°C\n"
            f"Humidity:{weather_data['main']['humidity']}%\n"
            f"Wind Speed:{weather_data['wind']['speed']}m/s\n"
            f"Conditions:{weather_data['weather'][0]['description']}"
        )
        result_label.config(text=result_str)
    else:
        result_label.config(text="Failed to retrieve weather data.")
def get_weather_and_display():
    city = city_entry.get()
    weather_data =  get_weather(api,city)
    display_weather(weather_data)

app = tk.Tk()
app.title("Simple Weather App")
api='47d244805373d83af4de0b0f073b1d73'

city_label = tk.Label(app,text="Enter City")
city_entry = tk.Entry(app,width=30)
search_button = tk.Button(app,text="Search",command=get_weather_and_display)
result_label = tk.Label(app,text="")

city_label.grid(row=0,column=0,pady=5)
city_entry.grid(row=0,column=1,pady=5)
search_button.grid(row=1,column=0,columnspan=2,pady=10)
result_label.grid(row=2,column=0,columnspan=2,pady=10)

app.mainloop()