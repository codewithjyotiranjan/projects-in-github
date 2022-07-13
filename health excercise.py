import datetime
print(" jyotiranjan mahapatra is a HR manager in a tech company of google "
      "who works 9am to 5pm. ")
import time
from pygame import mixer
while (True):
    def getdate():
        return datetime.datetime.now()
    def func1():
        with open("water drink.txt","a") as b:
            c = "drinking water is done"
            b.write(str([str(getdate())]) + c + "\n" + ":" + "\n")
    def func2():
        with open("eyeexcercise.txt","a") as d:
            e = "drinking water is done"
            d.write(str([str(getdate())]) + e + "\n" + ":" + "\n")
    def func3():
        with open("physicalexcercise.txt","a") as f:
            g = "drinking water is done"
            f.write(str([str(getdate())]) + g + "\n" + ":" + "\n")
    for i in range(3):
        time.sleep(10)
        mixer.init()
        mixer.music.load("C:\\Users\\Dell\\PycharmProjects\\pythonTuts\\Taqdeer BGM.mp3")
        mixer.music.play()
        a = input("type drank to stop the music:\n")
        if a == "drank":
            mixer.music.stop()
            func1()
            time.sleep(10)
        mixer.init()
        mixer.music.load("C:\\Users\Dell\\PycharmProjects\\pythonTuts\\angadai.mp3")
        mixer.music.play()
        h = input("type eyedone to stop music")
        if h == "eyedone":
            mixer.music.stop()
            func2()
            time.sleep(10)
        mixer.init()
        mixer.music.load("C:\\Users\\Dell\\PycharmProjects\\pythonTuts\\Taqdeer Violin.mp3")
        mixer.music.play()
        i = input("type phydone to stop music")
        if i == "phydone":
            mixer.music.stop()
            func3()
            time.sleep(0)
        else:
            print("invalid error")
    break

















































