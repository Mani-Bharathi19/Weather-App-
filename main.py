import tkinter as tk
import requests
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.configure(bg="#1e90ff")

# Create the labels and entry fields
tk.Label(root, text="City:", bg="#1e90ff", fg="white").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root, bg="#d3d3d3")
city_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Units:", bg="#1e90ff", fg="white").grid(row=1, column=0, padx=10, pady=10)
unit_choice = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly")
unit_choice.current(0)
unit_choice.grid(row=1, column=1, padx=10, pady=10)


# Define the function to get the weather information
def get_weather():
    city = city_entry.get()
    units = unit_choice.get()[0]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid=bcb771e74fad836ee647ac7a39521307"
    response = requests.get(url).json()

    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]

    # Create the labels to display the weather information
    temp_label = tk.Label(root, text=f"Temperature: {temperature}°{units}", bg="#1e90ff", fg="white")
    temp_label.grid(row=3, column=0, padx=10, pady=10)

    humidity_label = tk.Label(root, text=f"Humidity: {humidity}%", bg="#1e90ff", fg="white")
    humidity_label.grid(row=4, column=0, padx=10, pady=10)

    wind_speed_label = tk.Label(root, text=f"Wind Speed: {wind_speed} mph", bg="#1e90ff", fg="white")
    wind_speed_label.grid(row=5, column=0, padx=10, pady=10)


# Create the button to get the weather information
tk.Button(root, text="Get Weather", bg="#d3d3d3", command=get_weather).grid(row=2, column=0, columnspan=2, padx=10,
                                                                            pady=10)

# Start the main event loop
root.mainloop()

