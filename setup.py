import time
import os
import subprocess
import sys

def Install(package): # PACKAGE INSTALLER
    try:
        print("Installing " + package + " package. Please wait...",sep='')
        subprocess.call([sys.executable, "-m", "pip", "install", package])
        print("Package installed!")
    except ImportError:
        print("Installation of package failed.")

def SpeechInstall(): # INSTALL SPEECH RECOGNITION PACKAGE
    Install("SpeechRecognition")

SpeechInstall()
time.sleep(2)
