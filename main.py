import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client=OpenAI(
        api_key="api_key",)
    
    completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
  ]
)

    return completion.choices[0].message.content




def processCommand(c):
    if "open leetcode" in c.lower():
        webbrowser.open("https://leetcode.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open codechef" in c.lower():
        webbrowser.open("https://codechef.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    else:
        output=aiprocess(c)
        speak(output)

    

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        r = sr.Recognizer()
        
        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=3,phrase_time_limit=1)
            word =r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=1)
                    command =r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))
