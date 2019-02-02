
# nia - a virtual assistant

import time # USED DEAL WITH TIME
import random # USED TO SELECT RANDOM THINGS
from random import randint # USED TO SELECT NUMBERS
import subprocess
from subprocess import call
import sys
import os
import webbrowser # USED TO OPEN WEBPAGES
import speech_recognition as sr
from PyDictionary import PyDictionary
from PyLyrics import *
from weather import Weather, Unit

# IMPORT PYTHON TEXT-TO-SPEECH
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # FEMALE VOICE
engine.setProperty('rate', 150) # SPEECH SPEED

import tkinter
from tkinter import *

hellos = ["Hello!","What's up?","How's it going?","Hi!","Hey!"]
byes = ["bye","goodbye","see you", "until next time","see you later"]
bye = ["Bye!","See ya!", "Until next time...","See ya later!"]
action = ["Press Enter to speak.","When you're ready to speak, press Enter.","Press Enter when you're ready to speak."]
start = ["Let's start!","Press Enter to speak."]

language = 'en'
dictionary = PyDictionary()

# ALL THE FUNCTIONS ARE BELOW #

def Start():
    enter = input(random.choice(action))
    if enter == "":
        Speak()
    else:
        print("Please press Enter.\n")
        Start()
        
def Cls(): # CLEAR SCREEN
    os.system('cls')
    Start()

def ClsFirst(): # CLEAR SCREEN
    os.system('cls')

def Shutdown(): # SHUTDOWN PC
    print("Shutting down your PC.")
    os.system('shutdown -s -t 0')

ClsFirst()

