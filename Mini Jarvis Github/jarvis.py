import speech_recognition as sr
import pygame
import os
import uuid  
import edge_tts
import asyncio

from datetime import datetime
import time
import webbrowser
import random
import wikipedia
from googlesearch import search


def speak(text):
    print(text)
    
    filename = f"{uuid.uuid4()}.mp3"
    
    async def generate():
        tts = edge_tts.Communicate(text, voice="hi-IN-MadhurNeural")  
        await tts.save(filename)

    asyncio.run(generate())  

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(filename)


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
            speak("Ja na koi kaam dhandha nahi hai kya")

        elif "time" in command:
            now = datetime.now().strftime("%I:%M %p")
            speak(f"Vese Tera too kharab chal raha hai par abhi {now} Ho raha hai")

        elif "date" in command:
            today = datetime.today().date()
            speak(f"Tu kya karega uska vese aaj {today} hai")


        # Chrome open and close function 
        elif any(word in command for word in ["close", "band", "khatam"]) and "chrome" in command:
            speak("Closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "chrome" in command:
            speak("Chrome chalu kar raha hu dekh le porn lodu")
            os.system("start chrome")

        # Note pad ke liye ye 2 function hai    
        elif any(word in command for word in ["close", "band", "khatam"]) and "notepad" in command:
            speak("Closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "notepad" in command:
            speak("Notepad Chalu kar raha hu tu kya note karega")
            os.system("start notepad")

        # Calculator ke liye 2 function open and close
        elif any(word in command for word in ["close", "band", "khatam"]) and "calculator" in command:
            speak("Eesa kya note karliya tune")
            os.system("taskkill /f /im calc.exe")

        elif "calculator" in command:
            speak("Calculator hi chahiye hoga khud se to kar hi nahi sakta")
            os.system("start calc")

        elif "Google" in command:
            speak("Chalu kar raha hu google")
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            speak("Youtube Dekh Le padana to nahi hai")
            webbrowser.open("https://www.youtube.com")

        elif "whatsapp" in command:
            speak("Kisko message karega tere too dost bhi nahi hai")
            webbrowser.open("https://web.whatsapp.com/")

        elif "super" in command and "dark" in command and "joke" in command:
            super_dark_jokes = ["Tum rightist ho ya feer leftist , vese me to Sexist hu" , 
                                "Bhai me ek book padha raha tha par uska main character mar gaya , uska naam bibal bata raha tha"]

            super_dark_joke = random.choice(super_dark_jokes)
            speak(super_dark_joke)

        elif "dark" in command and "joke" in command:
            dark_jokes = [
                "Indian netaon ko chunav ke liye paise kyun nahi chahiye? Kyunki wade oxygen se bhi saste hain, aur hum dono se hi dam ghut rahe hain.",
                "Dilli ki hawa itni saaf hai, ab PM2.5 ka swad Michelin-star dish jaisa lagta hai.",
                "Bharat ka nyay vyavastha itni tezi se chalta hai, balatkari ko jamanat mil jati hai par peedit ko bandage bhi nahi milta.",
                "Bharat mein sirf sansadon ke ego hi nahi, table ke neeche ka paisa bhi inflated hai.",
                "Humein jansankhya ginne ki zarurat nahi; bas traffic mein fase logon ko gino—wohi number hai.",
                "Bharat mein bhook ki chinta kyun? Sarkaar har chunav mein muft bhashan jo deti hai.",
                "Jaati Bharat mein Wi-Fi jaisi hai—dikhti nahi, par signal kisko milta hai yeh wahi tay karti hai.",
                "Monsoon prakriti ka tarika hai yeh batane ka: naliya bhi ruling party ko vote deti hain.",
                "Bharatiya yuva ke paas itne job options hain—engineer, doctor, ya ‘No Vacancy’ sign ko ghoorna.",
                "Bharat mein hum itne secular hain, hum devtaon ke liye ladte zyada hain, prarthana kam karte hain."
            ]

            dark_joke = random.choice(dark_jokes)
            speak(dark_joke)

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
            speak("Aaj mausam bigda hua hai, ja chadar lele.")


        elif any(kw in command for kw in ["search", "who is", "what is", "bata", "ke baare mein", "kon hai" , "kaun hai" ]):
            for kw in ["search", "who is", "what is", "bata", "ke baare mein", "kya hai" , "kon hai" , "kaun hai"]:
                command = command.replace(kw, "")
            
            query = command.strip()
            
            try:
                summary = wikipedia.summary(query, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Bhai ye to confuse kar raha hai, {query} ke kai matlab ho sakte hain.")
            except wikipedia.exceptions.PageError:
                speak("Mujhe iske baare me kuch nahi mila Wikipedia pe jaake teri girlfriend se pucha.")
            except Exception as e:
                speak("Kuch gadbad ho gaya, dobara try kar bhai agar himmat nahi ho rahi to so ja.")
            

        

        elif "chutiya" in command:
            speak("Tu sirf mere samne hi bol sakta hai lodu")

        elif any(word in command for word in ["stop", "exit", "end", "quit", "goodbye","chup" , "shat" , "Band"]):
            speak("Goodbye sir.")
            break

        else:
            speak("Thoda dhank se Bolde")