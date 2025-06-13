import tkinter as tk
from tkinter import StringVar, Label, Button
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import pyjokes
import pywhatkit
from newsapi import NewsApiClient
import json

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Use default voice
engine.setProperty('rate', 150)

# Initialize Tkinter window
window = tk.Tk()
window.title('Faith AI Assistant')
window.configure(bg='white')

# Define StringVars for displaying output
var = StringVar()
var1 = StringVar()
var.set('Welcome!')

# Define functions

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Wish the user based on the current time."""
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    speak(greeting)
    var.set(greeting + " How can I help you today?")

def take_command():
    """Capture and recognize user's voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language='en')
        var1.set(query)
        window.update()
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return None

def play():
    """Handle user's voice commands."""
    while True:
        query = take_command()
        if query:
            # Exit condition
            if 'bye' in query:
                var.set("Goodbye!")
                speak("Goodbye!")
                break
            
            # Additional commands (e.g., Wikipedia search, playing music, jokes, etc.)
            elif 'joke' in query:
                speak(pyjokes.get_joke())
            
            elif 'play music' in query:
                speak("What song would you like me to play?")
                song_query = take_command()
                if song_query:
                    pywhatkit.playonyt(song_query)
            
            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            
            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            
            elif 'news' in query:
                speak("Fetching latest news.")
                news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
                response = requests.get(news_url)
                if response.status_code == 200:
                    news_data = response.json()
                    headlines = [article['title'] for article in news_data['articles'][:5]]
                    for headline in headlines:
                        speak(headline)
                else:
                    speak("Could not fetch news. Please check your network connection.")
            
            # Add more voice command handling here
            
            else:
                speak("Sorry, I don't understand the command. Can you please repeat?")

# Define GUI elements

output_label = Label(window, textvariable=var, bg='white')
output_label.pack(pady=5)
input_label = Label(window, textvariable=var1, bg='lightblue')
input_label.pack(pady=5)
btn_wish = Button(window, text='WISH ME', width=20, command=wish_me, bg='white')
btn_wish.pack(pady=5)
btn_talk = Button(window, text='TALK', width=20, command=play, bg='white')
btn_talk.pack(pady=5)
btn_exit = Button(window, text='EXIT', width=20, command=window.quit, bg='white')
btn_exit.pack(pady=5)

window.mainloop()
