def func1(a) :
    global b
    print('b =', b)
    b = b+a
    a = 20
# 여기서 따로 a를 정의한 게 없으니 a는 글로벌 값으로 간주
def func2(f, b) :
    print('a =', a)
    f(a)
    print('a =', a)
    print('b =', b)

def func3() :
    global a
    func2(func1, 10)
    a = 30
    func2(func1, b)

a = 10
b = 20
func3()
print('a =', a)
print('b =', b)




# a = 10
# b = 20
# a = 10
# b = 10
# a = 30
# b = 30
# a = 30
# b = 30
# a = 30
# b = 60
