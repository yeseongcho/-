import random

 

def func1(n):
    L = []
    for i in range(n):
        L.append([i, False])
    random.shuffle(L)
    return L

 

def func2(L):
    while True:
        try:
            n = int(input("Input a number: "))
            if 0<=n<len(L) and L[n][1]==False:
                return n
            print("Invalid input. Retry.")
        except:
            print("Invalid input. Retry.")

 

L1 = func1(3)

L2 = func1(3)
n = 0
m = 0
while n < len(L1):
    a = func2(L1)
    b = func2(L2)
    print(L1[a][0], L2[b][0])
    if L1[a][0] == L2[b][0]:
        L1[a][1] = True
        L2[b][1] = True
        n += 1
    m += 1

 

print(m)
