"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 로봇으로 하여금 주어진 맵의 창문을 전부 닫게 하는 프로그램입니다.
"""
from cs1robots import *
load_world("worlds/rain1.wld")
hubo = Robot(beepers = 6, orientation = "E", avenue = 2, street = 6) # 집 입구에 6개의 비퍼를 갖는 로봇을 지정 
hubo.set_pause(0.2)
hubo.set_trace("red")
# turn right 함수 
def turn_right() :
    for i in range(3):
        hubo.turn_left()
# 뒤로 도는 함수
def turn_backward() :
    for i in range(2):
        hubo.turn_left()

hubo.move()
hubo.drop_beeper() # 시작할 때 비퍼를 떨굼. 후에 24번째 줄 반복문 탈출을 위한 조건.
turn_right()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear(): 
        if not hubo.right_is_clear():
            hubo.move() # 창문이 아닌 경우
        else :
            hubo.drop_beeper()
            hubo.move() # 창문인 경우
    else :
        if not hubo.right_is_clear():
            hubo.turn_left() # 모서리에 다다른 경우
hubo.pick_beeper() #24번째 반복문 통과 후(즉, 집의 입구에 다다른 후) 
turn_right()
