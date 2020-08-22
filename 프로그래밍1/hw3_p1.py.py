"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 일정한 기준으로 주어진 이미지 내 많이 어두운 색은 파란색으로 중간 색은 초록색으로 밝은 색은 노란색으로 전환시켜 주는 프로그램입니다
"""


from cs1media import *
img = load_picture("images/yuna.jpg")
# 색깔의 이름을 정의
blue = (0, 0, 255) 
green = (0, 255, 0)
yellow = (255, 255, 0)
# 기준치 설정 
threshold1 = 255
threshold2 = 510
# size tuple unpacking
w, h = img.size()
# x, y 전체 픽셀의 색을 변화시키기 위한 반복문
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y) # x, y에 해당하는 r,g,b값 도출
        if 0 <= r+g+b < threshold1 :
            img.set(x, y, blue) # 파란색 전환
        elif threshold1 <= r+g+b < threshold2 :
            img.set(x, y, green) # 초록색 전환
        else :
            img.set(x, y, yellow) # 노랑색 전환

img.show()
