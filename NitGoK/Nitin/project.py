import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time
import sys
# from ecapture import ecapture as ec
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer ,QTime ,QDate, Qt
from PyQt5.QtGui import QMovie 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_jarvis

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

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskexecution()

    def takeCommand(self):

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
            query=query.lower()
            return query
            
        except Exception as e:
            print(e) 
            print("Say that again please...")
            return "None"
        

    def taskexecution(self):
        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in self.query:
                music_dir = 'D:\songs\punjabi'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "E:\web_devlopment\Bootstrap\project.py"
                os.startfile(codePath)

            elif 'exit' in self.query or 'bye' in self.query:
                name='meet milan and bimal'
                print("ok then by .."+name)
                speak("ok bye"+name)
                break

            elif 'who are you' in self.query or 'what can you do' in self.query:
                speak('I am jarvis version 2 point O your personal assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'In different cities')


            elif "who made you" in self.query or "who created you" in self.query or "who discovered you" in self.query:
                speak("I was built by Bimal ,Meet and Milan")
                print("I was built by Bimal ,Meet and Milan")

            elif 'search'  in self.query:
                self.query = self.query.replace("search", "")
                webbrowser.open_new_tab(self.query)
                time.sleep(5)
            
            elif 'news' in self.query:
                news = webbrowser.open_new_tab("https://sandesh.com")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif "say" in self.query:
                self.query=self.query.replace("say","")
                self.query=self.query.replace("to","")
                print(self.query)
                speak(self.query)
                speak("i am jarvis")

startExecution =MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_jarvis()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)       
        self.ui.pushButton_2.clicked.connect(self.close)       
    
    def startTask(self):
        self.ui.movie=QtGui.QMovie("iron man.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie=QtGui.QMovie("intiating.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timer=QTimer(self)
        # timer.start(1000)     
        startExecution.start()

app=QApplication(sys.argv)
project= Main()
project.show()
exit(app.exec_())