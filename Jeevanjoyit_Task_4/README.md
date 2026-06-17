# 🌦 Weather App

A simple and beginner-friendly Weather Application built using **Python**, **Tkinter**, and the **OpenWeatherMap API**. This application allows users to enter a city name and view the current weather conditions, including temperature, humidity, and weather description.

---

## 📌 Features

- 🌍 Search weather by city name
- 🌡 Display current temperature in Celsius
- 💧 Show humidity percentage
- ☁ Display weather conditions
- 🖥 User-friendly graphical interface using Tkinter
- ⚠ Error handling for invalid city names and network issues

---

## 🛠 Technologies Used

- Python 3
- Tkinter (GUI)
- Requests Library
- OpenWeatherMap API

---

## 📂 Project Structure

```text
WeatherApp/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📋 Requirements

- Python 3.8 or higher
- requests==2.31.0

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests==2.31.0
```

---

## 🔑 Get an OpenWeatherMap API Key

1. Visit https://openweathermap.org/api
2. Create a free account.
3. Generate an API key.
4. Copy your API key.

---

## ⚙ Configuration

Open `main.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key:

```python
API_KEY = "your_actual_api_key"
```

---

## ▶ How to Run

Run the application using:

```bash
python main.py
```

---

## 🖥 Application Interface

The application provides:

- City Name Input Field
- Get Weather Button
- Weather Information Display Area
- Error Messages for Invalid Inputs

---

## 📊 Sample Output

```text
City: Kochi

Temperature: 29°C

Humidity: 78%

Condition: Broken Clouds
```

---

## 🚀 Future Enhancements

- Add weather icons
- Display wind speed and pressure
- Add hourly and daily forecasts
- Support multiple temperature units (°C/°F)
- Add automatic location detection
- Improve UI design with themes

---

## 🎯 Learning Outcomes

This project helps in understanding:

- API Integration
- JSON Data Parsing
- GUI Development with Tkinter
- Error Handling
- User Input Validation
- Python Programming Fundamentals

---

## 👨‍💻 Author

**Jeevan Joyit**

Oasis Infobyte Internship Project

---

## 📜 License

This project is created for educational and internship purposes.
