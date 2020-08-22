"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 로봇으로하여금 불규칙적으로 있는 beeper를 우측에서 좌측으로 이동하면서
              전부 줍게 하는 프로그램입니다. ( 단, 맨 상단에 있는 줄은 수확하지 않습니다. )
"""    
# 주석은 영어로 달았습니다. 

# Make robot world
from cs1robots import *
#load_world("./worlds/harvest4.wld")
#load_world("./worlds/harvest1.wld")
load_world("./worlds/harvest3.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)
# Make turn right function
def turn_right() :
    for i in range(3):
        hubo.turn_left()
# Make function that robot move east and go up one step 
def move_east():
    while hubo.front_is_clear(): 
        if hubo.on_beeper():
            while hubo.on_beeper():
                hubo.pick_beeper() # make robot harvest every beeper not only one.(If there are two beeper, make robot harvest all of them)
        else :
            hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper() # Make this condition so that we can harvest beeper even if hubo's front isn't clear.
    hubo.turn_left()
    hubo.move() # Make this step so robot do not harvest the highest avenue because through this, we can go out loop in line 47.
# Make function that robot move west and go up one step
def move_west():
    while hubo.front_is_clear():
        if hubo.on_beeper():
            while hubo.on_beeper():
                hubo.pick_beeper()  # make robot harvest every beeper not only one.(If there are two beeper, make robot harvest all of them)
        else :
            hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper() # Make this condition so that we can harvest beeper even if hubo's front isn't clear.              
    turn_right()
    hubo.move()  # Make this step so robot do not harvest the highest avenue because through this, we can go out loop in line 47.
        
# Make a loop to make robot harvest
while hubo.front_is_clear() :
    move_east() 
    if hubo.front_is_clear() :
        hubo.turn_left()
    move_west()
    if hubo.front_is_clear() :
        turn_right()
        

