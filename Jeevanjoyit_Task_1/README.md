# Task 1 - Voice Assistant

A Python-based voice assistant that responds to voice commands.

## Features

- Responds to greetings
- Tells current time and date
- Searches Google and YouTube
- Tells jokes

## Installation

```bash
pip install speechrecognition pyttsx3 pyaudio
```

> **Note:** If `pyaudio` fails on Windows, install it with:

```bash
pip install pipwin
pipwin install pyaudio
```

## How to Run

```bash
python main.py
```

## Voice Commands

| Command | Response |
|----------|----------|
| "Hello" | Greeting |
| "What time is it?" | Current time |
| "What is today's date?" | Current date |
| "Search [topic]" | Opens Google search |
| "Open YouTube" | Searches YouTube |
| "Tell me a joke" | Tells a joke |
| "Exit / Bye" | Closes the assistant |

## Author

**Jeevan Joyit**  
Oasis Infobyte Internship 2026
