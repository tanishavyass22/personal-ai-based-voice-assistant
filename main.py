import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import wikipedia
import os
import time
import sys 
import random
import pyautogui
from time import sleep
from pyautogui import click
import socket
import speedtest
import psutil
import wolframalpha
import smtplib
import re
import requests
from translate import Translator
from languages import languages


NEWS_API = 'YOUR API'
OPENWEATHERMAP = 'YOUR API'
app = wolframalpha.Client("YOUR API")



def sptext():   # for listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("You can speak....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)  # Set timeout to 5 seconds

        try:
            print("Recognizing..")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Can't hear anything, speak loudly")
            textsp("Can't hear anything, speak loudly")

def textsp(x):   #for speaking
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Fix the typo
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    time.sleep(0.5)
    engine.runAndWait()
    
sender_id = "YOUR email"
password = "YOUR PASSWORD"
    
def send_email(recipient, subject, body):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_id, password)
    message = f"From: {sender_id}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
    try:
        s.sendmail(sender_id, recipient, message)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    s.quit()

def check_email(email):
    verifier = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(verifier, email):
        return True
    else:
        return False
    
def get_map():
    textsp("Enter the location you want to search on the map")
    location = input("Enter the location you want to search on the map: ").strip()
    webbrowser.open(f'https://www.google.com/maps/search/{location}')
    
def get_weather():
    city = input("Enter the city name to get the weather forecast: ").strip()
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP}&units=metric').json()
        weather = f'It\'s {response["main"]["temp"]}° Celsius and {response["weather"][0]["main"]}\n' \
               f'But feels like {response["main"]["feels_like"]}° Celsius\n' \
               f'Wind is blowing at {round(response["wind"]["speed"] * 3.6, 2)}km/h\n' \
               f'Visibility is {int(response["visibility"] / 1000)}km'
        return weather
    except requests.exceptions.RequestException:
        return None
    except KeyboardInterrupt:
        return None

def get_news():
    try:
        top_news = ""
        response = requests.get(f'http://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}').json()
        articles = response['articles']
        for article in articles[:10]:
            news_title = re.sub(r'[|-] [A-Za-z0-9 |:.]*', '', article['title']).replace("’", "'") + '\n'
            top_news += news_title
            print(news_title)
        return top_news
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None
    
def take_notes():
    textsp("Please dictate your note.")
    note_text = sptext()
    if note_text:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"note_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(note_text)
        textsp("Note saved successfully.")
        
def send_email(reciever_id, subject, body):
    sender_id = "your email id"
    password = "your password"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_id, password)
    message = "\r\n".join([
        f"From: {sender_id}",
        f"To: {reciever_id}",
        f"Subject: {subject}",
        "",
        f"{body}"
    ])
    try:
        s.sendmail(sender_id, reciever_id, message)
    except smtplib.SMTPRecipientsRefused:
        print("INVALID EMAIL ADDRESS")
        return False
    except smtplib.SMTPException:
        return False
    # terminating the session
    s.quit()
    return True

def check_email(email):
    verifier = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(verifier, email):
        return True
    else:
        return False
    

def print_supported_languages():
    print("Supported languages:")
    for code, name in languages.items():
        print(f"{code}: {name}")

def translate_text():
    print_supported_languages()
    
    source_language = input("Enter source language code: ")
    destination_language = input("Enter destination language code: ")
    text_to_translate = input("Enter text to translate: ")
    
    translator = Translator(from_lang=source_language, to_lang=destination_language)
    translated_text = translator.translate(text_to_translate)
    
    print("\nTranslated text:")
    print(translated_text)
    textsp(translated_text)
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    introduction = "I am Alex. How can I help you today?"
    full_message = f"{greeting}. {introduction}"
    textsp(full_message)


def pass_function(pass_inp):
    password = "helloWorld"
    passss = str(pass_inp)
    
    if passss == password:
        textsp("password match")
        wishMe()
    else:
        textsp("password not matched")
        sys.exit()

