# fill the details in between to execute the code
import  pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good morning")
    else:
        speak("good evening")
    speak("I am jarvis sir. Please tell me how may i help you")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please....")
        return "none"
    return query 
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-name@gmail.com','password')
    server.sendmail('your-name@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia ....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open code' in query:
            codePath="your code path"
            os.startfile(codePath)
        elif 'email to someone' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="receiver-name@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my someone bhai.I am not able to send this email")
