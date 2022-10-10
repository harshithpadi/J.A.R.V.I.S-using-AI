import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import smtplib
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import psutil
import pandas as pd
import mouse
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
#from pynput.keyboard import Key, Controller
import win32gui, win32con
import pyautogui
import re
import random
import requests
from bs4 import BeautifulSoup
import urllib.request
import shutil
import tempfile

R_EATING = "I don't like eating anything because I'm a robot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
def talk(text):
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('padiharshith@gmail.com', 'GAIL1234')
    server.sendmail('padiharshith@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    speak("please tell your password before accessing jarvis")
    content5 = takeCommand()

    if "47" in content5:
        speak("Activating jarvis")
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results) 
                speak(results)
            
            #elif "search" in query:
                #speak("What would you like to search?")
                #content3 = takeCommand()
                #pyautogui.hostkey('winleft')
                #mouse.move(-1079,1079, absolute=False, duration=0.6)
                #mouse.on_click(lambda: print("Right Button clicked."))
                #mouse.on_click(lambda: print("Left Bsclicked."))
                #pyautogui.write('sem', interval = 0.9)
                #pyautogui.typewrite("sem\n")
            
            elif "stands" in query:
                speak("jarvis stands for Just A Rather Very Intelligent System (J.A.R.V.I.S.) ")
                
            elif "notepad" in query:
                speak("opening notepad")
                npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\Accessories\\Notepad"
                os.startfile(npath)
                window = win32gui.GetForegroundWindow()
                win32gui.MoveWindow(window, 0, 0, 1440, 900, True)
                
            elif "command prompt" in query:
                speak("opening command prompt")
                os.system("start cmd")
                
            elif "where i am" in query or "where we are" in query:
                speak("wait sir,let me check")
                try:
                     ipAdd = requests.get('https://api.ipify.org').text
                     print(ipAdd)
                     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                     data = json.loads(url.read().decode())
                     country = data['country_name']
                     city = data['city']
                     speak('According to me we are in '+city+' city of '+country+' country')
                        
                except:
                    speak('Sorry sir, some of our monitoring systems are not working properly causing me unable to find our location')
            
            elif "close" in query:
                speak("what would you like to close?")
                content10 = takeCommand()
                speak("okay sir,closing")
                if "notepad" in content10:
                    speak("notepad")
                    for process in (process for process in psutil.process_iter() if process.name()=="notepad.exe"):
                        process.kill()
                elif "command promt" in content10:
                    speak("command promt")
                    for process in (process for process in psutil.process_iter() if process.name()== "cmd.exe"):
                        process.kill()
                      
            elif "describe" in query:
                print("from describe statement")
                person = query.replace("discribe","")
                info = wikipedia.summary(person,2)
                print(info)
                talk(info)
                
            elif "open whatsapp" in query:
                speak("To whom you would like to message?")
                content2 = takeCommand()
                print(content2)
                if "varun" in content2:
                    num ="+91 97035 85233"
                num ="+91 97035 85233"
                speak("What should I send?")
                content1 = takeCommand()
                T1 = int(datetime.datetime.now().strftime("%H"))
                T2 = int(datetime.datetime.now().strftime("%M"))   
                pywhatkit.sendwhatmsg(num,content1,T1,T2+1)
                mouse.move(1798, 969, absolute=False, duration=0.2)
                mouse.on_click(lambda: print("Left Button clicked."))
            
            elif "play" in query:
                song1 = query.replace("play","")
                talk("playing"+song1)
                pywhatkit.playonyt(song1)
                
            elif "map" in query:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open('https://www.google.com/search?q='+format(query))
                
            elif 'open youtube' in query:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                speak("What would you like to listen?")
                content = takeCommand()
                song = content.replace("play","")
                talk("playing"+song)
                pywhatkit.playonyt(song)   
                
            elif 'close' in query:
                pyautogui.hostkey('ctrl','w')
                
            elif 'open google' in query:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                try:
                    speak("What would you like to search?")
                    content = takeCommand()   
                    webbrowser.get(chrome_path).open('https://www.google.com/search?q='+format(content))
                    speak("searching")
                except Exception as e:
                    print(e)
                    speak("Sorry try again")    
                
            elif "camera" in query:
                cap = cv2.VideoCapture(0)
                # Check if the webcam is opened correctly
                if not cap.isOpened():
                    raise IOError("Cannot open webcam")
        
                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx=3, fy=2, interpolation=cv2.INTER_AREA)
                    cv2.imshow('Input', frame)
        
                    c = cv2.waitKey(1)
                    if c == 27:
                        break
        
                cap.release()
                cv2.destroyAllWindows()
                    
            elif "joke" in query:
                print("jokes ")
                talk(pyjokes.get_joke())
            elif "hand" in query:
                # initialize mediapipe
                mpHands = mp.solutions.hands
                hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
                mpDraw = mp.solutions.drawing_utils
        
                # Load the gesture recognizer model
                model = load_model('mp_hand_gesture')
        
                # Load class names
                f = open('gesture.names', 'r')
                classNames = f.read().split('\n')
                f.close()
                print(classNames)
        
        
                # Initialize the webcam
                cap1 = cv2.VideoCapture(0)
        
                while True:
                    # Read each frame from the webcam
                    _, frame1 = cap1.read()
        
                    xx, y, c = frame1.shape
        
                    # Flip the frame vertically
                    frame1 = cv2.flip(frame, 1)
                    framergb = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        
                    # Get hand landmark prediction
                    result = hands.process(framergb)
        
                    # print(result)
        
                    className = ''
        
                    # post process the result
                    if result.multi_hand_landmarks:
                        landmarks = []
                        for handslms in result.multi_hand_landmarks:
                            for lm in handslms.landmark:
                                # print(id, lm)
                                lmx = int(lm.xx * xx)
                                lmy = int(lm.y * y)
        
                                landmarks.append([lmx, lmy])
        
                            # Drawing landmarks on frames
                            mpDraw.draw_landmarks(frame1, handslms, mpHands.HAND_CONNECTIONS)
        
                            # Predict gesture
                            prediction = model.predict([landmarks])
                            # print(prediction)
                            classID = np.argmax(prediction)
                            className = classNames[classID]
        
                    # show the prediction on the frame
                    cv2.putText(frame1, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                                   1, (0,0,255), 2, cv2.LINE_AA)
        
                    # Show the final output
                    cv2.imshow("Output", frame1) 
        
                    if cv2.waitKey(1) == ord('q'):
                        break
        
                # release the webcam and destroy all active windows
                cap1.release()
                cv2.destroyAllWindows()    

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
    
            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "padiharshith@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    speak("Sorry my friend harshith. I am not able to send this email")    
    
            elif 'who' in query:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open('https://www.google.com/search?q='+format(query))
             
            elif 'explain' in query:
                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open('https://www.google.com/search?q='+format(query))
                
            elif "quit" in query:
                speak('thanks for using me sir,have a good day')
                sys.exit()
                
            elif "shutdown" in query:
                speak("turning off syteam")
                os.system("shutdown /s /t 5")
                
            elif "sleep" in query:
                speak("ok sir,systeam going to sleep")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
                
            else:
                def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
                    message_certainty = 0
                    has_required_words = True
                
                    # Counts how many words are present in each predefined message
                    for word in user_message:
                        if word in recognised_words:
                            message_certainty += 1
                
                    # Calculates the percent of recognised words in a user message
                    percentage = float(message_certainty) / float(len(recognised_words))
                
                    # Checks that the required words are in the string
                    for word in required_words:
                        if word not in user_message:
                            has_required_words = False
                            break
                
                    # Must either have the required words, or be a single response
                    if has_required_words or single_response:
                        return int(percentage * 100)
                    else:
                        return 0
                
                
                def check_all_messages(message):
                    highest_prob_list = {}
                
                    # Simplifies response creation / adds it to the dict
                    def response(bot_response, list_of_words, single_response=False, required_words=[]):
                        nonlocal highest_prob_list
                        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
                
                    # Responses -------------------------------------------------------------------------------------------------------
                    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
                    response('See you!', ['bye', 'goodbye'], single_response=True)
                    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
                    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
                    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
                
                    # Longer responses
                    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
                    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
                
                    best_match = max(highest_prob_list, key=highest_prob_list.get)
                    # print(highest_prob_list)
                    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
                
                    return unknown() if highest_prob_list[best_match] < 1 else best_match
                
                
                # Used to get the response
                def get_response(user_input):
                    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
                    response = check_all_messages(split_message)
                    return response
                
                
                # Testing the response system
                
                speak(get_response(query))
    else:
        speak("access denied")