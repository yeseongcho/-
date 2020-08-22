"""
Name : 조예성
Student ID : 21600685
Description : 사용자로부터 명령어를 입력받아 그래프에 있는 beeper들을 로봇이 전부
              수확하게 하는 명령어를 만듭니다.
"""
# 로봇을 불러오기 위한 cs1robots라는 라이브러리를 불러옵니다.
from cs1robots import *
# 수확할 열매가 포함되어 있는 그래프를 worlds 파일에서 불러옵니다.
load_world("worlds/harvest1.wld")
# 로봇을 만들고 1초에 한번 씩 움직이게 합니다.
hubo = Robot() 
hubo.set_pause(1) 
# 로봇을 우향우 시키는 함수를 만듭니다.
def turn_right():
    for i in range(3):
        hubo.turn_left()
# 로봇을 총 2열을 수확하는 명령어를 만듭니다.
def harvest_onerectangle():
    hubo.move()
    hubo.pick_beeper()
    hubo.turn_left()
    # 아래에서 위까지 가면서 수확하기 위한 반복문을 만듭니다.
    for i in range(5):
        hubo.move()
        hubo.pick_beeper()
    # 열을 옮기기 위한 명령어입니다.
    turn_right()
    hubo.move()
    hubo.pick_beeper()
    turn_right()
    # 다시 위에서 아래로 가면서 수확하기 위한 반복문을 만듭니다.
    for i in range(5):
        hubo.move()
        hubo.pick_beeper()
    hubo.turn_left()
# 이 과정을 3번 반복해줍니다.
for i in range(3):
    harvest_onerectangle()

    
    
