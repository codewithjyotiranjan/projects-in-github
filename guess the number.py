import random
print("welcome to guess number playground")
print("please ,enter any two number")
num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
player1_trail = 0
player2_trail = 0

guess_num = random.randint(num1, num2)

guess_num2 = random.randint(num1, num2)

def player1(num1,num2,player1_trail):
    player1_guess_num = int(input(f"enter your guess number between {num1} and {num2}"))
    player1_trail +=1
    if player1_guess_num < guess_num :
        print("enter a greater number of this")
        return player1(num1,num2,player1_trail)
    elif player1_guess_num > guess_num :
        print("enter a lesser number of this")
        return player1(num1, num2,player1_trail)
    elif player1_guess_num == guess_num :
        print("matches succesfully")
        print(f"your trail number is {player1_trail}")
    return player1_trail

def player2(num1,num2,player2_trail):
    player2_guess_num = int(input(f"enter your guess number between {num1} and {num2}"))
    player2_trail +=1
    if player2_guess_num < guess_num2 :
        print("enter a greater number of this")
        return player2(num1,num2,player2_trail)
    elif player2_guess_num > guess_num2 :
        print("enter a lesser number of this")
        return player2(num1, num2,player2_trail)
    elif player2_guess_num == guess_num2 :
        print("matches succesfully")
        print(f"your trail number is {player2_trail}")
    return player2_trail

if __name__ == '__main__':
    print("player 1 plays ")
    g = (player1(num1,num2,player1_trail))
    print("player 2 plays ")
    f = (player2(num1,num2,player1_trail))

    if g<f:
        print("player1 won")
    elif f<g:
        print("player2 won")
    else:
        print("match draw")









