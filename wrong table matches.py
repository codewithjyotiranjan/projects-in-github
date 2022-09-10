import random
table_name1 = int(input("enter your no.of table name"))
for k in range(table_name1):
    table_name2 = int(input(f"enter {k+1} table"))
    table_name = table_name2
    list = []

    wrong = random.randint(1, 10)
    for i in range(1,10):
        # print(f"{table_name} * {i+1} = ",table_name * (i+1))

        if i == wrong:
            list.append((table_name * (i))+random.randint(1,10))
        else:
            list.append(table_name * (i))

    list2=[]
    for j in range(1,10):
        list2.append(table_name * (j))

    compare = [result for result in sorted(zip(list2,list)) if result[0]!=result[1]]

    if compare:
        for key ,value in compare:
            print(f"{key} is not matched with {value}")
    else:
        print("none")


