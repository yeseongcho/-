"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 로봇으로 하여금 비퍼를 전부 윗 열로 옮기게 하고 다시 원 위치로 돌아와 동쪽을 바라보게 하는 프로그램입니다.
"""
# Edit my world
"""
from cs1robots import *
import random
create_world(avenues = 5, streets = 5)
edit_world()
save_world("myworld.wld")
"""


from cs1robots import *
load_world("myworld.wld")
hubo = Robot()
hubo.set_trace("red")
hubo.set_pause(0.1)
# 우향우 함수
def turn_right() : 
    for i in range(3) :
        hubo.turn_left()
# 뒤로 도는 함수
def turn_around() :
    for i in range(2) :
        hubo.turn_left()
# 비퍼를 옮기고 다음 열로 움직이는 함수 만듦
def go_and_move_beeper() :
    while hubo.front_is_clear(): # 벽을 만날 때까지 움직히게 하는 반복문 구성
        if hubo.on_beeper() :
            while hubo.on_beeper(): # 비퍼를 전부 줍게하는 반복문 구성 
                hubo.pick_beeper()
        hubo.turn_left() # 2층을 올라가기 위한 문장
        hubo.move()
        if hubo.carries_beepers(): # 로봇이 비퍼를 가지고 있으면 전부 내려놓게 하는 반복문 구성
            while hubo.carries_beepers():
                hubo.drop_beeper()
        turn_around()
        hubo.move()
        hubo.turn_left() # 다시 1층으로 돌아오기 위한 문장
        hubo.move()
    if hubo.on_beeper(): # 31번째 줄의 반복문을 탈출할 때 비퍼가 있는 경우(로봇이 벽면에 닿을때)
        while hubo.on_beeper():
            hubo.pick_beeper()
    hubo.turn_left()
    hubo.move()
    if hubo.carries_beepers(): # 마지막 벽면 쪽 2층으로 가 비퍼를 전부 내려놓게 하는 문장
        while hubo.carries_beepers():
            hubo.drop_beeper()
            
    turn_around()
    hubo.move()
    turn_right()
    while hubo.front_is_clear(): # 다시 원래 위치로 돌아오게 하는 반복문
        hubo.move()
    turn_around() # 동쪽을 바라보게 하기 위해

go_and_move_beeper() # main 함수 실행


