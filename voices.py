from jarvis import jarvis
import pyttsx3
import speech_recognition as sr 

engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
