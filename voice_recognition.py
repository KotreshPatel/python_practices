import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os 
import webbrowser


engine = pyttsx3.init('sapi5') # Microsoft sapi5
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=16:
        speak("Good Noon Sir")
    else:
        speak("Good Evening Sir")
    speak("I'm Hal Sir.Please tell me how may I help you")

def takeCommand():
    # It takes Microphone Input and Provides the string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query    
    

if __name__ == "__main__":
    wishme()
    #speak()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on Query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play video' in query:
            new_dir = 'C:\\Users\\kotrgk\\Videos'
            video = os.listdir(new_dir)
            print(video)
            os.startfile(os.path.join(new_dir,video[0]))
        elif 'the time' in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {t}")
        elif 'open atom' in query:
            p = "C:\\Users\\kotrgk\\AppData\\Local\\atom\\atom.exe"
            os.startfile(p)
        elif '
            
            
            
        
