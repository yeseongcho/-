"""
Name : 조예성
Studnet ID : 21600685
Description : 이 함수는 사용자가 맵(맵의 크기는 랜덤, 비퍼의 위치와 수는 임의로 지정)을 만들고 로봇으로 하여금 좌에서 우로 이동하며 비퍼를 전부 줍게 하는 프로그램입니다.
"""


from cs1robots import *
import random
x = random.randint(1, 15)
y = random.randint(1, 15)
create_world(avenues = x, streets = y)
edit_world() # 임의로 world 구성
save_world("worlds/myworld.wld")

"""
from cs1robots import *
load_world("worlds/myworld.wld") # 앞의 주석 처리한 부분에서 만든 world 불러옴
#create_world(avenues =1, streets = 1)
hubo = Robot(avenue = 1, street = 1)
hubo.set_pause(0.1)
hubo.set_trace("red")
# 우향 우 함수 구성
def turn_right() :
    for i in range(3):
        hubo.turn_left()
# 동쪽으로 이동하면서 쓰레기 줍고 한 계단 올라가는 함수
def move_east() :
    while hubo.front_is_clear() : # 벽이 없을 땐  계속 움직이게 하는 반복문 구성
        if hubo.on_beeper() :
            while hubo.on_beeper() :# 1개 이상의 비퍼를 모두 줍게 하기 위한 반복문
                hubo.pick_beeper()
        else :
            hubo.move()
    hubo.turn_left()
    if hubo.on_beeper() :
        while hubo.on_beeper() :# 1개 이상의 비퍼를 모두 줍게 하기 위한 반복문
            hubo.pick_beeper()
    
        
    
# 서쪽으로 이동하면서 쓰레기 줍고 한 계단 올라가는 함수
def move_west() :
      while hubo.front_is_clear(): # 벽이  없을 땐 계속 움직이게 하는 반복문
          if hubo.on_beeper() :
              while hubo.on_beeper() :
                  hubo.pick_beeper()

          else :
              hubo.move()
                
      turn_right()
      if hubo.on_beeper() :
          
          while hubo.on_beeper() :# 1개 이상의 비퍼를 모두 줍게 하기 위한 반복문
              
              hubo.pick_beeper()
     

                  
while True :
    if hubo.front_is_clear() :
        move_east()
        if not hubo.front_is_clear() :
            break
        hubo.move()
        hubo.turn_left()
        move_west()
        if not hubo.front_is_clear() :
            break
        hubo.move()
        turn_right()
    if not hubo.front_is_clear() : # 특수 경우
        hubo.turn_left()
        if hubo.front_is_clear() :
            while hubo.front_is_clear() :
                if hubo.on_beeper() :
                    while hubo.on_beeper() :
                        hubo.pick_beeper()
                hubo.move()
        if not hubo.front_is_clear() :
            break
    

    # 집 끝까지 갈 때까지 쓰레기 줍게하는 함수 구성

"""
