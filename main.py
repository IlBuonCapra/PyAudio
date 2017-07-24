# -*- coding: utf-8 -*-

import speech_recognition as sr
from time import ctime,sleep
import pyttsx as se

VOLUME = 1
RATE = 200
NAME = "JARVIS"
DRIVER = 'espeak'
LANGUAGE = 'italian'

l = sr.Recognizer()

schiavo = True

def speak(text):
    print(NAME + " >> " + text)
    s = se.init(DRIVER)
    s.setProperty('rate', RATE)
    s.setProperty('volume', VOLUME)
    s.setProperty('voice', LANGUAGE)
    s.say(text)
    s.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Parla")
        l.adjust_for_ambient_noise(source)
        audio = l.listen(source)

    try:
        sound = l.recognize_google(audio, language = "it-IT")
        print("You >> " + sound)
        return sound
    except sr.UnknownValueError:
        print("Non ho capito")
        #print("Could not understand audio")
    except sr.RequestError as e:
        print("Errore {0}".format(e))

    return ""

if __name__ == '__main__':
    while schiavo:
        listening = listen()
        if "spegni" in listening:
            speak("CI STANNO TRACCIANDO! STACCA STACCA!")
            schiavo = False

        if "ciao" in listening:
            speak("Ciao")

        if "come va" in listening:
            speak("Bene grazie!")

        if "dimmi l'ora" in listening:
            speak(ctime())

        if "come ti chiami" in listening:
            speak("mi chiamo " + NAME)

        if "grazie" in listening:
            speak("figurati. dovere")
