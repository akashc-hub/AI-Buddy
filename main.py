import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import winshell as winshell    # pip install winshell
import pyautogui        # pip install pyautogui
import pyjokes          # pip install pyjokes
import pywhatkit
import SnakeGame
import bs4              # pip install beautifulsoup4
import requests
from speedtest import Speedtest                    # pip install speedtest-cli
import smtplib
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import openai
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry!"

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = main["temp"]
            humidity = main["humidity"]

            weather_info = f"The weather in {city} is {weather_desc}. "
            weather_info += f"The temperature is {temperature} degrees Celsius, and humidity is {humidity}%."
            return weather_info
        else:
            return "City not found. Please check the city name."

    except Exception as e:
        return f"An error occurred: {e}"

def search_on_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(search_url)

if __name__ == '__main__':
    print('AI-Buddy')
    say = win32com.client.Dispatch("SAPI.SpVoice")
    say.Speak("A. I. Buddy")
    while True:
        print("Listening..")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.co.in/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say.Speak(f"Opening {site[0]} Sir..!")
                webbrowser.open(site[1])
        if "open music" in query:
            say.Speak("Opening music...")
            musicPath = "C:\\Users\\amd\\Desktop\\pythonProject\\Firecracker.mp3"
            os.system(f"start {musicPath}")

        elif "tell the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say.Speak(f"Sir the time is {strfTime}")

        elif "tell the date" in query:
            strfDate = datetime.datetime.now().strftime("%Y-%m-%d")
            say.Speak(f"Sir the Date is {strfDate}")

        elif "open vs code" in query:
            say.Speak("Opening VS code Sir...!")
            os.startfile("C:\\Users\\amd\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        # elif 'search' in query:
        #     query = query.replace('search', '')
        #     pywhatkit.search(query)

        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                say.Speak("Recycle Bin is cleaned successfully.")
            except Exception as e:
                print("Recycle bin is already Empty.")
                say.Speak("Recycle bin is already Empty.")

        elif 'write a note' in query or 'make a note' in query:
            say.Speak("What should I write, sir??")
            note = takeCommand()
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            file = open('Notes.txt', 'a')
            file.write(str_time)
            file.write(" --> ")
            file.write(note)
            say.Speak("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            say.Speak("Reading Notes")
            file = open("Notes.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            say.Speak(data_note)

        elif 'take screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            print("Screenshot taken successfully.")
            say.Speak("Screenshot taken successfully.")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            say.Speak(joke)

        elif 'snake game' in query:
            try:
                print("Starting the game!")
                say.Speak("Starting the game!")
                SnakeGame.game()
            except Exception as e:
                pass

        elif 'news' in query or 'news headlines' in query:
            url = "https://news.google.com/news/rss"
            response = requests.get(url)
            if response.status_code == 200:
                xml_page = response.text
                page = bs4.BeautifulSoup(xml_page, 'lxml')  # Specify the parser as 'lxml' pip install lxml
                news_list = page.findAll("item")
                say.speak("Today's top headlines are--")
                try:
                    for news in news_list:
                        print(news.title.text)
                        say.speak(f"{news.title.text}")
                        print()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print(f"Failed to fetch news. Status code: {response.status_code}")

        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            say.Speak("Wait!! I am checking your Internet Speed...")
            print("Checking...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            say.Speak(f'Your download speed is {round(dw_speed, 3)} Mbps')
            say.Speak(f'Your upload speed is {round(up_speed, 3)} Mbps')

        elif 'weather' in query:
            say.Speak("Sure! Please tell me the city name.")
            city_name = takeCommand()
            api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your API key
            weather_result = get_weather(api_key, city_name)
            print(weather_result)
            say.Speak(weather_result)

        elif 'search on YouTube' in query:
            say.Speak("What would you like to search for on YouTube?")
            search_query = takeCommand()
            search_on_youtube(search_query)





        # say(query)

































