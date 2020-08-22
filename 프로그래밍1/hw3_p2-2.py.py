"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 로봇으로 하여금 주어진 맵의 창문을 전부 닫게 하는 프로그램입니다.
"""

from cs1robots import *
load_world("worlds/rain2.wld")
hubo = Robot(beepers = 10, orientation = "E", avenue = 2, street = 6)
hubo.set_pause(0.2)
hubo.set_trace("red")
# 우향 우하는 함수
def turn_right() :
    for i in range(3):
        hubo.turn_left()
# 뒤로 도는 함수
def turn_backward() :
    for i in range(2):
        hubo.turn_left()
# 창문임을 판별하는 함수 구성 ( 로봇을 기준으로 앞이 뚫려 있고 우측 벽도 뚫려 있으나 창문인 경우가 있고 아닌 경우가 있음)
def there_is_window():
    window = False
    hubo.move()
    if not hubo.right_is_clear() : # 앞을 한발짝 가서 막혀있으면 창문, 그렇지 않으면 창문이 아님.
        window = True
    turn_backward()
    hubo.move()
    turn_backward() # 다시 판별 전 원위치로 회귀
    return window
        
        
hubo.move()
hubo.drop_beeper() # 36번째 줄 반복문 탈출을 위한 문장
turn_right()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear():
        if not hubo.right_is_clear(): #앞은 뚫려 있으나 우측 벽이 막힌 경우
            hubo.move()
        else :
            if there_is_window() :    #창문인 경우
                hubo.drop_beeper()
                hubo.move()
            else :
                turn_right()          #앞은 뚫려 있고 우측 벽도 뚫려 있으나 창문이 아닌 경우
                hubo.move()
                
    else :
        if not hubo.right_is_clear(): # 모서리인 경우
            hubo.turn_left()
hubo.pick_beeper()
turn_right()
