def getdate():
    import datetime
    return datetime.datetime.now()



print(" it is designed for your health and dieting purpose")



a =int(input(" do you want to lock or add\n:press 1 for lock\n  press 2 for add\n"))
b =int(input("it is for whom\n:-press 3 for maun\npress4 for smita\npress 5 for sona\n"))
c =int(input(" do you want for excercise or food\n:-press 6 for excercise\npress 7 for food\n"))

if a == 2 and b == 3 and c == 6:
    with open("maun excercise.txt", "a") as d:
        e = input("what excercise you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")
elif a==2 and b == 4 and c ==6 :
    with open("smita excercise.txt", "a") as d:
        e = input("what excercise you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")
elif a == 2 and b == 5 and c == 6 :
    with open("sona excercise.txt", "a") as d:
        e= input("what excercise you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")

elif a == 2 and b == 3 and c == 7:
    with open("maun food.txt", "a") as d:
        e = input("what food you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")


elif a == 2 and b == 4 and c == 7:
    with open("smita food.txt", "a") as d:
        e = input("what food you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")

elif a == 2 and b == 5 and c == 7:
    with open("sona food.txt", "a") as d:
        e = input("what food you will add ")
        d.write(str([str(getdate())]) + e + ":" + "\n")


elif a == 1 and b == 3 and c == 7 :
    with open("maun food .txt", "r") as d:
        print(d.read())
elif a == 1 and b == 4 and c == 7 :
    with open("smita food.txt", "r") as d:
        print(d.read())
elif a == 1 and b == 5 and c == 7 :
    with open("sona food.txt", "r") as d:
        print(d.read())

elif a == 1 and b == 3 and c == 6 :
    with open("maun excercise.txt", "r") as d:
        print(d.read())
elif a == 1 and b == 4 and c == 6:
    with open("smita excercise.txt", "r") as d:
        print(d.read())
elif a == 1 and b == 5 and c == 6:
    with open("sona excercise.txt", "r") as d:
        for i in d :
            print(i,end=" ")











