def Speak(): # ALL THE SPEECH RECOGNITION STUFF
    r = sr.Recognizer()
    mic = sr.Microphone()
    r.energy_threshold = 60
        
    with mic as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        print("Nia's listening...\n")
        engine.say("I'm listening.")
        engine.runAndWait()
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio)
        print('Nia thinks you said: {}'.format(speech))
        time.sleep(1)

        speech = speech.lower()

        # IF ANY OF THESE WORDS APPEAR IN YOUR SPEECH, NIA WILL CARRY OUT THE FOLLOWING ACTIONS

        if "hello" in speech: # SAY 'HELLO' BACK IF USER SAYS 'HELLO'
            print(random.choice(hellos))
            time.sleep(1)

        if "weather" in speech:
            weather = Weather(unit=Unit.CELSIUS)
            city = input("Enter the name of a city: ")
            location = weather.lookup_by_location(city)
            condition = location.condition
            print(condition.text)
            engine.say(condition.text)
            engine.runAndWait()

        if "defin" in speech:
            print()
            print("What word would you like to define? ")
            time.sleep(2)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                time.sleep(1)
                print()
                word = speech
                print(dictionary.meaning(word))
                engine.setProperty('rate', 165) # SPEECH SPEED
                engine.say((dictionary.meaning(word)))
                engine.runAndWait()
                engine.setProperty('rate', 150) # SPEECH SPEED
                    
            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()

        if "lyric" in speech:
            type = input("Would you like to speak or type the artist name? (Y = Speak/N = Type) ").lower()

            if type == "y":
                time.sleep(1)
                with mic as source:
                    print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                    r.adjust_for_ambient_noise(source)
                    print("Nia's listening...\n")
                    engine.say("I'm listening.")
                    engine.runAndWait()
                    audio = r.listen(source)

                try:
                    speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                    print('Nia thinks you said: {}'.format(speech))
                    artist = speech
                    time.sleep(1)

                    print("What's the song name? ")
                    time.sleep(1)

                    with mic as source:
                        print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                        r.adjust_for_ambient_noise(source)
                        print("Nia's listening...\n")
                        engine.say("I'm listening.")
                        engine.runAndWait()
                        audio = r.listen(source)

                    try:
                        speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                        print('Nia thinks you said: {}'.format(speech))
                        time.sleep(1)
                    
                        song = speech

                        print()
                        print(PyLyrics.getLyrics(artist, song)) 
                        print()
                    
                    except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                        print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                        time.sleep(1)
                        print()
                    except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                        print("Sorry, Nia couldn't understand your speech.")
                        time.sleep(1)
                        print()

                    print()
                    print(PyLyrics.getLyrics(artist, song)) 
                    print()
                    
                except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                    print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                    time.sleep(1)
                    print()
                except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                    print("Sorry, Nia couldn't understand your speech.")
                    time.sleep(1)
                    print()
            else:
                artist = input("What's the artist name? ")
                song = input("What's the song name? ")
                print(PyLyrics.getLyrics(artist, song))                
                
        if "help" in speech: # HELP
            print(">>> Hello\n>>> Help\n>>> Clear - clear screen\n>>> Calculat(e/or) - open calculator\n>>> Define / Definition - Define a word\n>>> Lyric(s) - Search lyrics to a song\n>>> Close Chrome - close Chrome tabs/windows\n>>> Translate - translate words or phrases\n>>> YouTube - search YouTube videos and channels\n>>> Google - search Google\n>>> Bye - exit\n")
            print("PLEASE NOTE: You do not have to use the words on their own. You can also say a sentence including\nthe words and it should work fine.")
            engine.say("I'm listening.")
            engine.runAndWait()
            
        if "clear" in speech: # CLEAR THE SCREEN WHEN 'CLEAR' IS SAID
            Cls()

        if "calculate" in speech: # OPEN CALCULATOR
            print("Opening Calculator...")
            engine.say("Opening Calculator.")
            engine.runAndWait()
            call(["calc.exe"])

        if "calculator" in speech: # OPEN CALCULATOR
            print("Opening Calculator...")
            engine.say("Opening Calculator.")
            engine.runAndWait()
            call(["calc.exe"])

        if "shutdown" in speech: # SHUT DOWN
            print("Are you sure you want to shutdown your PC? Yes or No?")
            engine.say("Are you sure you want to shutdown your PC? Yes or No?")
            engine.runAndWait()
            time.sleep(1)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                time.sleep(1)
                print()

                if "yes" in speech:
                    Shutdown()
                if "yeah" in speech:
                    Shutdown()
                    
            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()

        if "close" and "chrome" in speech: # CLOSE CHROME
            os.system("taskkill /im chrome.exe /f")
            print("Chrome tabs closed.")

        if "translate" in speech: # TRANSLATION
            from translate import Translator
    
            print("\nWhat would you like to translate?\n") # PHRASE
            time.sleep(1)
            
            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                inputted = speech
                time.sleep(1)
                print()
            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()
                
            print("Which language would you like to translate to?\n") # LANGUAGE
            time.sleep(1)
            
            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                lang = speech
                time.sleep(1)
                print()
            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()
            
            translator = Translator(to_lang=lang)
            translation = translator.translate(inputted)
            print("Original:\n",inputted,"\n\n","Translated:","\n",translation, sep='')
            print()

        if "youtube" in speech: # SEARCH ON YOUTUBE IF 'YOUTUBE' IS MENTIONED
            print("What would you like to search on YouTube?\n")
            time.sleep(2)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                time.sleep(1)

                print("Searching '"+ speech +"' on YouTube...",sep='')
                query = speech # SEARCHES WHAT THE USER SAYS
                webbrowser.open('https://www.youtube.com/results?search_query='+query) # OPENS THE URL
                time.sleep(1)

            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()


        if "search" in speech: # SEARCH ON GOOGLE IF 'GOOGLE' IS MENTIONED
            print("What would you like to Google?\n")
            time.sleep(2)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                time.sleep(1)

                print("Searching '"+ speech +"' on Google...",sep='')
                query = speech # SEARCHES WHAT THE USER SAYS
                webbrowser.open('https://www.google.com/search?q='+query) # OPENS THE URL
                time.sleep(1)

            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()

        if ".com" in speech: # OPEN CUSTOM URL IF '.COM' IS MENTIONED
            time.sleep(2)

            print("Opening '"+ speech +"'",sep='')
            query = speech # SEARCHES WHAT THE USER SAYS
            webbrowser.open(query) # OPENS THE URL
            time.sleep(1)

        if ".co.uk" in speech: # OPEN CUSTOM URL IF '.CO.UK' IS MENTIONED
            time.sleep(2)

            print("Opening '"+ speech +"'",sep='')
            query = speech # SEARCHES WHAT THE USER SAYS
            webbrowser.open(query) # OPENS THE URL
            time.sleep(1)

        if "google" in speech: # SEARCH ON GOOGLE IF 'GOOGLE' IS MENTIONED
            print("What would you like to Google?\n")
            time.sleep(2)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
                engine.say("I'm listening.")
                engine.runAndWait()
                audio = r.listen(source)

            try:
                speech = r.recognize_google(audio) # GOOGLE RECOGNIZES AUDIO
                print('Nia thinks you said: {}'.format(speech))
                time.sleep(1)

                print("Searching '"+ speech +"' on Google...",sep='')
                query = speech # SEARCHES WHAT THE USER SAYS
                webbrowser.open('https://www.google.com/search?q='+query) # OPENS THE URL
                time.sleep(1)

            except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
                print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
                time.sleep(1)
                print()
            except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
                print("Sorry, Nia couldn't understand your speech.")
                time.sleep(1)
                print()

        if speech == any(bye): # EXIT IF USER SAYS 'BYE'
            print(random.choice(bye))
            time.sleep(2)
            exit()
        
    except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
        print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
        engine.say("Speech Recognition API is unavailable.")
        engine.runAndWait()
        time.sleep(1)
        print()
    except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
        print("Sorry, Nia couldn't understand your speech")
        engine.say("Sorry, I couldn't understand your speech")
        engine.runAndWait()
        time.sleep(1)
        print()

    print()
    Start()

# END OF ALL FUNCTIONS #

print("I'm Nia, your virtual personal assistant.") # INTRODUCTION
engine.say("I'm Nia, your virtual personal assistant.")
engine.runAndWait()

print("I can help you with tasks like searching the web and having random conversations.")
engine.say("I can help you with tasks like searching the web and having random conversations if that's what you wanna do.")
engine.runAndWait()

print("Please note, Nia requires an Internet connection to function correctly.")
engine.say("Just so you know, I require an Internet connection to function correctly.")
engine.runAndWait()

print("If you ever need help, simply press Enter and say 'help'.\n")
engine.say("If you ever need help, simply press Enter and say 'help'.")
engine.runAndWait()

Start() # ASK FOR INPUT
