import time
import os
import subprocess
import sys

def Install(package): # PACKAGE INSTALLER
    try:
        print("Installing " + package + " package. Please wait...",sep='')
        subprocess.call([sys.executable, "-m", "pip", "install", package])
        print("Package installed!\n")
    except ImportError:
        print("Installation of package failed.\n")

installation = input("Online installation? (Y/N) ").lower()
print()

if installation == "y":
    Install("SpeechRecognition")
    Install("Translate")
    Install("gTTS")
    Install("Pyttsx3")
    Install("PypiWin32")
    Install("PyLyrics")
    Install("PyDictionary")
else:
    print("Installing packages...")
    os.system("tar -xzf translate-3.5.0.tar.gz")
    os.system("tar -xzf gTTS-2.0.3.tar.gz")
    os.system("tar -xzf SpeechRecognition-3.2.0.tar.gz")

print("Installation finished.\n")
start = input("Would you like to start Nia now? (Y/N) ").lower()

if start == "y":
    os.system("nia.py")
    print("Exiting..")
    time.sleep(1)
    exit()
else:
    print("Exiting..")
    time.sleep(1)
    exit()
