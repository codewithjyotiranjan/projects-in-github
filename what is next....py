b = int(input("enter how many number you want to take"))
a = []
for i in range(b):
    c = int(input(f"enter {i+1} number is:-"))
    a.append(c)
def next_palidrone(a):
    if a>=10 :
        while not is_palidrone(a):
            a += 1
            return next_palidrone(a)
        while is_palidrone(a):
            return a
    else:
        print("please enter two digit number")
        return a

def is_palidrone(a):
    p = str(a)
    for i in range(len(p)):
        if p == p[::-1]:
            return p
if __name__ == '__main__':
    for item in a:
        # print(item)
        if item<10:
            print("please enter two digit number with greater than 9")
        else:
            print(f"The palidromic number for  {item} is ",next_palidrone(item))
