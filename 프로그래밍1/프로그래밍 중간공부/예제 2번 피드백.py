for i in range(5) :
    if i == 0 or i == 4 :
        print("*" * 5)
    else :
        print("*" + " "*3 +"*")

# a = i+5 ......... for문 밖에서 정의하는지 안에서 정의하는지 유념해서 보자!
for i in range(5) :
    if i+5 == 5 or i+5 == 9 :
        print(" " *5 + "*"*5)
    else :
        print(" "*5 + "*" + " "*3 +"*")
