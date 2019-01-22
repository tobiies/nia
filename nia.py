# nia - a virtual assistant

import time # USED DEAL WITH TIME
import random # USED TO SELECT RANDOM THINGS
from random import randint # USED TO SELECT NUMBERS
import subprocess
import sys
import os
import webbrowser # USED TO OPEN WEBPAGES
import speech_recognition as sr

hellos = ["Hello!","What's up?","How's it going?","Hi!","Hey!"]
bye = ["Bye!","See ya!", "Until next time...","See ya later!"]
action = ["Press Enter to speak.","When you're ready to speak, press Enter.","Press Enter when you're ready to speak."]

# ALL THE FUNCTIONS ARE BELOW #

def Start():
    enter = input(random.choice(action))
    if enter == "":
        Speak()
    else:
        print("Please press Enter.\n")
        Start()
        
def Cls(): # CLEAR SPEECH
    os.system('cls')
    Start()

def ClsFirst(): # CLEAR SPEECH
    os.system('cls')

ClsFirst()

def Speak(): # ALL THE SPEECH RECOGNITION STUFF
    r = sr.Recognizer()
    mic = sr.Microphone()
    r.energy_threshold = 60
        
    with mic as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        print("Nia's listening...\n")
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

        if "help" in speech: # HELP
            print(">>> Hello\n>>> Help\n>>> Clear - clear screen\n>>> YouTube - search YouTube videos and channels\n>>> Google - search Google\n>>> Bye - exit\n")
            print("PLEASE NOTE: You do not have to use the words on their own. You can also say a sentence including\nthe word and it should work fine.")

        if "clear" in speech: # CLEAR THE SCREEN WHEN 'CLEAR' IS SAID
            Cls()

        if "translate" in speech: # TRANSLATION
            from translate import Translator
    
            print("\nWhat would you like to translate?\n") # PHRASE
            time.sleep(1)
            
            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
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

        if "google" in speech: # SEARCH ON GOOGLE IF 'GOOGLE' IS MENTIONED
            print("What would you like to Google?\n")
            time.sleep(2)

            with mic as source:
                print("Adjusting for ambient noise, please wait...") # TRIES TO TUNE OUT BACKGROUND NOISE
                r.adjust_for_ambient_noise(source)
                print("Nia's listening...\n")
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

        if "bye" in speech: # EXIT IF USER SAYS 'BYE'
            print(random.choice(bye))
            time.sleep(2)
            exit()
        
    except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
        print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
        time.sleep(1)
        print()
    except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
        print("Sorry, Nia couldn't understand your speech")
        time.sleep(1)
        print()

    print()
    Start()

# END OF ALL FUNCTIONS #

print("I'm Nia, your virtual personal assistant.") # INTRODUCTION
time.sleep(randint(1,2))
print("I can help you with tasks like searching the web and having random conversations.")
time.sleep(randint(2,3))
print("Please note, Nia requires an Internet connection to function correctly.")
time.sleep(randint(2,3))
print("If you ever need help, simply press Enter and say 'help'.\n")
time.sleep(randint(1,2))
Start() # ASK FOR INPUT
    
