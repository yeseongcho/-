"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 40*sinX+40 함수를 x가 0~2파이 범위까지의 그래프를 점을 찍어 그리는 프로그램입니다.
"""


import math

def compute_and_plot(angle) :
    n = int(math.sin(angle)*40+40+0.5) # sin함수의 결과값을 반올림해서 정수형으로 만든 수 정의, 후에 여백과 선, 점을 표시하기 위해 필요한 지표
    #print(n)
    if n > 40 : # 그림 상 x축 위쪽의 그림을 그리기 위한 조건
        if n == 41 : # 41일 때 경우를 따로 분류, 16번째 줄의 조건을 만들기 위해
            print(" " * 39 + "|" + "*")
        else :
            print(" " * 39 + "|" + " "*(n-41) + "*") 
    elif n < 40 : # 그림 상 x축 아래쪽의 그림을 그리기 위한 조건
        if n == 0 : # n이 0일때 특수 경우 따로 구분, 23번째 줄의 조건을 만들기 위해
            print("*" + " "*38 + "|")
        else :
            print(" "*(n-1) + "*" + (39-n)*" " + "|")
    else :
        if angle == math.pi : # x축을 그리기 위한 조건
            print("-"*39 + "*" + "-"*39)
        else :
            print(" "*39 + "*") # y축 위에 있는(on, not up) 점의 경우
    



for i in range(41) :
    angle = (2*math.pi/40)*i
    # 0~2파이까지 40번 나누기 위한 i 설정, i가 0~40까지 변할때마다 angle값 지정(연속 값을 갖는 수를 불연속인 정수 값으로 취하기 위해)
    compute_and_plot(angle)

    
