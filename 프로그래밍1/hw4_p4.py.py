"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 로봇으로 하여금 마름모 방향으로 바깥부터 시계반대방향으로 비퍼를 줍게 하는 프로그램입니다.
"""

from cs1robots import *
load_world("worlds/harvest2.wld")
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def harvest_all(robot) :
    move_to_bottom(robot)
    pick_beepers(robot)

def move_to_bottom(robot) : # 첫 로봇의 시작점 위치로 가게 하는 함수, parameter값을 robot으로 잡은 이유는 hubo가 아닌 다른 로봇이어도 같은 기능을 하게 하기 위함.
    for i in range(5) :
        robot.move()
    robot.turn_left()
    robot.move()

def pick_beepers(robot) : # 가장 틀이 큰 함수, 비퍼를 줍게 하는 함수의 총칭
    for i in range(3) : # n의 변수를 설정하게 하는 반복문
        n = 5-2*i # n은 로봇이 주어야 할 각 변의 비퍼의 갯수를 나타낸다. 이 규칙성에 의해 5, 3, 1개의 비퍼를 줍게 된다.
        diamond(robot, n) # diamond 함수 실행
        if n > 2 : # n=5, 3일때는 다음 시작점으로 가기 위해 북쪽으로 2번 움직여야 한다.
            robot.move()
            robot.move()

def turn_right(robot) :     # 우향우 함수
    for i in range(3) :
        robot.turn_left()

def diamond(robot, n) :     # 마름모 각 변에 있는 비퍼들을 모두 줍게 하는 함수
    for i in range(4) : # 마름모는 총 4개의 변을 가지므로 총 4번의 반복을 시행(= 총 4번의 move_and_pick함수 실행 )
        move_and_pick(robot, n)
        robot.turn_left() # 다음 변으로 똑같이 move_and_pick을 실행하기 위한 좌향 좌

def move_and_pick(robot, n) : # 마름모 한 변에 있는 비퍼들을 전부 줍게 하는 함수
    for i in range(n) :  # 여기서 n은 각 마름모 변에 있는 주울 비퍼들의 갯수를 의미하는 변수 ( 처음 자리에 있는 비퍼를  제외하고 5개, 3개, 1개의 규칙을 갖는다.  38번째 줄의 조건에 의해 정해진다. )
        robot.pick_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()
def move_and_pick(robot, n) : # 마름모 한 변에 있는 비퍼들을 전부 줍게 하는 함수
    for i in range(n) :  # 여기서 n은 각 마름모 변에 있는 주울 비퍼들의 갯수를 의미하는 변수 ( 처음 자리에 있는 비퍼를  제외하고 5개, 3개, 1개의 규칙을 갖는다.  38번째 줄의 조건에 의해 정해진다. )
        robot.pick_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()

harvest_all(hubo) # hubo를 parameter로 갖는 main 함수 실행
