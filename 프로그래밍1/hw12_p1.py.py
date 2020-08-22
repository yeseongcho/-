"""
Name : 조예성
Student ID : 21600685
Description : chicken family animation(엄마 닭과 첫째 병아리가 먼저 가고 뒤쳐진 둘째 병아리가 날면서 따라가는 애니메이션)을 procedural programming으로 실행한 코드입니다.
"""


from cs1graphics import *
import time # 시간 둔화를 위해
# 배경 설정
canvas = Canvas(1000, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Journey of Chicken")

# 땅을 만드는 함수
def create_ground() :
    ground = Rectangle(1000, 100)
    ground.setFillColor("light green")
    ground.move(500, 250)
    canvas.add(ground)

# 해를 만드눈 함수
def create_sun() :
    sun = Circle(50)
    sun.setFillColor("red")
    sun.move(25, 25)
    canvas.add(sun)

# 닭과 병아리들의 몸을 만드는 함수
def make_body(layer, hen = False) :
    if hen : # 닭의 경우 다른 경우이므로 따로 취급
        body = Ellipse(70, 80)
        body.setFillColor("white")
    else :
        body = Ellipse(40, 50)
        body.setFillColor("yellow")
        body.move(0, 10) # 닭보다 병아리의 경우 더 뒤에 위치해야 하므로 
    body.setBorderColor("yellow")
    body.setDepth(20)
    layer.add(body) # 입력받은 layer에 추가

# 닭과 병아리들의 날개를 만드는 함수
def make_wing(layer, hen = False) :
    if hen : # 닭의 경우 다른 경우이므로 따로 취급
        wing = Ellipse(60, 40)
        wing.setFillColor("white")
        wing.setBorderColor("yellow")
        wing.move(15, 10)
    else :
        wing = Ellipse(30, 20)
        wing.setFillColor("yellow")
        wing.setBorderColor("orange")
        wing.move(10, 20)
        wing.adjustReference(-5, -5)
    wing.setDepth(19) # 몸보단 깊이를 낮게 설정 몸보다 앞에 있어야 하므로
    layer.add(wing) # 입력받은 layer에 추가
    return wing
# 닭과 병아리들의 눈을 만드는 함수
def make_eye(layer, hen = False) :
    if hen : # 닭의 경우 다른 경우이므로 따로 취급
        eye = Circle(3)
        eye.move(-15, -15)
    else :
        eye = Circle(3)
        eye.move(-5, 0)
    eye.setFillColor("black")
    eye.setDepth(18) # 눈도 몸보단 깊이를 낮게 설정
    layer.add(eye)

# 부리를 만드는 함수
def make_beak(layer, hen = False) :
    if hen : # 닭의 경우 다른 경우이므로 따로 취급
        beak = Square(8)
        beak.move(-36, 0)
    else :
        beak = Square(4)
        beak.move(-22, 10)
    beak.rotate(45) # 부리모양을 45도 정도 돌려서 부리 모양이 나오게끔. (마름모 모양으로)
    beak.setFillColor("orange")
    beak.setBorderColor("orange")
    beak.setDepth(21) # 몸 안에 가려져야 하므로 몸보다 깊이를 깊게 설정
    layer.add(beak)

# 닭의 벼슬을 만드는 함수
def make_dots(layer, hen = False) :
    if hen : 
        # 첫 번째 모양의 벼슬
        dot1 = Ellipse(5, 8)
        dot1.setFillColor("red")
        dot1.setBorderColor("red")
        dot1.move(0, -42)
        dot1.setDepth(22) # 이것도 몸보다 더 뒤에 위치
        layer.add(dot1)

        dot2 = Ellipse(5, 8)
        dot2.setFillColor("red")
        dot2.setBorderColor("red")
        dot2.move(-6, -42) # 첫번쨰 벼슬보다 살짝 뒤에 위치
        dot2.setDepth(22)
        layer.add(dot2)

# 닭과 병아리 전체를 만드는 함수, layer지정
def make_chicken(hen = False) :
    layer = Layer() # layer설정 이 layer에 눈, 날개, 몸, 부리, 벼슬 등을 다 집어넣는다.
    make_body(layer, hen)
    wing = make_wing(layer, hen) # wing은 return값을 취해야하므로 따로 변수 지정
    make_eye(layer, hen)
    make_beak(layer, hen)
    make_dots(layer, hen)
    return layer, wing

# 닭과 닭이랑 같이 움직이는 병아리를 group으로 묶음
def make_group() :
    group = Layer() # 이 둘을 묶기 위한 layer설정
    mother_hen, wing = make_chicken(True) # 엄마 닭의 경우므로 hen값 true설정
    group.add(mother_hen)
    chicken1, wing1 = make_chicken() # 첫 번째 병아리의 경우
    chicken1.move(120, 0) # 살짝 더 뒤에 위치시켜야 하므로
    group.add(chicken1)
    group.move(600, 200) # layer의 위치 설정
    return group

# group과 두번쨰 병아리를 전부 canvas에 추가시키는 함수
def make_family() :
    group = make_group() 
    chicken2, wing2 = make_chicken() # 두번째 병아리 layer도 구성
    chicken2.move(800, 200) # group layer보다 조금 더 뒤에 위치시켜야 하므로 
    canvas.add(group)
    canvas.add(chicken2)
    return group, chicken2, wing2 # 각각을 리턴해주되 두 번쨰 병아리의 경우 움직임이 필요하므로 따로 리턴

# 배경 설정
def create_scene() :
    create_ground()
    create_sun()
    group, chicken2, wing2 = make_family()
    return group, chicken2, wing2

# group을 움직이게 하는 함수
def move_group(group) :
    for i in range(80) : # 무대 좌측 끝까지 이동시키기 위해
        time.sleep(0.06)
        group.move(-5, -2) # 좌측으로 이동하되 위 아래로 조금씩 흔들면서 이동해야하기에
        group.move(-5, 2)
        if i == 30 : # group이 이만큼 이동했을 때
            text1 = Text("OH?", 20)
            text1.move(800, 160)
            canvas.add(text1)
        elif i == 40 :
            canvas.remove(text1) # 기존의 문구 제거
            text2 = Text("WHERE IS MY MOMMY GOING?", 30)
            text2.move(500, 110)
            canvas.add(text2)
        elif i == 55 :
            canvas.remove(text2)

# 두번째 병아리를 움직이게 하는 함수
def move_chicken2(chicken2, wing2) :
    text3 = Text("Wait for ME~", 25) 
    text3.move(500, 110)
    canvas.add(text3)
    for i in range(10) : # 두 번째 병아리를 끝까지 이동시키기 위해
        for k in range(5) : # 날개도 상황에 맞게 따로 움직여야 하므로 2개의 반복문 구성
            time.sleep(0.06)
            chicken2.move(-10, -20) # 날때
            wing2.rotate(-10)
        for k in range(5) :
            time.sleep(0.06)
            chicken2.move(-10, 20) # 착지할 떄
            wing2.rotate(10)
        time.sleep(0.06)
    canvas.remove(text3)

# 애니메이션을 실행하는 상위 함수
def animate_chicken_family() :
    group, chicken2, wing2 = create_scene()
    move_group(group)
    move_chicken2(chicken2, wing2)

def main() :
    animate_chicken_family()
    canvas.wait()
    canvas.close()

main()