if __name__ == '__main__':
    textsp("this particular device is password protected")
    textsp("Please enter the required Password")
    pass_inp = input("Please enter the required Password:")
    pass_function(pass_inp)
    
    exit_flag = False
    while not exit_flag:
        data1 = sptext().lower()

        if "hey alex" in data1:
            while True:
                data1 = sptext().lower()

                if "who created you" in data1:
                    name = "my boss tanisha created me"
                    textsp(name)

                elif "how old are you" in data1:
                    age = "I am 1 day old"
                    textsp(age)

                elif "taani" in data1:
                    app = """Taani, you are an exceptional individual whose dedication and commitment shine through in everything you do. 
                    Your unwavering passion for your work, coupled with your strong work ethic, is truly admirable. 
                    You possess an incredible ability to lead and inspire those around you, fostering an environment of collaboration and growth. 
                    Your attention to detail and innovative thinking make you an invaluable asset to any team. 
                    Not only are you incredibly talented, but your kindness and willingness to support others make you a truly remarkable person. 
                    Your positive attitude and perseverance in the face of challenges are truly inspiring. 
                    Taani, you are an individual whose contributions and impact are greatly appreciated, and they continue to make a meaningful difference in our lives and work."""
                    textsp(app)

                elif "covid" in data1:
                    app = "Common symptoms include fever, cough, and difficulty breathing. However, symptoms can vary and may include loss of taste or smell, fatigue, muscle or body aches, headache, sore throat, congestion, nausea, or diarrhea."
                    textsp(app)

                elif "time" in data1:
                    time_now = datetime.datetime.now().strftime("%I:%M %p")  
                    textsp(time_now)
                     
                elif "day" in data1:
                  day = datetime.datetime.now().strftime("%A")  # %A gives the full day name
                  day_message = f"today is {day}"
                  textsp(day_message)
                
                elif "date" in data1:
                    date_today = datetime.datetime.now().strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
                    date_message = f"Today's date is {date_today}"
                    textsp(date_message)

                
                elif "youtube" in data1:
                    textsp("sure")
                    webbrowser.open("https://www.youtube.com/")
                    textsp("here is youtube")
                    
                elif "arijit songs on youtube" in data1:
                    textsp("sure")
                    webbrowser.open("https://youtu.be/kXHiIxx2atA?si=6KgcDeIyFZVTowa1")

                elif "google" in data1:
                    textsp("sure")
                    webbrowser.open("https://www.google.co.in/")
                    textsp("here is google")
                
                elif "chat" in data1:
                    textsp("sure")
                    webbrowser.open("https://chat.openai.com/?sso=")
                    textsp("here is chatGpt")
                
                elif "open whatsapp" in data1:
                    textsp("sure")
                    webbrowser.open("https://web.whatsapp.com/")
                    textsp("here your whatsapp")
                
                elif "joke" in data1:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    print(joke)
                    textsp(joke)
                    
                elif "wikipedia" in data1:
                    textsp('sure')
                    textsp("searching wikipedia...")
                    data1 = data1.replace("wikipedia", "")
                    results = wikipedia.summary(data1, sentences = 2)
                    print(results)
                    textsp("according to wikipedia")
                    textsp(results)
                
                # elif "open whatsapp" in data1:
                #     textsp('sure')
                #     path = "C:\\Users\\vyast\\OneDrive\\Desktop\\whatsapp"     #if you want to open installed apps
                #     os.startfile(path)
                    
                
                elif "open notepad" in data1:
                    textsp("sure")                                      #if you want to open built in apps
                    os.system("start notepad")
                
                elif "open cmd" in data1:
                    textsp("sure")
                    os.system("start cmd")
                    
                elif "open camera" in data1:
                    textsp("sure")
                    os.system("start microsoft.windows.camera:")
                
                elif "open microsoft word" in data1:
                    textsp("sure")
                    apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
                    os.startfile(apath)
                
                elif "open excel" in data1:
                    textsp("sure")
                    bpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
                    os.startfile(bpath)
                
                elif "open power point" in data1:
                    textsp("sure")
                    bpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
                    os.startfile(bpath)
      
                elif "play music" in data1:
                    textsp("sure")
                    songs = r"C:\Users\vyast\OneDrive\Desktop\songs"
                    listofsongs = os.listdir(songs)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(songs, rd))
                
                elif "turn on bluetooth" in data1:
                    textsp("sure")
                    pyautogui.click(x=1646, y=1050)
                    sleep(1)
                    pyautogui.click(x=1700, y=472)
                    sleep(1)
                    pyautogui.click(x=1854, y=431)
                    
                elif "turn on air" in data1:                #for wifi
                    textsp("sure")
                    pyautogui.click(x=1646, y=1050)
                    sleep(1)
                    pyautogui.click(x=1576, y=476)
                    sleep(1)
                    pyautogui.click(x=1843, y=421)
                
                elif "open files" in data1:
                    textsp("sure")
                    pyautogui.click(x=1086, y=1055)
                
                elif "open edge" in data1:
                    textsp("sure")
                    pyautogui.click(x=1050, y=1040)                 
                    sleep(1)
                    
                elif "save" in data1:
                    pyautogui.hotkey('ctrl', 'shift', 's')
                
                elif "minimise the window" in data1:
                    pyautogui.hotkey('win' , 'd')
                    
                elif "maximize the window" in data1:
                    pyautogui.hotkey('win', 'up')
                    
                elif "open new tab" in data1:
                    pyautogui.hotkey('ctrl', 't')
                
                elif "close this tab" in data1:
                    pyautogui.hotkey('ctrl', 'w')
                
                elif "close all tab" in data1:
                    pyautogui.hotkey('alt', 'f4')
                
                elif "switch tab" in data1:
                    pyautogui.hotkey('ctrl', 'tab')

                elif "select all text" in data1:
                    pyautogui.hotkey('ctrl', 'a')
                    
                elif "copy text" in data1:
                    pyautogui.hotkey('ctrl', 'c')
                    textsp("coppied")

                elif "paste text" in data1:
                     pyautogui.hotkey('ctrl', 'v')
                     textsp("pasted succesfully")

                elif "delete text" in data1:
                     pyautogui.press('delete')
                
                elif "take screenshot" in data1:
                    pyautogui.screenshot('screenshot.png')
                    textsp("done")
                
                elif "create new file" in data1:
                    pyautogui.hotkey('ctrl', 'n')
    
                elif "volume increase" in data1:
                    pyautogui.hotkey('volumeup')
                
                elif "volume decrease" in data1:
                    pyautogui.hotkey('volumedown')
                
                elif "mute" in data1:
                    pyautogui.hotkey('volumemute')
                    
                elif "internet speed" in data1:
                    st = speedtest.Speedtest()
                    download_speed = st.download()
                    upload_speed = st.upload()
                    speed_message = f"My internet speed is Download: {download_speed / 10**6:.2f} Mbps, Upload: {upload_speed / 10**6:.2f} Mbps"
                    print(speed_message)
                    textsp(speed_message)
                
                elif "system statistics" in data1:
                    cpu_usage = psutil.cpu_percent()
                    ram_usage = psutil.virtual_memory().percent
                    disk_usage = psutil.disk_usage('/').percent
                    system_message = f"My system stats: CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}% | Disk Usage: {disk_usage}%"
                    print(system_message)
                    textsp(system_message)
                
                elif "ip address" in data1:
                    host_name = socket.gethostname()
                    ip_address = socket.gethostbyname(host_name)
                    ip_message = f"My IP address is {ip_address}"
                    print(ip_message)
                    textsp(ip_message)
                
                elif "calculate" in data1:
                    textsp("give me the input")
                    query = sptext()
                    # query = input("enter the query")
                    res = app.query(query)
                    print(next(res.results).text)
                    textsp(next(res.results).text)
                    
                elif "take notes" in data1:
                    take_notes()
                
                elif "open map" in data1:
                    get_map()
                    
                elif "translate" in data1:
                    translate_text()
                    
                elif "news" in data1:
                    news = get_news()
                    if news:
                        textsp(news)
                    else:
                        textsp("Failed to fetch news. Please try again later.")
                        
                elif "weather" in data1:
                    weather = get_weather()
                    if weather:
                        textsp(weather)
                    else:
                        textsp("Failed to fetch weather information. Please try again later.")
                
                elif "send email" in data1:
                    textsp("Sure, whom do you want to send the email to?")
                    recipient_email = input("Recipient's Email Address:").lower()

                    if check_email(recipient_email):
                        textsp("What should the subject of the email be?")
                        subject = input("subject:")

                        textsp("What message would you like to include?")
                        body = input("body")

                        textsp("Sending the email now.")
                        if send_email(recipient_email, subject, body):
                            textsp("The email has been sent successfully.")
                        else:
                            textsp("Sorry, I couldn't send the email. Please try again later.")
                        break
                    else:
                        textsp("The email address you provided seems to be invalid. Please try again.")
                        continue
                
                

                elif "Bye" in data1:
                    textsp("Thanks for using me")
                    exit_flag = True  # Set the flag to exit the outer loop
                    break  # Exit the inner loop

                time.sleep(3)  # Delay in the next command

        else:
            print("Thanks")
