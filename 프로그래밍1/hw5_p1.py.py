"""
Name : 조예성
Student ID : 21600685
Description : 이 함수는 캔버스에 집, 나무 등 다양한 그림을 그려놓는 프로그램입니다.
"""


from cs1graphics import *
paper = Canvas(300, 200, 'skyblue', 'My canvas') # 가로 300, 세로 200에 배경색이 하늘색인 배경을 만들어준다.

def Draw_sun() : # 해를 만드는 함수 지정
    sun = Circle(30, Point(250, 50)) # 크기는 30으로 지정
    sun.setFillColor("yellow")
    paper.add(sun) 
    sunraySW = Path(Point(225, 75), Point(210, 90)) # 햇빛도 추가적으로 만들어준다
    sunraySE = Path(Point(275, 75), Point(290, 90))
    sunrayNE = Path(Point(275, 25), Point(290, 10))
    sunrayNW = Path(Point(225, 25), Point(210, 10))
    sunraySW.setBorderWidth(6) 
    sunraySE.setBorderWidth(6)
    sunrayNE.setBorderWidth(6)
    sunrayNW.setBorderWidth(6)
    sunraySW.setBorderColor("yellow")
    sunraySE.setBorderColor("yellow")
    sunrayNW.setBorderColor("yellow")
    sunrayNE.setBorderColor("yellow")
    paper.add(sunraySW)
    paper.add(sunraySE)
    paper.add(sunrayNE)
    paper.add(sunrayNW)


def Draw_house() : # 창문, 지붕을 제외한 집을 만드는 함수 지정
    facade = Square(60, Point(140, 130))
    facade.setFillColor('white')
    paper.add(facade)

def Draw_roof() : # 지붕을 만드는 함수 지정
    roof = Polygon(Point(110, 80), Point(80, 100), Point(200, 100), Point(170, 80)) # 사다리꼴 모양의 지붕이므로 polygon함수를 활용해준다. 네 포인트를 전부 찍어준다.
    roof.setFillColor((60, 60, 60)) # 지붕 색 지정
    roof.setDepth(40) # house보다 더 앞쪽에 있어야 하므로 깊이를 40으로 해준다.(집의 깊이가 기본 값인 50이므로)
    paper.add(roof)

def Draw_window() : # 창문을 만드는 함수 지정
    window = Rectangle(10, 30, Point(130, 120))
    window.setFillColor("blue")
    window.setBorderColor("red") # 창문의 테두리 색이 다르므로 빨간색 지정
    window.setBorderWidth(5)
    window.setDepth(40) # 역시 집보다 앞쪽에 위치해야 하므로 깊이 40 지정
    paper.add(window)

def Draw_chimney() : # 굴뚝을 만드는 함수 지정
    chimney = Rectangle(15, 28, Point(155,85))
    chimney.setFillColor('red') 
    chimney.setDepth(30) # 굴뚝의 경우 지붕보다 더 앞쪽에 위치해야 하므로 깊이 30 지정
    paper.add(chimney)

def Draw_smoke() : # 연기를 만드는 함수 지정
    smoke = Path(Point(155, 70), Point(150, 65), Point(160, 55), Point(155, 50)) # 4개의 점을 이은 선으로 구성되어 있으므로 path함수 활용
    paper.add(smoke)

def Draw_trees() : # 나무를 만드는 함수 지정
    tree = Polygon(Point(50, 80), Point(30, 140), Point(70, 140)) # 삼각형을 만드는 함수가 따로 없으므로 polygon함수를 활용해준다.
    tree.setFillColor("darkGreen")
    paper.add(tree)
    othertree = tree.clone() # (170,30)쪽에 다른 나무를 만들어주어야 하므로 clone() method활용
    othertree.move(170, 30)
    othertree.scale(1.2) # 다른 나무의 크기를 더 늘려준다.
    paper.add(othertree)

def Draw_grass() : # 잔디를 만드는 함수 지정
    grass = Rectangle(300, 80, Point(150, 160))
    grass.setFillColor("green")
    grass.setBorderColor("green") # 경계선 역시 동일하게 초록색으로 해준다.
    grass.setDepth(75) # 잔디의 경우 모든 물체들이 잔디 위에 있어야 하므로 깊이를 가장 깊게 해준다.
    paper.add(grass)

def Draw_car_and_move() : # 자동차를 만들어 움직이게 하는 함수 지정
    car = Layer() # layer를 이용한다. (바퀴와 몸체가 하나가 되게 하기 위해)
    tire1 = Circle(8, Point(65, 195))
    tire2 = Circle(8, Point(95, 195))
    tire1.setFillColor("black")
    tire2.setFillColor("black")
    tire1.setDepth(10) # 자동차의 타이어의 경우 몸체보다 앞에 있어야 하며, 캔버스에 있는 모든 물체보다 앞쪽에 있어야 하므로
    tire2.setDepth(10)
    car.add(tire1) # 각각의 타이어를 자동차 layer에 합쳐준다.
    car.add(tire2)
    body = Rectangle(60, 30, Point(80, 180)) 
    body.setFillColor("blue")
    body.setDepth(20) # 몸체의 경우 타이어보단 뒤에 있지만 다른 물체들보단 앞에 있어야 하므로 깊이 20 지정
    car.add(body) # 몸체도 자동차 layer에 합쳐준다.
    paper.add(car)
    for i in range(100) :
        car.move(2, 0) # 자동차를 동쪽으로 이동시켜주는 함수 지정

# 함수들 실행
Draw_sun()
Draw_house()
Draw_roof()
Draw_window()
Draw_chimney()
Draw_smoke()
Draw_trees()
Draw_grass()
Draw_car_and_move()


    
     
