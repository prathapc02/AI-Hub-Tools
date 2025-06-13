from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import wolframalpha
import winshell
import psutil
import pyjokes
import pywhatkit
from PIL import Image
import time
import pyperclip
import pyautogui
import requests
from newsapi import *
import json


Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
Engine.setProperty('voice', voices[-1].id)
Engine.setProperty('rate', 200)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir") #Name - your Name
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("My name is Faith How can i help you today")

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 500
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
            var.set("Listening...")
            window.update()
            print("Listening...")
            audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'bye' in query or 'thanks mate' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            exit()
            break
                                                                                             #wikipedia
        elif 'wiki' in query:
            if 'open wikipedia' in query:
                webbrowser.open_new_tab("http://www.wikipedia.com")
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')
                                                                                  #google search
        elif 'search on google' in query:
            speak("what do you want to search on google?")
            record = takeCommand()
            speak('according to google')
            url='www.google.com/search?q=' + record
            webbrowser.get().open(url)

        elif 'open calculator' in query:
            speak("Opening calculator.")
            os.system("calc")


        elif 'open command prompt' in query:
            speak("Opening Command Prompt.")
            os.system("cmd")

        elif 'take screenshot' in query:
            speak("Taking screenshot.")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")

        elif 'search for' in query:
            query = query.replace("search for", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")

        elif 'play video' in query:
            speak("Sure, what video would you like me to play?")
            video_name = takeCommand()
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={video_name}")

        elif 'define' in query:
            query = query.replace("define", "")
            webbrowser.open_new_tab(f"https://www.dictionary.com/browse/{query}")



        elif 'play tamil music' in query:
            speak("Playing music from the Tamil.")
            music_link = "https://youtu.be/ZdMZ40GSVmc?si=2C3PU53PETggQWos"
            webbrowser.open(music_link)

                                                                                  #ONLY_map
        elif 'open google map' in query:
            speak("what is the location?")
            map= takeCommand()
            speak('Opening google  map...wait a sec')
            link='https://www.google.com/maps/place/' + map
            webbrowser.get().open(link)
                                                                                 #open website
        elif 'open website' in query:
            speak("tell me your website URL")
            website= takeCommand()
            speak('opening your given website')
            web= website
            webbrowser.get().open(web)
                                                                                  #open google website

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open_new_tab("http://www.youtube.com")


        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open_new_tab("http://www.google.com")

        elif 'open gmail' in query:
            var.set('opening mail')
            window.update()
            speak('opening mail')
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

                                                                                             #play songs in youtube
        elif ('play songs' in query ):
            speak("what song would you like me to play on youtube?")
            song = takeCommand()
            speak("playing song" +song)
            pywhatkit.playonyt(song)

                                                                                            #jokes
        elif 'tell me a joke' in query:

            speak(pyjokes.get_joke())

                                                                                            #talks
        elif 'hello' in query:
            var.set('Greetings')
            window.update()
            speak("Greetings")


        elif "what's the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif "what is today's date" in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks for you sir like open websites,applications ,write notes,play music,jokes etc ')
            window.update()
            speak('I can do multiple tasks for you sir like open websites,applications ,write notes,play music,jokes etc')

        elif 'old' in query:
            var.set("Old enough to know better")
            window.update()
            speak("Old enough to know better")


        elif 'what is your name ' in query:
            var.set("Myself Faith Sir")
            window.update()
            speak('Myself Faith sir')

        elif 'who created you' in query:
            var.set('My Creators is Sakthi')
            window.update()
            speak('My Creators is Sakthi')


        elif "who am i" in query:

            speak("An evolving species")

        elif 'what is love' in query:

            speak("It is 7th sense that destroy all other senses")


        elif "give me direction" in query:
            var.set("opening website")
            speak("opening website")
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(
                executable_path="D:\\project\\chromedriver\\chromedriver.exe",
                options=options)
            driver.minimize_window()
            driver.get("https://www.google.co.in/maps/")
            user1= driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
            user1.click()
            var.set("tell me starting point")
            speak("tell me starting point")
            sp=takeCommand()
            string1=sp
            var.set("tell me your destination")
            speak("tell me you destination")
            sd=takeCommand()
            string2=sd
            driver.maximize_window()
            sp_box=driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
            sp_box.send_keys(string1)
            sd_box=driver.find_element_by_xpath('//*[@id="sb_ifc52"]/input')
            sd_box.send_keys(string2)
            button=driver.find_element_by_xpath('//*[@id="directions-searchbox-1"]/button[1]')
            button.click()

        elif "news" in query:

            url = ('https://newsapi.org/v2/top-headlines?'
                   'country=in&'
                   'apiKey=c43f5622a51544f4958de27646d0e7a9')
            try:
                response = requests.get(url)
            except:
                speak("please check your connection")
            count = 3

            news = json.loads(response.text)
            for new in news["articles"]:
                if count>0:
                    n1=0
                    n2=0
                    n1=str(new["title"])
                    var.set(n1)
                    window.update()
                    speak(str(new["title"]))

                    n2=print(str(new["description"]))
                    var.set(n2)

                    speak(str(new["description"]))
                    count-=1

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute the volume" in query:
            pyautogui.press("volumemute")

        elif "unmute the volume" in query:
            pyautogui.press("volumeunmute")


            
                                                                      #WRITE A NOTE
        elif "write a note" in query:

            speak("What should i write, sir")

            note = takeCommand()

            file = open('note.txt', 'w')
            file.write(note)
            file.close()
            speak("Note created"+ note)
                                                                       #SHOW NOTE COMMAND
        elif "read note" in query:

            speak("Reading Notes")

            file = open("aihub.txt", "r").read()

            var.set(file)

            speak("You created this note" + file)


                                                                    #WINDOWS FUNCTION
        
        elif 'lock my device' in query:

            speak("locking the device")

            ctypes.windll.user32.LockWorkStation()

        elif 'empty recycle bin' in query:

            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

            speak("Recycle Bin Recycled")

        elif 'shutdown system' in query:

            speak("Hold On a Sec ! Your system is on its way to shut down")

            os.system("shutdown /s /t 1") 

        elif 'restart system' in query:

            speak("Hold On a Sec ! Your system is on its way to restart")

            os.system("shutdown /r /t 1")


                                                                      #OPEN PRESENTING FILES
        elif 'open your ppt' in query:

            speak("opening Power Point presentation")

            power = r"C:\Users\ASUS-2024\Downloads\ai-hub.pptx"

            os.startfile(power)



def update(ind):
    frame = frames[(ind)%50]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='VAME.gif',format = 'gif -index %i' %(i)) for i in range(50)]
window.title('Faith')
window.configure(bg = '#111124')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)


btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#FFFFFF')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'TALK',width = 20,command = play, bg = '#FFFFFF')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#FFFFFF')
btn2.config(font=("Courier", 12))
btn2.pack()
window.mainloop()
                                       #END#
