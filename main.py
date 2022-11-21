import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import playsound
#from googlesearch import search

print("Intializing suzieeeee")

MASTER = "Vishwa"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12 :
        speak('Good Morning' + MASTER)

    elif hour>=12 and hour<18 :
        speak('Good Afternoon' + MASTER)

    else:
        speak('Good Evening' + MASTER)

    speak('Hi I am Suzieee. How may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try : 
        print("recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('vishwagandhi16@yahoo.com' , 'password')
    server.sendmail("vishwahiren16@gmail.com" , to , content)
    server.close()   

speak("Intializing suzieeeee...")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower() :
    speak('searching wikipedia..')
    query = query.replace("wikipedia" , "")
    results = wikipedia.summary(query , sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('youtube.com')

elif 'open google' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('google.com')

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\Vishwa Gandhi\\Music\\musiccc"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir , songs[2]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f'{MASTER} the time is {strTime}')

elif 'email to vishwa' in query.lower():
    try:
        speak("what should I send")
        content = takeCommand()
        to = "vishwahiren16@gmail.com"
        sendEmail(to , content)
        speak("email has been sent")

    except Exception as e:
        print(e)