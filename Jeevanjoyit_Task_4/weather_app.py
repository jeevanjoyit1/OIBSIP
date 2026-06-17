import tkinter as tk
from tkinter import messagebox
import urllib.request
import urllib.parse
import json

# ==========================
# OpenWeatherMap API Key
# ==========================
API_KEY = "532703e07f9bf901b9cde9201d78d3fa"

unit_system = "metric"


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        encoded_city = urllib.parse.quote(city)

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={encoded_city}&appid={API_KEY}&units={unit_system}"
        )

        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"].title()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        wind = data["wind"]["speed"]

        visibility = data.get("visibility", 0) / 1000

        emoji = get_weather_emoji(weather)

        unit_symbol = "°C" if unit_system == "metric" else "°F"

        result_label.config(
            text=f"""
{emoji} {description}

🌡 Temperature : {temp}{unit_symbol}

💧 Humidity : {humidity}%

🌬 Wind Speed : {wind} {'m/s' if unit_system == 'metric' else 'mph'}

📊 Pressure : {pressure} hPa

👀 Visibility : {visibility} km
"""
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def get_weather_emoji(condition):
    emojis = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️",
        "Smoke": "🌫️"
    }

    return emojis.get(condition, "🌍")


def toggle_unit():
    global unit_system

    if unit_system == "metric":
        unit_system = "imperial"
        unit_btn.config(text="Switch to °C")
    else:
        unit_system = "metric"
        unit_btn.config(text="Switch to °F")


# ==========================
# GUI
# ==========================
root = tk.Tk()
root.title("Weather App")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#1E293B")

title_label = tk.Label(
    root,
    text="🌦 Weather App",
    font=("Arial", 22, "bold"),
    bg="#1E293B",
    fg="white"
)
title_label.pack(pady=20)

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25,
    justify="center"
)
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Search Weather",
    command=get_weather,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)
search_btn.pack(pady=10)

unit_btn = tk.Button(
    root,
    text="Switch to °F",
    command=toggle_unit,
    bg="#10B981",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
)
unit_btn.pack(pady=10)

result_frame = tk.Frame(
    root,
    bg="#334155",
    bd=2,
    relief="ridge"
)
result_frame.pack(padx=20, pady=20, fill="both", expand=True)

result_label = tk.Label(
    result_frame,
    text="Enter a city and click Search",
    font=("Arial", 13),
    bg="#334155",
    fg="white",
    justify="left"
)
result_label.pack(padx=20, pady=20)

footer = tk.Label(
    root,
    text="Made by Jeevan Joyit",
    font=("Arial", 10),
    bg="#1E293B",
    fg="lightgray"
)
footer.pack(pady=10)

root.mainloop()
