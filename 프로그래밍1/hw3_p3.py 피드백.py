"""
from cs1robots import *
import random
x = random.randint(1, 15)
y = random.randint(1, 15)
create_world(avenues = x, streets = y)
edit_world()
save_world("worlds/myworld.wld")
"""

from cs1robots import *
load_world("worlds/myworld.wld")
#create_world(avenues = 5, streets = 5)
hubo = Robot(avenue = 1, street =1 )
hubo.set_pause(0.1)
hubo.set_trace("red")

def turn_right() :
    for i in range(3):
        hubo.turn_left()

def turn_around() :
    for i in range(2) :
        hubo.turn_left()
# 이 문제를 풀때 중요한 건 맵이 random이라는 것이다! 그럼 맵이 어떠한 경우인지 모든 경우의 수를 다 고려해서 코딩을 짜주어야 한다는 것이다!!!
def move_east() :
    while hubo.front_is_clear() :
        if hubo.on_beeper() : # 시작할 때 비퍼가 있어도 주워야 하잖아!
            while hubo.on_beeper() :
                hubo.pick_beeper()
        hubo.move()
    if hubo.on_beeper() : # 벽에 막혀 뒤로 돌 때도 비퍼는 주어야한다
        while hubo.on_beeper() :
            hubo.pick_beeper()
    hubo.turn_left()
    if hubo.front_is_clear() :
        hubo.move()
        turn_around()
        if hubo.right_is_clear() : # 이 경우 모서리에 위치
            turn_right()
        else :
            turn_around() # x = 1인 특수경우
            while hubo.front_is_clear() :
                hubo.move()
            hubo.turn_left()

def move_west() :
    while hubo.front_is_clear() :
        if hubo.on_beeper() :
            while hubo.on_beeper() :
                hubo.pick_beeper()
        hubo.move()
    if hubo.on_beeper() :
        while hubo.on_beeper() :
            hubo.pick_beeper()
    turn_right()
    if hubo.front_is_clear() :
        hubo.move()
        turn_right()
    
# 반복문의 run time error를 멈추기 위한 조건!
def wall() :
    if not hubo.front_is_clear() and not hubo.right_is_clear or not hubo.left_is_clear() and not hubo.front_is_clear() : 
        return True

def main() :
    while True :
        if not wall() :
            move_east()
            move_west()
        else :
            break  
        

main()
    
