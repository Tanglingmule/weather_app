from configparser import ConfigParser
import requests
from customtkinter import *

# get config key
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
key = config["gfg"]["api"]
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format("{}","{}")

def get_weather(city):
    result = requests.get(url.format(city, key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelv = json['main']['temp']
        temp_celc = temp_kelv - 273.15
        weather_desc = json['weather'][0]['main']
        final = [city, country, temp_celc, weather_desc]
        print(final)
        return final
    else:
        print("Error in the HTTP request")

# explicit function to
# search city
def search():
    city = city_text.get()
    weather_data = get_weather(city)

    if weather_data:
        location_label.configure(text='{}, {}'.format(weather_data[0], weather_data[1]))
        temperature_label.configure(text="{} Degree Celsius".format(round(weather_data[2], 2)))
        weather_desc_label.configure(text=weather_data[3])
    else:
        location_label.configure(text='Not Found')
    
    # Update the GUI
    app.update_idletasks()


app = CTk()
app.geometry("500x500")
app.title("Weather App")

city_text = StringVar()
city_entry = CTkEntry(app, width=200, textvariable=city_text)
city_entry.pack(pady=20, padx=20)

search_button = CTkButton(app, text="Search", command=search)
search_button.pack(pady=0, padx=20)

location_label = CTkLabel(app, text="Location", font=('Bold', 25))
location_label.pack(pady=20, padx=20)

temperature_label = CTkLabel(app, text="" ,font=('Arial', 20))
temperature_label.pack(pady=0, padx=20)  

weather_desc_label = CTkLabel(app, text="", font =('Arial',20))
weather_desc_label.pack(pady=20, padx=20)

app.mainloop()
