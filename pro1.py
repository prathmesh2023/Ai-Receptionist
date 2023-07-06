import pyttsx3
import speech_recognition as sr
import datetime
import vlc


import pyqrcode
import png
from pyqrcode import QRCode


from PIL import Image

engine=pyttsx3.init()
voices = engine.getProperty('voices')


maplink = "https://maps.google.com/?q="





def wish():
    speak('I am Your Virtual receptionist Created By Kedar, Aniket and Prathmesh As An Final Year Project')

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

 

    speak("I am Rambhau Sir. Please tell me how may I help you")


def speak(audio):
    engine.setProperty("rate",188)
    engine.say(audio)

    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wish()

    while True:
        query = takeCommand().lower()


        if 'the time' in query:
            strt = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strt}")

        elif 'who are you' in query:
            
            speak("I am Rambhau. ")
            speak("Created By Prathamesh Lohar.")
            speak("Aniket Madhurkar .")
            speak("And  Kedaar  Tandalee .")
            speak("As  An,  Final  Year  Project.")

        elif 'play national anthem' in query:

            speak("Playing .")
            speak("National .")
            speak("Anthem .")
            speak("3.")
            speak("2.")
            speak("1.")
        
            m=m=vlc.MediaPlayer("/home/prathmesh/Downloads/jangan.mp3")
            m.play()

        elif 'where is it department' in query:

            loc="18.408286,76.520372"

            s=maplink+loc

            print(s)

            url = pyqrcode.create(s)

            url.svg("myqr.svg", scale=8)

            url.png('myqr.png', scale=8)

            im = Image.open("/home/prathmesh/Desktop/project/myqr.png")

            im.show()

            speak("Scan The QR Code. ")
            speak("And Get Location.")

        elif 'joke' in query:
            jk=m=vlc.MediaPlayer("/home/prathmesh/Downloads/joke.mp3")
            jk.play()

        elif 'college website' in query:
            abt="https://www.msbecl.ac.in/"
            url = pyqrcode.create(abt)

            url.svg("myqr.svg", scale=8)

            url.png('myqr.png', scale=8)

            im = Image.open("/home/prathmesh/Desktop/project/myqr.png")

            im.show()

            speak("Scan The QR Code. ")
            speak("And Viste Webiste.")

        elif 'exit' in query:
            exit(0)

        elif 'favourite food' in query:
            speak("chiken biryani")


