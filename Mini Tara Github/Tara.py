import speech_recognition as sr
import os
import asyncio

from datetime import datetime
import time
import webbrowser
import random
import wikipedia
from googlesearch import search
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed of speech
engine.setProperty('voice', 'hi')  # Choose Hindi if available

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()
recognizer.pause_threshold = 1
recognizer.energy_threshold = 300

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=10)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""


speak("Tara Activated")


while True:
    command = listen()
    if command == "":
        continue  

    words = command.split()


# Technological Assistant for Research & Automation
    
    if len(words) > 0 and words[0].lower() == "tara":
        command = " ".join(words[1:])

        
        if any(kw in command for kw in ["kaisa", "hello", "kaisa ho"]):
            speak("Hello sir")

        elif "time" in command:
            now = datetime.now().strftime("%I:%M %p")
            speak(now)

        elif "date" in command:
            today = datetime.today().strftime("%d %B %Y")
            speak(f"Today's date is {today}")



        # Chrome open and close function 
        elif any(word in command for word in ["close", "band", "khatam"]) and "chrome" in command:
            speak("Closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "chrome" in command:
            speak("Opening Chrome")
            os.system("start chrome")

        # Note pad ke liye ye 2 function hai    
        elif any(word in command for word in ["close", "band", "khatam"]) and "notepad" in command:
            speak("Closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("start notepad")

        # Calculator ke liye 2 function open and close
        elif any(word in command for word in ["close", "band", "khatam"]) and "calculator" in command:
            speak("Closing Calculator")
            os.system("taskkill /f /im calc.exe")

        elif "calculator" in command:
            speak("Opening Calculator")
            os.system("start calc")

        elif "Google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif "whatsapp" in command:
            speak("Opening Youtube")
            webbrowser.open("https://web.whatsapp.com/")

        elif "joke" in command:
            hindi_jokes = [
                "Tumse na ho payega, chhoti chhoti baaton pe coding chhod deta hai.",
                "Tera IQ to room temperature se bhi kam hai.",
                "Tere jaise to bathroom me bhi Google se puchhte hain — flush kaise karein?",
                "Tu aur teri coding, dono hi incomplete hain."
            ]

            joke = random.choice(hindi_jokes)
            speak(joke)


        elif "rost" in command:
            roasts = [
                "Tu itna lazy hai, hostel ki staircase bhi tujhe dekhkar thak jaati hai!",
                "Tere attendance se toh canteen wale chai ke cup zyada reliable hain.",
                "Tu engineer nahi, ek chalta-firta 'Assignment Copy Kar Do' machine hai.",
                "Tere sapne itne bade hain, par alarm snooze karte waqt sab udd jate hain!",
                "Tu class mein baitha hai ya sirf oxygen waste karne ka world record banane?",
                "Tere CGPA ka haal dekhkar toh mummy bhi bolti hai, 'Beta, mechanic hi ban ja!'",
                "Tu backlogs ko collect karta hai jaise koi Pokémon cards jama karta hai!"
            ]

            roast = random.choice(roasts)
            speak(roast)

        elif "weather" in command:
            speak("I do not currently have API for it.")


        elif any(kw in command for kw in ["search", "who is", "what is", "bata", "ke baare mein", "kon hai" , "kaun hai" ]):
            for kw in ["search", "who is", "what is", "bata", "ke baare mein", "kya hai" , "kon hai" , "kaun hai"]:
                command = command.replace(kw, "")
            
            query = command.strip()
            
            try:
                summary = wikipedia.summary(query, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"It has more than 1 meaning")
            except wikipedia.exceptions.PageError:
                speak("I do not know anything about it.")
            except Exception as e:
                speak("Error came up")
            


        elif any(word in command for word in ["stop", "exit", "end", "quit", "goodbye","chup" , "shat" , "Band"]):
            speak("Goodbye sir.")
            break

        else:
            speak("I am not able to hear properly")
