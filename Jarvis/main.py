import pyttsx3
from datetime import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import time
import os
import random
engine=pyttsx3.init('sapi5')
#selecting voice
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def myself():
    '''
     it takes input from microphone as "who are you" and then Jarvis introdeuces itself.
    :return:
    '''
    speak("I am an artificial intelligence assistant, and i love ice-cream ha ha ha.")
def take_Command():
    '''
    This function takes input from the microphone and returns the command by recognizing
    it through speech recognizing module.
    :return:
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="us-in")
        print(query)
    except Exception as e:
        print("Couldn't recognize,speak again.")
        return "none"
    return query

def how_are_you():
    sentences=["i am totally fine, how are you my friend","i have been a bit tensed,but it's ok.",
               "What kind of question is this, i am a machine and i don't feel anything",
               "i am awesome man thank you soooooo much."]
    speak(random.choice(sentences))

def wishme():
    '''
    this function greets the user according to the current time.
    '''
    current_time=datetime.now().hour
    if current_time>=0 and current_time<12:
        speak("Good morning, I am jarvis.")
    elif current_time>=12 and current_time<16:
        speak("Good afternoon, I am jarvis.")
    else:
        speak("Good evening, I am jarvis.")

def speak(audio):
    '''
    This function takes input and speaks it out loud.
    :param audio:
    :return:
    '''
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == '__main__':
    wishme()
    while True:
        time.sleep(1)
        query = take_Command().lower()
        if "wikipedia" in query:
            print("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            print(result)
            speak(result)
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "none" in query:
            continue
        elif "who are you" in query:
            myself()
        elif "how are you" in query:
            how_are_you()
        elif "open file" in query:
            query=query.replace("open file ","")
            find_files(query,"D:\\Adil")
        elif "the time" in query:
            timeNow=datetime.now().strftime("%H:%M:%S")
            speak(timeNow)
        elif "bye jarvis" in query:
            speak("ok, bye my friend. i will meet you next time.")
            exit()
        else:
            chrome=webbrowser.get('chrome')
            chrome.open(f"google.com/?#q={query}")