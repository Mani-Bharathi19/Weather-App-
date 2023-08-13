from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
import colorsys

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['my']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json_file= result.json()
        city = json_file['name']
        country = json_file['sys']['country']
        temp_kelvin = json_file['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_far=(temp_kelvin-273.15)*9/5+32
        weather1 = json_file['weather'][0]['main']
        final = (city, country, temp_celsius,temp_far, weather1)
        return final
    else:
        print("NO Content Found")


# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = '{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Driver Code
# create object
app = Tk()
app.geometry("700x400")
app.title("My Weather App")
app.config(background="lightblue")
def change_background_color():
    global hue
    hue = (hue + 0.01) % 1
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))
    app.config(background=hex_color)
    app.after(50, change_background_color)


# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=("Arial", 20), fg="black")
city_entry.pack(pady=20)

Search_btn = Button(app, text="Search Weather", width=20, bg="orange", fg="white", font=("Arial", 15, "bold"), command=search)
Search_btn.pack()

location_lbl = Label(app, text="", font=("Arial", 30, "bold"), bg="lightpink")
location_lbl.pack(pady=10)

temperature_label = Label(app, text="", font=("Arial", 30, "bold"), bg="lightgreen")
temperature_label.pack(pady=10)

weather_l = Label(app, text="", font=("Arial", 30, "bold"), bg="yellow")
weather_l.pack(pady=10)

hue = 0  # Initialize hue value
change_background_color()
app.mainloop()
