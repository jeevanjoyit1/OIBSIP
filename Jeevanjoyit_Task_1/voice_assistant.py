import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        return ""

speak("Hello! I am your voice assistant.")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello Jeevan!")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open("https://www.google.com/search?q=" + query)
        speak("Searching for " + query)

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "bye" in command or "exit" in command:
        speak("Goodbye!")
        break
