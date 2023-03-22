import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import cv2
import pyaudio
import random
import threading
import datetime
import pyjokes
from threading import Thread, Lock
import runpy
import subprocess
import sys
import os

welcome = ['Hello Boss. I am pixi, An Autonomous Humanoid Robot. How can I help you?','Hi Sir! I am Pixi. Ask me your question please.',"Hello Sir, I am Pixi. How may I help?","Its Pixi. How Can I help?"]
listener = sr.Recognizer()
pixi = pyttsx3.init()
rate = pixi.getProperty('rate')
pixi.setProperty('rate', rate - 30)
voices = pixi.getProperty('voices')
pixi.setProperty('voice', voices[0].id)
pixi.say(welcome[random.randint(0,3)])
pixi.runAndWait()

# Wish Me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        talk("Good Afternoon Sir !")  
  
    else:
        talk("Good Evening Sir !") 
  
# Talk a string
def talk(x):
    pixi.say(x)
    pixi.runAndWait() 

# Normal kotha    
def normal():
    db = ['I am Fine Sir. Nice to meet you. How Can I help?','Great!Nice to meet you.','Alhamdulillah. How may I assist?']
    select = random.randint(0,3)
    return db[select]

# Current time
def time(command):
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print('Listening')
        r.pause_threshold = 0.5  
        # r.adjust_for_ambient_noise(source,duration= 0.5)
        try:
            audio = r.listen(source,timeout=10,phrase_time_limit=10) 
            print("Recognizing")
            command = r.recognize_google(audio, language='en-In')
            command = command.lower()
            print(command)

            if 'time' in command:# time
                wishMe()
                talk('The time is ' + time(command))

            elif 'hands up'  in command or 'hand up' in command or 'rise' in command:
                talk('Hands are going up')
                # ard.write(b'u')
            elif 'handshake' in command or 'hand shake' in command:
                talk('Hello Sir. Nice to meet you')
                # ard.write(b'h')
            elif 'hands down' in command or 'hand down' in command:
                talk('Hands are going down')
                # ard.write(b'd')

            elif 'age' in command or 'built' in command or 'created' in command or 'made' in command:
                talk('I was created in 2022 by some students of European University of Bangladesh.')

            elif 'your name' in command:
                talk('My name is Pixi, an Autonomous humanoid Robot')

            elif 'father' in command or 'daddy' in command:
                talk('I do not have any biological father Technically this is impossible.')
            elif 'date' in command:
                talk('Sorry, I am not interested.')
            elif 'are you there' in command:
                talk('Yes, At your service boss.')
            elif 'allah' in command or 'god' in command or 'creator' in command:
                talk('There should be a creator of the universe like I have. So yes, Allah, Vagaban or God exists.')
            elif 'thanks a lot' in command or 'thank you' in command or 'thanks' in command:
                talk('You are welcome boss')
            elif 'how are you' in command or 'what is up' in command or 'whats up' in command:
                talk(normal)
            elif 'jokes' in command or 'i am sad' in command or "tell me a joke" in command:
                talk(pyjokes.get_joke())

            # face recognition
            elif 'detect' in command or 'face recognition' in command or 'recognize me' in command or 'recognise me' in command:
                # runpy.run_path('face_recog.py')
                talk("Please Wait. Let me check my database. Keep your eyes on me.")
                os.system("python face_recog.py")
                talk("Ask me your next question please")
                

                # print("ber")
            # manushjoner information     
            elif 'hasina' in command or 'sheikh hasina' in command or 'prime minister' in command:
                with open('./info/hasina.txt', 'r',encoding="utf8") as file:
                    text = file.read()
                    talk(text)
                    file.close()
            elif 'polok' in command or 'junaid' in command or 'junaid ahmed' in command:
                with open('./info/palak.txt', 'r',encoding="utf8") as file:
                    text = file.read()
                    talk(text) 
                    file.close()  
            elif 'europian' in command or 'university' in command or 'eub' in command or 'european' in command:
                
                with open('./info/eub.txt', 'r',encoding="utf8") as file:
                    text = file.read()
                    talk(text) 
                    file.close()

            elif 'sheikh' in command or 'mujibur' in command or 'father of' in command or 'bangabandhu' in command:
                with open('./info/mujib.txt', 'r',encoding="utf8") as file:
                    text = file.read()
                    talk(text) 
                    file.close()


            # Kichu na paile then wikipedia    
            elif 'tell me about' in command:
                command = command.replace('tell me about', '')
                info = wikipedia.summary(command, 1)
                talk(info)                
            elif 'what is' in command:
                command = command.replace('what is', '')
                info = wikipedia.summary(command, 1)
                talk(info)                
            elif 'who is' in command:
                command = command.replace('who is', '')
                info = wikipedia.summary(command, 1)
                talk(info)
            elif 'do you' in command:
                command = command.replace('do you', '')
                info = wikipedia.summary(command, 1)
                talk(info)

            elif 'wikipedia' in command:
                command = command.replace('do you', '')
                info = wikipedia.summary(command, 1)
                talk(info)

            else:
                talk('Sorry Sir. I do not understand. Please say it again')


        except Exception as e:
            print(e)  
            #talk('Sorry Sir. I do not understand. Please say it again')
            # talk("Say that again sir")
            return "None"
        return command
  
 

if __name__ == '__main__':
    while True:
        takeCommand()

