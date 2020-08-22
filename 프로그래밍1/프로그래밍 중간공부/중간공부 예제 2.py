for i in range(5) :
    if i == 0 :
        print("*"*5)
    elif i == 1 or i == 2 or i == 3 :
        print("*" + " "*3 + "*")
    else :
        print("*"*5)

for a in range(5) :
    if a == 0 :
        print(" "*5 + "*"*5)
    elif a == 1 or a == 2 or a == 3 :
        print(" "*5 + "*" + " "*3 + "*")
    else :
        print(" "*5 + "*"*5)
