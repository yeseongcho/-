"""
Name : 조예성
Student ID : 21600685
Description : 이 프로그램은 주어진 사진을 다른 사진에 덧붙이는 프로그램입니다.
"""

# 이미지 불러옴
from cs1media import*
import math
img1 = load_picture("photos/statue1.jpg")
img2 = load_picture("photos/trees1.jpg")

# 석상 사진을 반전시킴
def reflection(img) :
    w, h = img.size()
    for y in range(h) :
        for x in range(w//2) :
            p1 = img.get(x, y)
            p2 = img.get(w-1-x, y)
            img.set(x, y, p2)
            img.set(w-1-x, y, p1)
    return img

# 배경색과 석상색의 색 정도를 구분하기 위한 함수
def get_distance(pixel, backcolor) :
    r1, g1, b1 = pixel
    r2, g2, b2 = backcolor
    return math.sqrt((r1-r2)**2 +(g1-g2)**2 + (b1-b2)**2)

# 석상 사진의 배경 사진을 잘라내는 함수
def chromarkey(img1, img2, key, threshold) :
    w, h = img1.size()
    for y in range(h) :
        for x in range(w) :
            j1 = img1.get(x, y)
            j2 = img2.get(x+200, y+50)
            if get_distance(j1, key) < threshold : # 석상 색의 tuple값이 일정 기준을 넘지 못하면(배경색이면) 그 부분은 배경 사진으로 대체한다
                img1.set(x, y, j2)
    return img1
                
# 석상 사진을 배경 사진에 붙이는 함수
def put_state(img1, img2, x0, y0) :
    w, h = img1.size()
    for y in range(h) :
        for x in range(w) :
            states = img1.get(x,y)
            img2.set(x0+x, y0+y, states)
    return img2
            

def main() :
    img = reflection(img1)
    key = (41, 75, 146) # 배경색
    threshold = 70 # 배경색과 석상색의 기준선, 이 정도를 넘냐 안넘냐에 따라 잘라낼지 말지를 결정

    image = chromarkey(img, img2, key, threshold)
    
    i = 200
    j = 50
    
    image2 = put_state(image, img2, i, j)
    
    image2.show()

main()
