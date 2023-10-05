import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir")
    else:
        talk("Good Evening Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)

        while True:
            audio = r.listen(source, phrase_time_limit=10)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio)
                print("User said: {}".format(query))
                break
            except Exception as e:
                print("Say that again please...")

    return query

if __name__ == "__main__":
    wishMe()
    talk("hello how are you. This is Evo sense")
    talk("how may i help you")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            talk('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\sudha\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
        elif 'thank you' in query:
            talk("Welcome Have a nice day")
            break
