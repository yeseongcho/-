"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 40*sinX+40 함수를 x가 0~2파이 범위까지의 그래프를 그리는 프로그램입니다.
"""

import math # 수학 식을 쓰기 위한 조건

def compute_and_plot(angle) :
    n = int(math.sin(angle)*40+40+0.5) # '#'기호가 들어가는 수를 정의, 후에 #을 표기하기 위한 지표
    print("#"*n)
for i in range(41) :
    angle = (2*math.pi/40)*i # i는 0~2파이까지 해당하는 x의 값을 불연속적으로 40번 나누기 위한 조건, 연속적인 값은 "#"그림으로 그리기에 제한이 되므로
    #angle은 i가 0에서부터 40까지 변할 때마다 갖게 되는 세타값
    compute_and_plot(angle)
    # 설정한 세타값 angle을 sin함수에 대입
    
