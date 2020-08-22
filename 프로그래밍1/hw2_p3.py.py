"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 로봇으로하여금beeper가 있는 곳에 이를때 까지 불규칙적으로 있는 허들을 넘게 하는 프로그램입니다.
"""    
# 주석은 영어로 달았습니다. 

# Make robot world
from cs1robots import *
#load_world("./worlds/hurdles1.wld")
load_world("./worlds/hurdles2.wld")
#load_world("./worlds/hurdles3.wld")
hubo = Robot()
hubo.set_pause(0.2)
# Make turn right function
def turn_right ():
    for i in range(3):
        hubo.turn_left()
# Make jump function
def jump ():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
# Make loop to make robot keep go and jump hurdle until there is a beeper
while not hubo.on_beeper() :
    if hubo.front_is_clear():
        hubo.move()
    else :
        jump()









