from gtts import gTTS
import os
from time import sleep
import pyglet

import speech_recognition as sr

def speak(audio):
    tts =  gTTS(audio,lang="mr",tld="co.in")
    filename="play.mp3"
    tts.save(filename)

    music = pyglet.media.load(filename,streaming=True)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file
    # playsound('play.mp3')



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,0,7)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='mr')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


speak("नमस्कार, मी तुमची कशी मदत करू शकते ?")


if __name__ == "__main__":
  

    while True:
        query = takeCommand().lower()


        if 'जेवण झालं का' in query:
            
            speak("हो मी आत्ताच काही होल्टेज current खाल्ला आहे")