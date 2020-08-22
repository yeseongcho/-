"""
Name : 조예성
Student ID : 21600685
Description : 사용자로부터 명령어를 입력받아 로봇으로하여금 계단을 올라 해당 지점에 신문을 배달하게하고
              다시 원래 위치로 돌아오게 하는 함수를 만듭니다.
"""
# 로봇을 불러오기 위한 cs1robots라는 라이브러리를 불러옵니다.
from cs1robots import *
# 계단이 포함되어 있는 그래프를 worlds파일에서 불러옵니다.
load_world("worlds/newspaper.wld")
# 로봇을 만들고 1초에 한번 씩 움직이게 합니다.
hubo = Robot(beepers = 1) 
hubo.set_pause(1)
# 로븟을 우향우 시키는 함수를 만듭니다.
def turn_right():
    for i in range(3):
        hubo.turn_left()
# 계단을 올라가는 함수를 만듭니다.
def up_stairs():
    hubo.move() # 한칸 앞으로 간 뒤에 계단을 올라가야 하므로
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
# 뒤로 도는 함수를 만듭니다.
def turn_around():
    for i in range(2):
        hubo.turn_left()
# 계단을 내려가는 함수를 만듭니다.
def down_stairs():
    hubo.move() # 한칸 앞으로 간 뒤에 계단을 내려가야 하므로
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
# 신문을 배달하는 지점까지 가기 위해 4번의 up_staris 반복문을 구성합니다.
for i in range(4):
    up_stairs()
hubo.move()
hubo.drop_beeper() # 신문을 내려놓습니다.
turn_around()
hubo.move()
# 신문을 내려놓은 뒤 다시 원래 자리로 돌아오기 위해 down_stairs 반복문을 구성합니다.
for i in range(4):
    down_stairs()
# 처음 로봇이 바라보는 방향을 만들기 위해 다시 뒤를 돌아보게 합니다.
turn_around()
    
    
    

           
