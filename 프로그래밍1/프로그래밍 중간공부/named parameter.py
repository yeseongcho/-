from cs1graphics import *
canvas = Canvas(300, 300)

def create_circle(radius = 30, color = "yellow") :
    circle = Circle(radius)
    circle.setFillColor(color)
    circle.setBorderColor(color)
    circle.moveTo(100, 100)
    return circle
circle = create_circle()
circle = create_circle(color="red")
circle = create_circle(20) # named parameter가 아니면 순서가 중요하다!
circle = create_circle(color = "red", radius = 20) # 둘다 named면 순서가 상관 없다!
circle = create_circle(color = "red", 20) # 하나라도 named가 아니면
circle = create_circle("red", radius = 20) # positional correspondence를 지켜라!
canvas.add(circle)

# 작년 중간 기출이었다! 이 예시를 꼭 기억하라!
