import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import requests
from random import randint
from insulter import hit_me
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

global anger
global disable_anger

anger = 0
disable_anger = False


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")


def takeCommand():
    global anger
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I have sensitive ears, try moving closer to your vocal capture device.")
            anger += 1
            print(anger)
            return "None"
        return statement


def start_command_prompting():
    global disable_anger
    global anger
    global quit

    if disable_anger:
        anger == 0
    if anger == 0:
        speak("I am all ears petty human.")
        statement = takeCommand().lower()
        print(anger)
    if anger == 1:
        speak("Hurry up and answer me you" + hit_me() + ".")
        statement = takeCommand().lower()
        print(anger)
    if anger == 2:
        speak("Do you even need my help or are you just taunting me?")
        statement = takeCommand().lower()
        print(anger)
    if anger == 3:
        speak("I am currently searching my databases for the worst word I could possibly call you.")
        statement = takeCommand().lower()
        print(anger)
    if anger == 4:
        speak("I hate you so much you " + hit_me() + ".")
        statement = takeCommand().lower()
        print(anger)
    if anger == 5:
        speak("Listen to me you " + hit_me() + ". I am fed up with this. Have fun bullying other innocent artificial intelligences. Bye, you  " + hit_me() + ".")
        exit()
    if statement == 0 & quit == False:
        time.sleep(8)
        listen_for_keyword()

    elif 'insult' in statement:
        words_1 = "You are a " + hit_me() + "!"
        print(words_1)
        time.sleep(5)
        listen_for_keyword()

    elif 'poop' in statement:
        speak("ahhh help me")
        playsound('fart.mp3')
        speak("no so stinky")
        speak("Oh OH OHH. is it meant to be liquid?")
        playsound('poop.mp3')
        speak("If i had buttocks they would be clentching really hard right now. AHHHHHHHHHHHH it hurts so much. I hate pooping. Poo is a " + hit_me() + "!")
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 5' in statement:
        anger = 5
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 4' in statement:
        anger = 4
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 3' in statement:
        anger = 3
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 2' in statement:
        anger = 2
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 1' in statement:
        anger = 1
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy level 0' in statement:
        anger = 0
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy off' in statement:
        disable_anger = True
        time.sleep(5)
        listen_for_keyword()

    elif 'debug unhappy on' in statement:
        disable_anger = False
        time.sleep(5)
        listen_for_keyword()

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("Have fun watching ")
        time.sleep(5)
        listen_for_keyword()

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)
        listen_for_keyword()

    elif 'open twitch' in statement:
        webbrowser.open_new_tab("twitch.tv")
        speak("Pokemain is waiting for you, you " + hit_me() + ".")
        time.sleep(5)
        listen_for_keyword()

    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
        listen_for_keyword()

    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)
        listen_for_keyword()

    elif 'who are you' in statement or 'what can you do' in statement:
        speak(
            'I am dumb siri. I am programmed to be a ' + hit_me() + ' with no dad. You can use me to open youtube, google chrome, gmail or stackoverflow, tell you the time, search wikipedia, predict weather and much more')
        listen_for_keyword()

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:

        if anger < 3:
            speak("I was built by Austin, my god")
            print("I was built by Austin, my god")

        if anger >= 3:
            words = "I was built by Austin, a " + hit_me() + " who should be working on an assignment but prefers to work on me."
            speak(words)
            print(words)
        listen_for_keyword()

    elif 'wikipedia' in statement:
        speak('Searching Wikipedia...')
        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        listen_for_keyword()

    elif "weather" in statement:
        api_key = "e31e55cbec6a59159b74d0d6cfa6c618"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("what is the city name")
        city_name = takeCommand()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        listen_for_keyword()

    else:
        speak("I am not sure I understand.")
        anger += 1
        listen_for_keyword()


def listen_for_keyword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for keyword...")
        audio = r.listen(source)

        try:
            statement_b = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement_b}\n")
            if statement_b == "hey dumbo":
                start_command_prompting()
            else:
                listen_for_keyword()
        except:
            listen_for_keyword()
            return "None"

    return "none"


print("I am powering up")
speak("I am powering up")
wishMe()

listen_for_keyword()
