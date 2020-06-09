#import the necessary libraries
import pyttsx3 #text to speech
import datetime #to greet user
import speech_recognition as sr #Speech to text
import webbrowser #to open WHO's website

#---Initialize pyttsx3---

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#---We will store the user data in a txt file---

count = 0
User_Data = open("UserData.txt", "a+")

#---To get input from user---

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#---Greet the user---

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning ")
    elif hour>=12 and hour<4:
        speak("Good afternoon User")
    else:
        speak("Good Evening User")

    speak("I am your evaluation bot")


#---takes my command from microphone and gives text---

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry User I could not hear you please restart the program and try again")
        return "None"
        quit()
    return query

if __name__ == "__main__":
    wishMe()
    #Check for symptoms
    while True:
        speak("Do you have a fever?") #Check for fever
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok")
            count = count+1
        else:
            speak("ok")

        speak("Do you feel tired?") #Check for tiredness
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok")
            count = count+1
        else:
            speak("ok")

        speak("Do you have dry cough?") #Check for dry cough
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok")
            count = count+1
        else:
            speak("ok")

        speak("Do you have shortage of breath or other respiratory problems?") #Check for respiratory problems
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok")
            count = count+1
        else:
            speak("ok")

        speak("Do you have  aches, pains, nasal congestion, runny nose, sore throat or diarrhea?") #Check for other symptoms
        query = takeCommand().lower()
        if 'yes' in query:
            speak("ok")
            count = count+1
        else:
            speak("ok")

#---Classify into high, moderate, low or no risk by the number of symptoms an write to a .txt file for keeping a record you can also upload this to a server---

        if count==5:
            speak("You have a high risk of coronavirus, get yourself checked")
            User_Data.write(", High Risk")
            User_Data.close()
            
        elif count==4:
            speak("You have a moderate risk of coronavirus, get yourself checked")
            User_Data.write(", Moderate Risk")
            User_Data.close()

        elif count==3:
            speak("You have a low risk of coronavirus, get yourself checked")
            User_Data.write(", Low Risk")
            User_Data.close()

        elif count<3:
            speak("You seem to be fine, but still keep yourself in quarantine")
            User_Data.write(", Fine")
            User_Data.close()
        speak("Say more info to visit w h o z website or ignore to exit")
        query = takeCommand().lower()
     
        if 'more info' in query:
            webbrowser.open("who.int")
        else:
            speak("Closing program")
            quit()




