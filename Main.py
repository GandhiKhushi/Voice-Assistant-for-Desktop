import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import winsound
import datetime
import AppOpener
import openai
import secrets
import wikipedia
from PIL import Image, ImageDraw
from gtts import gTTS
from youtubesearchpython import VideosSearch
import folium
from geopy.geocoders import Nominatim
import requests
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    say("Welcome,How Can I Help You ?")
    print("You Can Use This Are The Function Using Speech")
    print("1) Open Website - Youtube,Wikipedia,Google")
    print("2) Generate Any Type of Password")
    print("3) Generate Any Type of Image")
    print("4) Generate Any Topic Short Introduction")
    print("5) Generate Any Topic Audio")
    print("6) Find Any Topic YouTube Video")
    print("7) Show Today's News")
    print("8) Find Any City Location")
    print("9) Open Any App - Google_Crome,Zoom,Anydesk ,Pycharm")
    print("10) Open Recoding App")
    print("11) Open Whatsapp")
    print("12) Play Music")
    print("For Exit Please Say Thank You")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [
                  ["youtube", "https://www.youtube.com"],
                  ["wikipedia", "https://www.wikipedia.com"],
                  ["google", "https://www.google.com"] ,
         ]
        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                say(f"Opening{site[0]}")
                webbrowser.open(site[1])


        if "Open Music".lower() in query.lower():
            say(f"Play Music")
            os.startfile("C:/Users/User/Downloads/sunshine.mp3")

        if "Today's News".lower() in query.lower():
            webbrowser.open("https://www.aajtak.in/livetv")

        if "Open Whatsapp".lower() in query.lower():
            say("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        if "Open Recoding App".lower() in query.lower():
            say("Opening Bandicam")
            webbrowser.open("https://www.bandicam.com/")

        app = [
            ["crome", r"C:\Program Files\Google\Chrome\Application\chrome.exe"],
            ["zoom", r"C:\Users\User\AppData\Roaming\Zoom\bin\Zoom.exe"],
            ["anydesk",r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"],
            ["pycharm",r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.4\bin\pycharm64.exe"],
        ]
        for apps in app:
            if f"{apps[0]}".lower() in query.lower():
                say(f"Opening {apps[0]}")
                open(f"{app[1]}",match_closest=True)

        if "Create Password".lower() in query.lower():
            say("Please Provides Following Details To Create Password")
            x = int(input("Enter the How Long Password You required ? "))
            password = ''.join(
                secrets.choice("abcdefghijklmnopqrstuvwxyz12313444444ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in
                range(x))
            print(password)

        if "Generate Image".lower() in query.lower():
            say("Please Provides Following Details To Create Image")
            width = int(input("Enter image width: "))
            height = int(input("Enter image height: "))
            color = input("Enter image color: ")
            image = Image.new("RGB", (width, height), color)
            image.save("user_generated_image.png")

        if "Create A Short Introduction".lower() in query.lower():
            say("Please Provides Following Details To Create Introduction")
            topic = input("Enter the topic: ")
            summary = wikipedia.summary(topic, sentences=2)
            print(summary)

        if "Generate Audio".lower() in query.lower():
            say("Please Provides Following Details To Create Audio")
            topic = input("Enter the topic for the audio: ")
            output_file = input("Enter the output filename (include extension, e.g., 'output.mp3'): ")
            tts = gTTS(topic)
            tts.save(output_file)

        if "Find YouTube Video".lower() in query.lower():
            say("Please Provides Following Details To Show Video")
            search_query = input("Enter the topic name: ")
            search = VideosSearch(search_query, limit=0)
            video = search.result()['result'][0]
            print("Found video:", video['link'])

        if "Find Any City Location".lower() in query.lower():
            say("Please Provides Following Details To Find Location")
            city = input("Enter city name: ")
            location = Nominatim(user_agent="my_app").geocode(city)
            map = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)
            folium.Marker(location=[location.latitude, location.longitude], popup=city).add_to(map)
            map_file = "city_ma.html"
            map.save(map_file)
            webbrowser.open(map_file)


        if "Thank You".lower() in query.lower():
            say("Thank You For the Visit")
            exit()
