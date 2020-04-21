import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import smtplib


'''The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech
 recognition and speech synthesis within Windows applications. '''

engine=pyttsx3.init('sapi5')

'''voices gives us all type of voices available in our system'''
voices=engine.getProperty('voices')

'''Below line is used to set the voice according to my need'''
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login('yourmailid', 'password')
    server.sendmail('yourmailid', to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how can I help you")

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


if __name__ == '__main__':
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play video' in query:
            music_dir = 'F:\\redmi 5 hemant backup\\WhatsApp Images+videos\\whatsapp videos'
            videos = os.listdir(music_dir)
            print(videos)
            x=random.randrange(0,len(videos))
            os.startfile(os.path.join(music_dir, videos[x]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mail-id(other)"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        else:
            print("Please speak again")
            speak("Sorry sir!Please speak again.")