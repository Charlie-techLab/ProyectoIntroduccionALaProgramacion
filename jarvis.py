"""
pip install pyttsx3
pip install SpeechRecognition
pip install pywhatkit
pip install pyjokes
pip install PyPDF2
"""

import pyttsx3
import speech_recognition as sr 
import pywhatkit 
import pyjokes 
import webbrowser
import datetime
import wikipedia
import sounddevice 
from scipy.io.wavfile import write 
import sounddevice 
from scipy.io.wavfile import write
from hangman import hangman
from draw_welcome_jarvis import draw_welcome_jarvis
from menu import menu
from audiobook import audiobook


# Voice options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# Welcome function
def greet():
    # Store moment of the day
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = 'Good evening'
    elif 6 <= hour.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'

    # Tell a greet
    talk(f'Hello, {moment}, nice to meet you.')
    talk('What is your name? Please write it in the console: ')
    name = input('What is your name? Please write it in the console: ')
    talk(f'Nice to meet you {name}!')
    talk('I am Jarvis, your personal assistant. Tell me how can I help you')

"""
To know the available voices:

engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
"""

# Listen the microphone and return audio as a text
def transform_audio_in_text():
    
    #Store recognizer r = recognizer
    r = sr.Recognizer()

    # Configure the microphone
    with sr.Microphone() as origin:

        # Lead Time
        r.pause_threshold = 0.8

        # Inform that the recording has begun
        print('You can talk :)')

        # Store the audio
        audio = r.listen(origin)

        try:
            # Searching in Bing
            request = r.recognize_google(audio, language = "en-us")

            # Print audio
            print(f'You said: "{request}."')

            # return request
            return request
        
        # When audio is not understood
        except sr.UnknownValueError:
            print('I did not understand :(')

            # Return error
            return 'I am still waiting...'
        
        # When request could not be solved
        except sr.RequestError:
            print('There is no service :(')

            # Return error
            return 'I am still waiting...'

        # Unexpected error
        except sr.RequestError:
            print('Something went wrong :(')

            # Return error
            return 'I am still waiting...'


# Function for the assistant can be heard
def talk(message):

    #Ignite the engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)

    # Read the message
    engine.say(message)
    engine.runAndWait()

"""
To know the available voices:

engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
"""


# Inform the day of the week
def request_day():
    
    # Store current date
    day = datetime.date.today()
    print(day)

    # Store current day of the week
    day_of_the_week = day.weekday()
    print(day_of_the_week)

    # Dictionary with the names of the days of the week
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday',
                }
    # Tell the day of the week
    talk(f'Today is {calendar[day_of_the_week]}')

# Inform the hour of the day
def request_hour():
    # Store data from hour
    hour = datetime.datetime.now()
    hour = f'It is {hour.hour} hours, {hour.minute} minutes and {hour.second} seconds'
    print(hour)

    # Tell the hour
    talk(hour)


# Central command of the assistant
def central_command():

    # Initializing central command
    start = True
    
    # Central loop
    while start:

        # Activate the microphone and store the request in a string
        request = transform_audio_in_text()

        if 'open YouTube' in request:
            talk('Sure. I am opening YouTube')
            webbrowser.open('https://www.youtube.com')
        elif 'open browser' in request:
            talk('Sure. I am opening Bing')
            webbrowser.open('https://www.bing.com')
            continue
        elif 'open chat' in request:
            talk('Great. Here it is')
            webbrowser.open('https://chat.openai.com/')
            continue
        elif 'what day is today' in request or 'get the current date' in request:
            request_day()
            continue
        elif 'what time is it' in request or 'get the current time' in request:
            request_hour()
            continue
        elif 'Wikipedia' in request or 'wikipedia' in request or 'open Wikipedia' in request:
            talk('Looking for it in wikipedia')
            request = request.replace('search in wikipedia', '')
            wikipedia.set_lang('en')
            result = wikipedia.summary(request, sentences=2)
            talk('Wikipedia states the following information:')
            talk(result)
            continue
        elif 'search in Internet' in request:
            talk('I am looking for it')
            request = request.replace('search in Internet', '')
            pywhatkit.search(request)
            talk('I have found this')
            continue
        elif 'get a recording' in request:
            # sample_rate
            fs=44100
            # Ask to enter the recording time
            second = int(input("Enter the recording time in seconds: "))
            print("Recording...\n")
            record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
            sounddevice.wait()
            write("MyRecording.wav", fs, record_voice)
            print("Recording in done. Please check your folder to listen recording")
        elif 'Play' in request or 'play' in request or 'play a video from internet' in request:
            talk('Great idea. I am doing it now')
            pywhatkit.playonyt(request)
            continue
        elif 'Hangman' in request or 'hangman' in request:
            hangman()
            continue
        elif 'audiobook' in request:
            talk('Great. You are going to learn about object oriented programming.')
            audiobook() and input('Press q if you want to stop listening: ')
            if 'q':
                break
            talk('I hope you loved this interesting topic')
            continue
        elif 'bye' in request:
            talk('Happy to help you. I am here whenever you need it')
            break

# Call the functions
greet()
draw_welcome_jarvis()
menu()
central_command()
