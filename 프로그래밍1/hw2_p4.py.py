"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 랜덤으로 형성 되는 맵에 로봇을 위에서 아래방형으로 지그재그로 움직이게 해 맨 끝까지 이동하게 하는 프로그램입니다.
"""    
# 주석은 영어로 달았습니다. 

# Make robot world
from cs1robots import *
import random
# Give random value to x and y
x = random.randint(1, 20)
y = random.randint(1, 20)
#x = 1
#y = 1
create_world(avenues = x, streets = y)
hubo=Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)
# Make turn right function
def turn_right() :
    for i in range(3):
        hubo.turn_left()
# Make going up function
def up_stairs() :
    while hubo.front_is_clear() :
        hubo.move()
    turn_right()
# Make going to next column function
def next_to_column() :
    if hubo.front_is_clear() :
        if hubo.right_is_clear() : # Move to next column when he is on top street.
            hubo.move()
            turn_right()
        else :                     # Move to next column when he is on bottom street.
            hubo.move()
            hubo.turn_left()       
# Make going down function
def down_stairs() :
    while hubo.front_is_clear() :
        hubo.move()
    hubo.turn_left()
# To make it briefly, make main function
def main() :
    hubo.turn_left() # make robot's first direction 
    if hubo.front_is_clear() :
        while hubo.front_is_clear():
            up_stairs()
            next_to_column() # if x=1, hubo's front isn't clear when we are in this function, so it finishes. 
            down_stairs()
            next_to_column()
    else : # if y=1, at the first time, hubo's front is not clear. To deal with special case like(x or y is 1)
        turn_right()
        while hubo.front_is_clear() :
            hubo.move()
    
main()

