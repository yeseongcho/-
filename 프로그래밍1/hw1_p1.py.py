"""
Name : 조예성
Student : 21600685
Description : 사용자로부터 값을 입력받아 해당 로봇을 지그재그 모양으로 움직이게
              하는 프로그램입니다.
"""
# 로봇을 불러오기 위한 cs1robots라는 라이브러리를 불러옵니다.
from cs1robots import * 
# 로봇이 활동하게 될 격자 모양의 그래프와 로봇을 만들기 위한 명령어입니다.
create_world()
hubo = Robot()
# 로봇이 지나가는 자취를 파란 선으로 표시해주고 1초에 한번씩 움직이게하는 명령어입니다.
hubo.set_trace("blue")
hubo.set_pause(0.2)
# turn_right이라는 새로운 함수를 만듭니다.
def turn_right():
    for i in range(3):
        hubo.turn_left()
# 로봇 기준 위로 올라가고 열을 바꾸어 내려가기까지의 경로를 나타내는 함수를 만듭니다.
def move_up_and_down():
    hubo.turn_left()
    # 그래프의 끝 바운더리까지 가기 위해 9번의 move를 수행하는 반복문을 만듭니다.
    for i in range(9):
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    for i in range(9):
        hubo.move()
# move_up_and_down 명령 수행을 마치고 다음 열로 넘어가기 위한 함수를 만듭니다.
def move_to_next_column():
    hubo.turn_left()
    hubo.move()
# move_up_and_down과 move_to_next_column 과정을 4번 반복해주는 반복문을 만듭니다.
for i in range(4):
    move_up_and_down()
    move_to_next_column()
# 마지막으로 한번 더 move_up_and_down하며 해당하는 마지막 위치로 이동합니다.
move_up_and_down()


