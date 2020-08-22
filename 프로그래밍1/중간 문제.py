def f1(a) :
    a = a + 20
    print("a=", a)

def f2(b) :
    a = b + 10
    print("a=", a)

def f3(c) :
    c = a + 30
    print("c=", c)

def f4(d) :
    global a
    a = d + 10
    print("a=", a)

a = 10
f1(a)
f2(a)
f3(a)
f4(a)
print("a=", a)
