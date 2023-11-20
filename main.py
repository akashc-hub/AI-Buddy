import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import winshell as winshell    # pip install winshell
import pywhatkit         # pip install pywhatkit
import pyautogui        # pip install pyautogui
import pyjokes          # pip install pyjokes
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
        # say(query)
