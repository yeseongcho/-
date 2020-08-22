"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 임의로 맵의 크기와 로봇의 위치, 그리고 바라보는 방향이 정해지고 그 로봇을 다시 처음위치로 되돌려 동쪽을 바라보게 하는 프로그램입니다.
"""

from cs1robots import *
import random
x = random.randint(1, 10)
y = random.randint(1, 10)
f = random.randint(1, 4) # 로봇의 방향을 임의로 지정하기 위한 임의값 f 지정
create_world(avenues=x, streets=y)
# 임의의 f값에 동서남북 값 부여
if f == 1 :
    f = "E"
elif f == 2 :
    f = "W"
elif f == 3 :
    f = "S"
else :
    f = "N"


hubo = Robot(orientation = f, avenue = x, street = y)
hubo.set_trace("red")
hubo.set_pause(0.1)
# 우향우 함수
def turn_right():
    for i in range(3):
        hubo.turn_left()
# 뒤로 돌아 함수
def turn_backward():
    for i in range(2):
        hubo.turn_left()
# 이 위치가 처음 위치인지 판별하는 함수
def first_position() :
    first = False
    hubo.turn_left()
    if not hubo.right_is_clear():
        first = True
    return first
# 로봇이 바라보는 방향이 동쪽일 때
if f == "E":
    turn_backward()
    while hubo.front_is_clear():
        hubo.move()
    #벽을 마주했을 때
    hubo.turn_left()
    #벽면에 다다를 때
    while not hubo.right_is_clear():
        while hubo.front_is_clear():
            hubo.move()
        if first_position(): # 처음위치로 돌아가면 while문(right is clear)을 빠져나가야한다.(로봇이 멈추어야 하기 때문) 그러기 위한 조건문 구성.
            turn_backward()
    turn_backward()

# 로봇이 바라보는 방향이 서쪽일 때
if f == "W" :
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    while not hubo.right_is_clear():
        while hubo.front_is_clear():
            hubo.move()
        if first_position():
            turn_backward()
    turn_backward()

# 로봇이 바라보는 방향이 남쪽일 때
if f == "S" :
    turn_right()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    while not hubo.right_is_clear():
        while hubo.front_is_clear():
            hubo.move()
        if first_position():
            turn_backward()
    turn_backward()
# 로봇이 바라보는 방향이 북쪽일 때
if f == "N" :
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    while not hubo.right_is_clear():
        while hubo.front_is_clear():
            hubo.move()
        if first_position():
            turn_backward()
    turn_backward()
        
