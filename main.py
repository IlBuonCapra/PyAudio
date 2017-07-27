# -*- coding: utf-8 -*-
import speech_recognition as sr
import time as t
import pyttsx as se

HOUR = t.strftime("%X")
DATE = str(t.strftime("%d %B %Y"))
TURN_OFF = "schiavo = False"
VOLUME = 1
RATE = 200
NAME = "JARVIS"
DRIVER = 'sapi5'#'espeak'
LANGUAGE = 'italian'

possible_commands = {
    "spegniti" : "{NAME} si sta spegnendo!",
    "ciao" : "Ciao!",
    "come va" : "Bene grazie!",
    "data" : "Oggi è {DATE}",
    "ora" : "Sono le {HOUR}",
    "chiami" : "Mi chiamo {NAME}",
    "grazie" : "Figurati!",
    "porcodio" : "Diocane!"
}

def make_action(command, possible_commands=possible_commands):
    if command in possible_commands.keys():
        speak(possible_commands[command].format(command))

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
        return ""

if __name__ == '__main__':
    l = sr.Recognizer()
    schiavo = True

    #test()
    #schiavo = False

    if schiavo:
        speak(NAME + " si stà accendendo")
    while schiavo:
        listening = listen()
        make_action(listening)
