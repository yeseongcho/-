""" 컴퓨터는 모든지 Top-Dowm식으로 해석한다!"""
def test() :
    print(a) # ?, a라는게 있나보네.. 
    a = 77 # a는 Local variance구나! 엥 그러면 위에 것은 대체 뭐지? 선언되기도 전에..
    print(a)
    # 함수가 끝나는 순간 a는 파괴된다.
a = 99 # a는 Global variance구나!
test()
def test() :
    a = 77 # a는 Local variance구나!
    print(a)
    # 함수가 끝나는 순간 a는 파괴된다!
a = 99
test()
def test() :
    print(a) # a라는게 있나보네... local이면 먼저 쓰이면 안되는데..

a = 99 # 아! a가 Global이구나!
test()
def test() :
    global a # a라는 건 앞으로 global하게 할거야!
    print(a) # global a값을 가져와!
    a = 77 # local variance a를 선언했지만 이건 이제 global하게 간주할거야!
    print(a) 

a = 99
test() # 이 값에 의해 a는 77이 됬어! 왜냐? global a에 의해
print(a) # 77이 산출되겠지
# local variance가 나타날때!
def test() :
    a = 77 # exists during execution of the function
    print(a)
    # disappears when the function is terminated
a = 99 
test() # when a function is called
# 이 경우도 한번 보자!
def test(a) : # 여기는 a라는 parameter를 가졌는데 그 a의 arg값은 99다.
    #global a      ----------------------------------------------------- 이 경우를 보자! a는 이 test함수에 들어오자 parameter라는 local variance를 갖게 되는데, 걔를 global하자는 말 자체가 syntax error가 된다! parameter 함수 자체가 local한 성향이 있는데 어떻게 global로 취하는가
    print(a) # 그래서 99로 프린트
    a = 77  
    print(a)

a = 99
test(a)
print(a)
# Parameter인 경우를 정말 조심해야한다! 기출에서도 Parameter인 부분때문에 실수를 많이 했는데 이 부분을 정말 유심히 보면서 공부해야한다!

def test(a) :
    print(a)
    a = 77
    print(a) # 이 경우는 parameter로 받은 local variance가 99지만 다시 local variance를 77로 선언했으므로 77반환

a = 99
test(a)
print(a)
