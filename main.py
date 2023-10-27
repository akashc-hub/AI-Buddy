import speech_recognition as sr
import os
import win32com.client
import webbrowser
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
    print('Pycharm')
    say = win32com.client.Dispatch("SAPI.SpVoice")
    say.Speak("Jarvis A. I.")
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

        # say(query)
