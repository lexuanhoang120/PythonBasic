import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os


friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty("voice", voice[1].id)


def speak(audio):
    print("F.R.I.D.A.Y.:  " + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)


def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning , Sir")
    elif 12 <= hour < 18:
        speak("Good afternoon , Sir")
    elif 18 <= hour < 24:
        speak("Good night , Sir")
    speak("How can i help you ?")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="en")
        print("Xuan Hoang :" + query)
    except sr.UnknownValueError:
        print("Please repeat or tying the command ")
        query = str(input("Your order is: "))
    return query


if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should i search boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on the google")
        if "youtube" in query:
            speak("What should i search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on the youtube")
        elif "open video":
            meme = r"E:\Documents\Python\visualassistantfriday\meme.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("friday is quitting sir. Goodbye boss")
            quit()
