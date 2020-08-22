"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 해가 떠서 지는 동안 해와 하늘의 색이 변하게 하는 프로그램입니다.
"""


from cs1graphics import *
import math # 수식을 사용하기 위해
import time # time.sleep을 사용하기 위해
paper = Canvas(400, 400)

sun = Circle(20, Point(0, 410)) # 해의 위치를 초반 캔버스 좌측 아래쪽에 위치하도록 지정

sun.setFillColor('red')
paper.setBackgroundColor('white')

paper.add(sun)

# angle값이 변함에 따라 하늘의 색을 변하게 하는 함수 지정
def set_sky_color(angle) : # Color('skyblue').getColorValue()를 실행한 결과 하늘색은 (135, 206, 235)의 tuple값을 가짐!
    if 0<= angle <= 90 :
        n = (int(angle*135/90), int(angle*206/90), int(angle*235/90))  # 처음 angle이 0에서 90까지 변할때 하늘이 (0, 0, 0)에서 (135, 206, 235)값으로 변하는 n의 값 지정

    elif 90< angle <= 180 : # angle이 90에서 180으로 변할 때 하늘이 (135, 206, 235)에서 (0, 0, 0)값으로 변하는 n의 값 지정
        n = (int(135-(angle-90)*135/90), int(206-(angle-90)*206/90), int(235-(angle-90)*235/90))

    elif 180 < angle <= 360 : # 밤일 경우 하늘은 계속 검정색
        n = (0, 0, 0)

    elif 360 < angle <= 450 : # 다시 해가 뜰 경우인 이 경우 angle이 360에서 450으로 변할 때 하늘이 (0, 0, 0)에서 (135, 206, 235)값으로 변하는 n의 값 지정
        n = (int((angle-360)*135/90), int((angle-360)*206/90), int((angle-360)*235/90))

    elif 450 < angle <= 540 : # 다시 해가 질 경우인 이 경우 angle이 450에서 540으로 변할 때 하늘이 (135, 206, 235)에서 (0, 0, 0)값으로 변하는 n의 값 지정
        n = (int(135-(angle-450)*135/90), int(206-(angle-450)*206/90), int(235-(angle-450)*235/90))

    else :
        n = (0, 0, 0) # 이후는 다시 하늘을 검정색으로
    
    return n # 그 변하는 n의 값을 리턴

# angle값이 변함에 따라 해의 색을 변하게 하는 함수 지정
def set_sun_color(angle) :
    if 0<= angle <= 90 : # angle이 0에서 90으로 변할 때 해의 색이 빨강색인 (255, 0, 0)에서 노란색인 (255, 255, 0)으로 변하는 m의 값 지정
        m = (255 , int(255*angle/90), 0 )

    elif 90< angle <= 180 : # angle이 90에서 180으로 변할 때 해의 색이 노란색인 (255, 255, 0)에서 빨강색인 (255, 0, 0)으로 변하는 m의 값 지정
        m = (255, int(255*(180-angle)/90), 0 )

    elif 180<= angle < 360 :
        m = (0, 0, 0) # 밤일 경우 해의 색은 딱히 중요치 않으므로 검정색 지정

    elif 360<= angle < 450 : # 다시 해가 뜨는 경우인 이 경우 angle이 360에서 450으로 변할 때 태양이 (255, 0, 0)에서 (255, 255, 0 )으로 변하는 m의 값 지정
        m = (255, int(255*(angle-360)/90), 0 ) 

    elif 450<= angle < 540 : # 다시 해가 지는 경우인 이 경우 angle이 450에서 540으로 변할 때 태양이 (255, 255, 0)에서 (255, 0, 0)으로 변하게 하는 m의 값 지정
        m = (255, int(255*(540-angle)/90), 0 )

    else :
        m = (0, 0, 0)

    return m # 그 변하는 m의 값을 리턴

# sun과 paper값을 parameter로 갖는 총괄 함수 지정
def animate_sunrise(sun, paper) :
    w = paper.getWidth() # 해의 중심을 이동시키기 위한 w, h, r값 구함
    h = paper.getHeight()
    r = sun.getRadius()
    x0 = w/2 
    y0 = h + r
    max_x = w/2 - r # 원의 중심이 x0에서 가장 많이 떨어져 있는 경우, 이 값에다 angle에 따라 변하는 cos값을 곱해주고 그 정도를 x0에서 빼줌으로써  해의 중심을 이동시킨다.
    max_y = h # 원의 중심이 y0에서 가장 많이 떨어져 있는 경우, 이 값에다 angle에 따라 변하는 sin값을 곱해주고 그 정도를 y0에서 빼줌으로써 해의 중심을 이동시킨다.


    for angle in range(721) : # 총 2번 태양이 360도 돌아야 하므로 angle값을 720도까지 변하게 함
        time.sleep(0.05) # 해가 너무 빨리 이동하지 않게 속도 지
        rad = (math.pi/180)*angle # angle값을 sin, cos의 변수로 받아야 하기에 radian값으로 변환

        x = x0 - math.cos(rad)*max_x # 이 식들을 통해 angle에 따른 원의 중심이 타원 모양으로 이동하게 된다.
        y = y0 - math.sin(rad)*max_y 

        sun.moveTo(x, y) # 해의 중심을 이동

        n=set_sky_color(angle) # set_sky_color값에서 구한 리턴 값을 n에 반환

        m=set_sun_color(angle) # set_sun_color값에서 구한 리턴 값을 m에 반환

        paper.setBackgroundColor(n) # 하늘의 배경색으로 지정

        sun.setFillColor(m) # 해의 색으로 지정

# main함수 실행
animate_sunrise(sun, paper)

