"""
Name : 조예성
Student ID : 21600685
Description : chicken family animation(엄마 닭과 첫째 병아리가 먼저 가고 뒤쳐진 둘째 병아리가 날면서 따라가는 애니메이션)을 object oriented programming으로 실행한 코드입니다.
"""



from cs1graphics import *
# 배경 설정
canvas = Canvas(1000, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Journey of Chicken")

import time # 시간 둔화를 위해

def animate_chickens(scene) :
    animation = Animation(scene) # animation이란 인스턴스 형성
    animation.move_group() # Animation Class에 있는 move_group속성 실행
    animation.move_chicken2() 


def main() :
    scene = Scene() # scene이란 인스턴스형성
    animate_chickens(scene) 
    canvas.wait()
    canvas.close()

# Scene이라는 class 형성
class Scene :
    def __init__(self) :
        # 다음의 class들을 속성으로 취함
        self.ground = Ground()
        self.sun = Sun()  
        self.family = Family() 

    # Class에 있는 또 다른 정의되는 함수, 최종적으로 group과 두번쨰 병아리와 그 날개를 리턴한다.
    def get_anim_data(self) :
        return self.family.group.layer, self.family.chick2.layer, self.family.chick2.wing

# Ground라는 class 형성
class Ground :
    def __init__(self) :
        # 다음의 특징들을 속성으로 취함. 즉 땅을 만드는 class이다.
        self.grass = Rectangle(1000, 100, Point(500, 250))
        self.grass.setFillColor("light green")
        self.grass.setDepth(100)
        canvas.add(self.grass) # 최종적으로 만들어진 녀석을 캔버스에 추가해준다.

# Sun이라는 class 형성
class Sun :
    def __init__(self) :
        # 다음의 특징들을 속성으로 취함. 즉 해를 만드는 class이다.
        self.suns = Circle()
        self.suns.setRadius(50)
        self.suns.moveTo(25, 25)
        self.suns.setFillColor("red")
        canvas.add(self.suns)
# 닭과 병아리를 만드는 class형성
class Family :
    def __init__(self) :
        # 다음의 class들을 속성으로 취함
        self.group = Group() # Group의 class 불러옴
        self.group.layer.move(600, 200) # Group안에 있는 layer method 실행
        self.chick2 = Chicken() # Chicken class 불러옴
        self.chick2.layer.move(800, 200) # Chicken안에 있는 layer method 실행
        # 해당 layer들 추가
        canvas.add(self.group.layer)
        canvas.add(self.chick2.layer) 

# 닭과 병아리를 group으로 묶는 class 형성
class Group :
    def __init__(self) :
        # 다음의 class들을 속성으로 취함
        self.hen = Chicken(True) # True를 인자로 하는 Chicken class 불러옴
        self.chick1 = Chicken() 
        self.chick1.layer.move(120, 0) 
        self.layer = Layer() # layer속성 형성. 이 속성때문에 64번째랑 66번째 속성 실행 가능
        # Group이라는 layer형성 - 즉, 어미닭과 첫째 병아리를 group으로 설정
        self.layer.add(self.hen.layer)
        self.layer.add(self.chick1.layer)

# 닭과 병아리를 만드는 class 형성
class Chicken :
    def __init__(self, hen=False) :
        # 다음의 class들을 속성으로 취함
        self.body = Body(hen) 
        self.wing = Wing(hen) 
        self.eye = Eye(hen) 
        self.beak = Beak(hen) 
        self.dots = Dots(hen)
        self.layer = Layer() # layer 속성 취함
        self.layer.add(self.body.shape) # 몸, 날개, 눈, 부리, 벼슬을 하나의  layer로 만듦
        self.layer.add(self.wing.shape)
        self.layer.add(self.eye.shape)
        self.layer.add(self.beak.shape)
        self.layer.add(self.dots.shape)

# 몸을 만드는 class 형성
class Body :
    def __init__(self, hen) :

        if hen : # 어미 닭일 경우
            self.shape = Ellipse(70, 80)
            self.shape.setFillColor("white")
        else : # 병아리일 경우
            self.shape = Ellipse(40, 50)
            self.shape.setFillColor("yellow")
            self.shape.move(0, 10)
        self.shape.setBorderColor("yellow")
        self.shape.setDepth(20) # 깊이를 20으로 설정

# 날개를 만드는 class 형성
class Wing:
    def __init__(self, hen) :
        if hen : # 어미 닭일 경우
            self.shape = Ellipse(60, 40)
            self.shape.setFillColor("white")
            self.shape.setBorderColor("yellow")
            self.shape.move(15,20)
        else : # 병아리일 경우
            self.shape = Ellipse(30, 20)
            self.shape.setFillColor("yellow")
            self.shape.setBorderColor("orange")
            self.shape.move(10, 20)
            self.shape.adjustReference(-5, -5)
        self.shape.setDepth(19) # 깊이를 몸보다 앞으로 설정

    def flap(self, angle) : # 날개를 움직여야 하는 둘째 병아리의 경우를 위해 flap함수 설정
        self.shape.rotate(angle) # 돌려야 하는 각도를 인자로 하는 rotate를 method로 설정

# 눈을 만드는 class 형성
class Eye :
    def __init__(self, hen) :
        if hen : # 어미 닭일 경우
            
            self.shape = Circle()
            self.shape.setRadius(3)
            self.shape.moveTo(-15, -15)
            
        else : # 병아리일 경우
            self.shape = Circle()
            self.shape.setRadius(3)
            self.shape.moveTo(-5, 0)
        self.shape.setFillColor("black")
        self.shape.setBorderColor("black")
        self.shape.setDepth(18) # 역시 깊이를 몸보다 얕게한다.
        
# 부리를 만드는 class 형성
class Beak :
    def __init__(self, hen) :
        if hen : # 어미인 경우
            
            self.shape = Square(8)
            self.shape.move(-36, 0)
            
        else : # 병아리인 경우
            self.shape = Square(4)
            self.shape.move(-22, 10)

        self.shape.setFillColor("red")
        self.shape.setBorderColor("yellow")
        self.shape.setDepth(21) # 몸 뒤에 있어야 하므로 깊이 깊게 설정
        self.shape.rotate(45) # 마름모 모양으로 해 부리 모양 형성

# 벼슬을 만드는 class 형성
class Dots :
    def __init__(self, hen) :
        self.shape = Layer() # 두개의 벼슬을 만들어야 하므로 layer구성. 어미가 아닌 병아리의 경우도 shape이라는 속성을 가져야 하므로.
        if hen :
        
            self.dotss1 = Ellipse(5, 8)
            self.dotss2 = Ellipse(5, 8)
            self.dotss1.setFillColor("red")
            self.dotss2.setFillColor("red")
            self.dotss1.setBorderColor("red")
            self.dotss2.setBorderColor("red")
            self.dotss1.move(0, -42) # 벼슬의 위치를 다르게
            self.dotss2.move(-6, -42)
            self.dotss1.setDepth(22) # 몸 뒤에 있어야 하므로
            self.dotss2.setDepth(22)
            self.shape.add(self.dotss1)
            self.shape.add(self.dotss2)
        
# 닭과 병아리를 움직이게 하는 class 형성            
class Animation :
    def __init__(self, scene) :

        group, chicken, wing = scene.get_anim_data() # Scene class의 get_anim_data() 속성 실행, 닭과 첫째 병아리, 둘째 병아리와 그 날개를 산출
        # 다음의 속성을 만듦
        self.group = group
        self.chicken2 = chicken
        self.wing2 = wing
    # 닭과 첫째 병아리를 움직이게 하는 속성 구성
    def move_group(self) :
        
        for i in range(80) : # 무대 끝까지 가기 위한 반복문 구성
            time.sleep(0.06)
            self.group.move(-5, -2) # 위 아래로 움직여야 하므로
            self.group.move(-5, 2)
            if i == 30 : # group이 이만큼 위치했을 떄
                text1 = Text("OH!", 20)
                text1.move(800, 160)
                canvas.add(text1)
            elif i == 40 :
                canvas.remove(text1) # 다음 문구를 위해 제거
                text2 = Text("WHERE IS MY MOMMY GOING?", 30)
                text2.move(500, 100)
                canvas.add(text2)
            elif i == 55 :
                canvas.remove(text2)

    # 둘째 병아리를 움직이게 하는 속성 구성
    def move_chicken2(self) :
        text3 = Text("Wait for ME~", 25)
        text3.move(500, 100)
        canvas.add(text3)
        for j in range(10) : # 무대 끝까지 가기 위한 반복문 구성
            for i in range(5) : # 병아리가 날 때와 착지할 때의 날개의 각이 다르므로 두개의 반복문 구성
                time.sleep(0.06)
                # 병아리가 날떄  
                self.chicken2.move(-10, -20)
                self.wing2.flap(-10) 
            for i in range(5) :
                time.sleep(0.06)
                # 병아리가 착지할 때
                self.chicken2.move(-10, 20)
                self.wing2.flap(10)
        canvas.remove(text3)

main()













# 궁금한 점... -- layer를 만들면 위치를 다시 (0,0)으로 초기화되는가..?

