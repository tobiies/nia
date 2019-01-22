# nia - a virtual assistant

import time
import random
from random import randint
import subprocess
import sys
import os
import webbrowser # USED TO OPEN WEBPAGES
import speech_recognition as sr

action = ["When you're ready to speak, press enter.","Press enter when you're ready to speak."]

# ALL THE FUNCTIONS ARE BELOW #

def Cls(): # CLEAR SPEECH
    os.system('cls')

Cls()
    
def Start():
    enter = input(random.choice(action))
    if enter == "":
        Speak()

def Speak():
    r = sr.Recognizer()
    mic = sr.Microphone()
        
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
            print("Hello!")
            time.sleep(1)

        if "google" in speech:
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
                print("Sorry, Nia couldn't understand your speech.\nReturning to commands...")
                time.sleep(1)
                print()

        if "bye" in speech: # EXIT IF USER SAYS 'BYE'
            print("Bye!")
            time.sleep(2)
            exit()
        
    except sr.RequestError: # IF NIA CANNOT CONNECT TO THE API...
        print("Sorry, Speech Recognition API is unavailable. Please check your network connection.\nReturning to commands...")
        time.sleep(1)
        print()
    except sr.UnknownValueError: # IF YOUR SPEECH IS UNRECOGNIZABLE
        print("Sorry, Nia couldn't understand your speech.\nReturning to commands...")
        time.sleep(1)
        print()

    print()
    Start()

# END OF ALL FUNCTIONS #

print("I'm Nia, your virtual personal assistant.")
time.sleep(randint(1,2))
print("I can help you with tasks.\n")
time.sleep(randint(2,3))
Start() # ASK FOR INPUT
    
