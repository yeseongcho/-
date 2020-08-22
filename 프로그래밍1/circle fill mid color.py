from cs1graphics import *
canvas = Canvas(500, 500)
circle1 = Circle(20, Point(300, 300)) # 원을 만들때는 중심이 몇 포인트인지도 항상!
circle2 = Circle(20, Point(250, 250))
circle3 = Circle(20, Point(200, 200))
canvas.add(circle1) # 캔버스에 나타내기 위해서는 항상 이런 게 필수!
canvas.add(circle2)
canvas.add(circle3)
color1 = (255, 0, 0)
color3 = (0, 0, 255)
circle1.setFillColor(color1)
circle3.setFillColor(color3)

def get_t() : # t를 입력받음
    while True :
        try :
            t = input("put your number t : ")
            value = float(t)
            if 0 < value < 1 :
                break
            else : print("Please put your number between 0 and 1 : ")
        except :
            print("Please again put your number t : ")
    return value

def interpolate_color(t, color1, color3) : # 입력받은 t에 맞게 적당한 값 반환
    r1, g1, b1 = color1
    r2, g2, b2 = color3
    return int((1-t)*r1 + t*r2), int((1-t)*g1+t*g2), int((1-t)*b1+t*b2) # 굳이 tuple값으로 반환한다고 큰 괄호를 만들 필요는 x
#print(11111) # 디버그 하는 방법
t = get_t()
#print(22222)
color2 = interpolate_color(t, color1, color3)
#print(33333, color2)
circle2.setFillColor(color2)
#print(44444)
#print(55555)
