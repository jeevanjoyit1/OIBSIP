import tkinter as tk
from tkinter import messagebox
import requests

# ==========================
# OpenWeatherMap API Key
# ==========================
API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            result_label.config(
                text=f"""
City: {city.title()}

Temperature: {temperature} °C

Humidity: {humidity}%

Condition: {condition.title()}
"""
            )
        else:
            messagebox.showerror(
                "Error",
                data.get("message", "Unable to fetch weather data")
            )

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Network Error",
            "Please check your internet connection."
        )


# ==========================
# GUI Window
# ==========================
root = tk.Tk()
root.title("Weather App")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#1E293B")

# Title
title_label = tk.Label(
    root,
    text="🌦 Weather App",
    font=("Arial", 22, "bold"),
    bg="#1E293B",
    fg="white"
)
title_label.pack(pady=20)

# City Input
city_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 14),
    justify="center"
)
city_entry.pack(pady=10)

# Search Button
search_button = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15
)
search_button.pack(pady=10)

# Result Frame
result_frame = tk.Frame(
    root,
    bg="#334155",
    bd=2,
    relief="ridge"
)
result_frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

# Result Label
result_label = tk.Label(
    result_frame,
    text="Enter a city name and click Get Weather",
    font=("Arial", 13),
    bg="#334155",
    fg="white",
    justify="left"
)
result_label.pack(padx=20, pady=20)

# Footer
footer = tk.Label(
    root,
    text="Created by Jeevan Joyit",
    font=("Arial", 10),
    bg="#1E293B",
    fg="lightgray"
)
footer.pack(pady=10)

root.mainloop()
