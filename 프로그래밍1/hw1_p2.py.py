"""
Name : 조예성
Student ID : 21600685
Description : 사용자로부터 명령어를 입력받아 로봇을 허들을 넘게해 목표하는 위치까지 이동해
              beeper를 내려놓고 돌아오는 명령을 수행하는 프로그램입니다.
"""
# 로봇을 불러오기 위한 cs1robots라는 라이브러리를 불러옵니다.
from cs1robots import *
load_world("C:/Users/sec/Desktop/교과목들/프로그래밍1/worlds/hurdles1.wld") # 허들이 포함되어 있는 그래프를 worlds파일에서 불러옵니다.
hubo = Robot() # 로봇을 만들어줍니다.
# 로봇이 지나가는 자취를 파란 선으로 표시해주고 1초에 한번씩 움직이게하는 명령어입니다.
hubo.set_trace("blue")
hubo.set_pause(1)
# 로봇이 우향우를 하는 새로운 함수를 만듭니다.
def turn_right():
    for i in range(3):
        hubo.turn_left()
# 로봇이 한걸음 가고 허들을 한 번 뛰어넘고 다시 옆을 보는 과정까지 나타내주는 함수를 만듭니다.
def jump_forward():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
# 로봇이 뒤로 도는 함수를 만들어줍니다.
def turn_around():
    for i in range(2):
        hubo.turn_left()
# Jump_forward와는 반대 방향으로 다시 돌아오는 함수를 만들어줍니다.
def jump_backward():
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
# 해당 지역까지 허들을 넘으며 이동하는 반복문을 구성합니다.
for i in range(4):
    jump_forward()
# 해당지역까지 이동 후 beeper를 내려놓고 다시 뒤를 돕니다.
hubo.move()
hubo.pick_beeper()
turn_around()
# 원래 집으로 돌아가기 위한 반복문을 구성합니다.
for i in range(4):
    jump_backward()
hubo.move()
# 마지막으로 원래 로봇이 바라보는 방향을 보게 하기 위해 뒤를 돌게 합니다.
turn_around()
    
