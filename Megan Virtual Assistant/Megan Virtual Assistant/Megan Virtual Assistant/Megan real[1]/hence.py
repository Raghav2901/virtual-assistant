import pyttsx3 
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import requests
import pyautogui
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

def getWeather(city, speed=200):
    apiKey = "c9ff620c39e8b1456a3a9955bf276b59"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        speak(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.",speed=speed)
    else:
        speak("Sorry, I could not find the weather for that city.")  


def get_latest_news():
    try:
        news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=22ddd806b3fd47c3a3daa061a6bd5f09"
        news_request = requests.get(news_url)
        news_data = news_request.json()
        news_articles = news_data["articles"]
        speak("Here are some top news headlines")
        for article in news_articles:
            speak(article["title"])
            command = takeCommand().lower()
            if "stop news" in command:
                speak("Stopping the latest news.")
                return
        speak("End of news headlines.")
    except Exception as e:
        print(f"Error getting latest news: {e}")
        speak("Sorry, I could not fetch the latest news.")


def getCurrentTime():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S") # Get the current time in the format HH:MM:SS
    date = now.strftime("%d-%m-%Y") # Get the current date in the format DD-MM-YYYY
    day = now.strftime("%A") # Get the name of the current day (e.g. Monday, Tuesday, etc.)
    result = f"The time is {time} on {day}, {date}."
    return result 

def openApplication(application):
    try:
        os.startfile(application)
        print(f"{application} opened successfully.")
    except Exception as e:
        print(f"Error opening {application}: {e}")

def closeApplication(application):
    try:
        os.system(f"TASKKILL /F /IM {application}")
        print(f"{application} closed successfully.")
    except Exception as e:
        print(f"Error closing {application}: {e}")

def takeScreenshot():
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
        screenshotName = f"screenshot_{timestamp}.png"
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshotName)
            print(f"Screenshot saved as {screenshotName}")
        except Exception as e:
            print(f"Error taking screenshot: {e}")           

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio,speed=200):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed) 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Megan, your virtual assistant. Please tell me how can I help you.") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query.lower()

if __name__== "__main__":
    wishMe()
    
    while True:

        query = takeCommand().lower()
        
        if 'open google' in query:
            speak("What would you like to search on google sir?")
            search_query=takeCommand().lower()
            speak("Here is your result sir")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'close google' in query:
            speak("Closing google sir")
            closeApplication("chrome.exe")       
        
        elif 'take a screenshot' in query:
             takeScreenshot()    

        elif 'what is time now' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir the time is {strTime}")
                   
        elif 'open instagram' in query:
            speak("Opening Instagram sir")
            webbrowser.open("instagram.com")

        elif 'close instagram' in query:
            speak("Closing instagram sir")
            closeApplication("msedge.exe")   
     
        elif 'open whatsapp' in query:
            speak("Opening whatsapp sir")
            webbrowser.open("web.whatsapp.com")

        elif 'close whatsapp' in query:
            speak("Closing whatsapp sir")
            closeApplication("mseddge.exe")   
    

        elif 'open youtube' in query:
            speak("Opening youtube sir")
            webbrowser.open("youtube.com")
    
    
        elif 'close youtube' in query:
            speak("Closing youtube sir")
            closeApplication("msedge.exe")   
    

        elif 'open gmail' in query:
            speak("Opening Gmail sir")
            webbrowser.open("https://mail.google.com/")
            
        elif 'close gmail' in query:
            speak("Closing gmail sir")
            closeApplication("msedge.exe")   
            
        elif 'turn off' in query:
              speak("OK Sir Have a nice day.") 
              os.system("taskkill /f /im msedge.exe") 
              os.system("taskkill /f /im chrome.exe")
              break

        elif 'your processor id' in query:
            speak("No, please mind your own business sir.")
  
        elif 'open chrome' in query:
             speak("Opening chrome sir")
             openApplication("chrome.exe")

        elif 'close chrome' in query:
            speak("Closing chrome sir")
            closeApplication("chrome.exe")   
    
        elif 'about raghav' in query:
            speak("Raghav is a 21 year old boy, and his hobby is to play games like survivor and action games. He also has a little bit of interest in studies, but not too much.")
        
        elif 'hi megan' in query or 'hello megan' in query or 'hey megan' in query:
            speak("Hello sir, please let me know your command.")
            

        elif 'i love you megan' in query:
            speak("I love you too sir.")
            

        elif 'play music' in query:
          speak("Playing music sir.")
          music_dir="C:\\Users\\Lenovo\\Desktop\\Megan Virtual Assistant\\Music"
          songs = os.listdir(music_dir)
          print(songs)
          current_song_index = 0
          os.startfile(os.path.join(music_dir, songs[current_song_index]))

          playing_music = True

          while playing_music:
               command = takeCommand().lower()
               if 'next music' in command:
                  current_song_index = (current_song_index + 1) % len(songs)
                  os.startfile(os.path.join(music_dir, songs[current_song_index]))
               elif 'stop music' in command:
                  os.system("taskkill /f /im music.ui.exe")
                  playing_music = False


        elif 'tell me the weather' in query:
            speak("Please tell me the name of the city.")
            city=takeCommand().lower()
            getWeather(city) 

        elif 'latest news' in query:
            get_latest_news()  
            while True:
                stop_query = takeCommand().lower()
                if 'stop news' in stop_query:
                    speak("Stopping the latest news.")
                    break  
            
        elif 'open spotify' in query:
            speak("Sure sir, which song would you like me to play on Spotify?")
            song = takeCommand().lower()
            webbrowser.open(f"https://open.spotify.com/search/{song}") 
            # Authenticate with the Spotify API using OAuth
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

           # Search for a song
            results = sp.search(q='track:Time artist:Pink Floyd', type='track')

           # Get the first track
            track = results['tracks']['items'][0]

           # Play the track
            sp.start_playback(uris=[track['uri']])

        # else:
            # speak("I'm sorry sir, I didn't understand your command. Could you please repeat") 
