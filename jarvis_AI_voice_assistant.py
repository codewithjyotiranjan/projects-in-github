'''
p.s:please do this before run this code.
make this all txt file in your specific drive first.you can make list of all catagory ,but keeping user security,it should be create.
'''
# z1 = make a number txt ,starting from 10 to required number as long the number of email id present and enter  path(directory) here.
# z2 = make a email txt ,  enter all email id that you want to send mailand  enter path(directory) here.
# z3 = make a txt file , enter app password for your respetive personal or bussiness email id and enter  path(directory) here.
# z4 = make a phone number txt and enter your phone number and enter path(directory) here.
# z5 = enter the path for your visual stdio code
# z6 = enter your email whose has a app paswowrd and use to send email
# z7 =  enter your music directory(path)


import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
import random
import smtplib
import re
import time


group_list = {"enter group name":"enter group id"}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',145)
engine.setProperty('volume',1.2)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good morning!")
    elif hour>12 and hour< 18:
        speak("good afternoon!")
    else :
        speak("good evening!")

    speak("i am alexa, please tell me how can i help you")
def takecommand():
    '''it takes microphone input from users'''
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=0.2)
        r.energy_threshold = 2000
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "none"
    return query
def mailfunc():
    import os
    os.chdir(r"z1 ")
    a = os.listdir(r"z1")
    for item in a:
        b = open(item,"r")
        c = b.read()
        name = c.replace("\n"," ").strip().split(",")
        os.chdir(r"z2")
        b = os.listdir(r"z2")
        for item in b:
            d = open(item,"r")
            c = d.read()
            email = c.replace("\n"," ").strip().split(",")
            all = dict(sorted(zip(name,email)))
            return all
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    os.chdir(r"z3")
    a = os.listdir(r"z3")
    for item in a:
        print(item)
        b = open(item, "r")
        c = b.read()
        print(c)
        server.login('z6',c)
    server.sendmail('z6',to,content)
    server.close()
def messagefunc():
    import os
    os.chdir(r"z1")
    a = os.listdir(r"z1")
    for item in a:
        b = open(item, "r+")
        c = b.read()
        name = c.replace("\n", " ").strip().split(",")
        os.chdir(r"z4")
        b = os.listdir(r"z4")
        for item in b:
            d = open(item, "r+")
            c = d.read()
            number = c.replace("\n", " ").strip().split(",")
            all = dict(zip(name, number))
            return all

def text_toperson(number,message):
    import pywhatkit as wp
    wp.sendwhatmsg_instantly(number,message,15,True,3)
def text_togroup(id,message):
    import pywhatkit as wp
    wp.sendwhatmsg_to_group(id,message,15,True,3)

if __name__ == '__main__':
    wishme()
    while(True):
        query = takecommand().lower()
        if 'wikipedia' in query:
            print("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'z7'
            songs = os.listdir(music_dir)
            print(songs)
            total = len(songs)-1
            os.startfile(os.path.join(music_dir,songs[random.randint(0,total)]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is{strtime}")
        elif 'open visual studio code' in query:
            '''you can add by your own choice.'''
            codepath = r"z5"
            os.startfile(os.path.join(codepath))
        elif 'message by email' in query:
            try:
                speak("please say your contact among below ,to whom you want to email")
                s = mailfunc()
                name3 = [name for name in s.keys()]
                name1 = [name.split("@")[0] for name in s.values()]
                name2 = ((re.findall("[a-zA-Z]+", str(name1))))
                for i in range(len(name2)):
                    print(f"{name3[i]}--{name2[i]}")
                to_whom = takecommand()
                to = s[to_whom.replace(" ", "").lower()]
                value = [items for items in s.values()]
                if to in value:
                    print("ok...email got it")
                    speak("what do you want to send")
                    content = takecommand()
                    sendEmail(to,content)
                    speak("Email has been sent!")

                else:
                    speak("sorry,we can not find any email id related to this contacts")
            except Exception  as e:
                speak("sorry my friend jyotiranjan,i am unable to send this email")
        elif 'message to person' in query:
            try:
                speak("choose contacts from below list")
                s = messagefunc()
                name3 = [name for name in s.keys()]
                name1 = [name.split("@")[0] for name in mailfunc().values()]
                name2 = ((re.findall("[a-zA-Z]+", str(name1))))
                for i in range(len(name3)):
                    print(f"{name3[i]}--{name2[i]}")
                to_whom = takecommand()
                num = s[to_whom.replace(" ", "").lower()]
                value = [items for items in s.values()]
                if num in value:
                    print("number got")
                    speak("what you want to send by whatsapp")
                    message = takecommand()
                    text_toperson(num,message)
                    speak("message sent")
                else:
                    speak("i could not find any matches")
            except Exception as e:
                speak("sorry jyotiranjan,i am unable to process your requests")

        elif 'message to group' in query:
            try:
                speak("choose group from below list")
                print([items for items in group_list.keys()])
                select_group = takecommand()
                id = group_list[select_group.replace(" ", "").lower()]
                value = [items for items in group_list.values()]
                if id in value:
                    print("id got")
                    speak("what you want to send by whatsapp")
                    message = takecommand()
                    text_togroup(id,message)
                    speak("message sent")
                else:
                    speak("i could not find any matches")
            except Exception as e:
                speak("sorry jyotiranjan,i am unable to process your requests")
        elif 'the date' in query:
            b = datetime.datetime.now().strftime("%H:%M:%S")
            c = time.asctime().replace(b,"")
            speak(f"sir the time is {c}")
        elif 'your name' in query:
            speak("my name is alexa")
        elif 'who discovered you' in query:
            speak("Mr.Jyotiranjan mahapatra ,and he is also my God , thanks for brought me to this world")
        elif 'about yourself' in query:
            speak("My name is alexa , i am a one kind of robot and you are my commando.I am very delighted to serve your every work as soon as possible ")
        elif 'quit' in query:
            exit()





