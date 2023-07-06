from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import datetime
from operations import basic

import vlc


import pyqrcode
import png
from pyqrcode import QRCode


from PIL import Image

import os
import pyglet
from time import sleep

from pywikihow import search_wikihow

from neurons import chat



language= "en"
tlds = "co.in"    

maplink = "https://maps.google.com/?q="


engine=pyttsx3.init()
voices = engine.getProperty('voices')

def speak2(audio):
    engine.setProperty("rate",188)
    engine.say(audio)

    engine.runAndWait()


def speak(audio):
    tts =  gTTS(audio,lang=language,tld=tlds)
    filename="play.mp3"
    tts.save(filename)

    music = pyglet.media.load(filename,streaming=True)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file
    # playsound('play.mp3')



def wish():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

 

    speak("I am Virtual Receptionist Sir. Please tell me how may I help you")




def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,0,7)


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
            strt = basic.time()
            speak(f"Sir, the time is {strt}")


        elif 'play national anthem' in query:

            speak("Playing National Anthem.")
            
            speak("3.")
            speak("2.")
            speak("1.")
        
            m=vlc.MediaPlayer("/home/prathmesh/Downloads/jangan.mp3")
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
            speak("And Viste Website.")

        elif 'exit' in query:
            exit(0)

        elif 'favourite food' in query:
            speak("chiken biryani")

        elif 'question' in query:
            
            speak2("ok what is your question ? ")
            question = takeCommand()
            speak2("please wait")
            max_res=1
            ans = search_wikihow(question,max_res)
            assert len(ans) == 1
            ans[0].print()
            speak2(ans[0].summary)

        elif 'wikipedia' in query:    
            speak('Searching Wikipedia please wait...')
            wiki = basic.wiki(query)
            speak("According to Wikipedia")
            speak(wiki)

        elif 'news from university' in query:
            from scrape import dbatu

            result = dbatu.get_news()
            print(result)

            speak(result)
            
        
        else:
            neuro = str(chat.neuro(query))
            print(neuro)
            speak(neuro)
            
            # if neuro == 'I do not understand...' :
            #     wiki = basic.wiki(query)
            #     speak(wiki)
            






