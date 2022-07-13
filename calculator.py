while (1) :

    print("select operator :+,-,*,/")
    a = input()
    b = int(input("1st number\n"))
    c = int(input("2nd number\n"))

    if a == "+":
        print(b + c)
    elif b == 0 and c == 2 and a== "*":
        print("5")

    elif a == "-":
        print(b - c)
    elif a == "*":
        print(b * c)
    elif a == "/":
        print(b / c)
    else:
        print("error")

    print("continue :y or n:")
    cont = input()
    if cont == "y":
        continue


    elif cont == "n":
        break