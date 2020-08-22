'''

Name: 조예성, 조수아, 김시우

Student ID: 21600685, 21700687, 21800111

Description: <Teamproject> 이 프로그램은 지각한 학생이 교수님의 차를 타고 격려를 받은 프로그램입니다.

'''

from cs1graphics import *
import time
canvas = Canvas(1000, 700)

# 장면 1: 지각이야!
class Scene1 :
    def __init__(self) :
        self.man = Man1()
        self.bed = Bed()
        self.window1 = Window1()
        self.table = Table()
        self.sun = Sun()
        self.door = Door()
        self.clock = Clock()

    def get_anim_data(self) :
        return self.man, self.bed.blanket, self.bed.bed, self.window1.window, self.table.drawer, self.sun.suns, self.door.doors, self.door.doors_sign, self.door.doors_hand, self.clock.clock


# 해
class Sun :
    def __init__(self) :
        self.suns = Circle(25, Point(150, 100))
        self.suns.setFillColor("red")
        self.suns.setBorderColor('orange')
        self.suns.setDepth(10)
        canvas.add(self.suns) # 추가

# 창문
class Window1 :
    def __init__(self) :
        self.window = Layer() # 겹

        # 창문 전체
        self.bigwindow = Rectangle(300, 300, Point(150, -150))
        self.bigwindow.setFillColor('Brown')
        self.window.add(self.bigwindow) # 겹 추가

        # 왼쪽 창문
        self.window1 = Rectangle(132.5, 280, Point(76.25, -150))
        self.window1.setFillColor('sky blue')
        self.window1.setDepth(30)
        self.window.add(self.window1) # 겹 추가
        # 오른쪽 창문
        self.window2 = Rectangle(132.5, 280, Point(225, -150))
        self.window2.setFillColor('sky blue')
        self.window2.setDepth(30)
        self.window.add(self.window2) # 겹 추가
        
        self.window.moveTo(100, 300)
        canvas.add(self.window) # 추가

# 서랍
class Table:
    def __init__(self) :
        self.drawer = Layer() # 겹

        # 서랍 앞면
        self.drawer1 = Rectangle(150, 200, Point(75, -100) )
        self.drawer1.setFillColor('rosybrown')
        self.drawer1.setDepth(60)
        self.drawer.add(self.drawer1) # 겹 추가

        # 서랍1
        self.door1 = Rectangle(130, 50, Point(75, -37.5) )
        self.door1.setFillColor('brown')
        self.door1.setDepth(30)
        self.drawer.add(self.door1) # 겹 추가
        # 서랍2
        self.door2 = Rectangle(130, 50, Point(75, -100) )
        self.door2.setFillColor('brown')
        self.door2.setDepth(30)
        self.drawer.add(self.door2) # 겹 추가
        # 서랍3
        self.door3 = Rectangle(130, 50, Point(75, -162.5))
        self.door3.setFillColor('brown')
        self.door3.setDepth(30)
        self.drawer.add(self.door3) # 겹 추가

        # 서랍 윗면
        self.upperside = Polygon(Point(0, -200), Point(50, -240), Point(200, -240), Point(150, -200))
        self.upperside.setFillColor('rosybrown')
        self.drawer.add(self.upperside) # 겹 추가

        # 서랍 우측면
        self.rightside = Polygon(Point(150, -200), Point(200, -240), Point(200, -40), Point(150, 0))
        self.rightside.setFillColor('rosybrown')
        self.drawer.add(self.rightside) # 겹 추가
        
        self.drawer.moveTo(500, 450)
        canvas.add(self.drawer) # 추가

# 시계
class Clock :
    def __init__(self) :
        self.clock = Layer() # 겹

        # 시계 몸통
        self.clocks = Circle(35, Point(0, 0))
        self.clocks.setFillColor('gray')
        self.clocks.setDepth(60)
        self.clock.add(self.clocks) # 겹 추가

        # 시계 윤곽선
        self.line1 = Polygon(Point(0, 0), Point(-20, 15))
        self.line2 = Polygon(Point(0, 0), Point(20, 20))
        self.line3 = Polygon(Point(0, 0), Point(-25, 44))
        self.line4 = Polygon(Point(0, 0), Point(25, 44))
        self.line3.setDepth(80)
        self.line4.setDepth(80)
        self.clock.add(self.line1) # 겹 추가 
        self.clock.add(self.line2) # 겹 추가
        self.clock.add(self.line3) # 겹 추가
        self.clock.add(self.line4) # 겹 추가

        # 시계 손잡이
        self.handline = Circle(22, Point(0, -35))
        self.handline.setDepth(80)
        self.clock.add(self.handline) # 겹 추가

        # 시계 벨1
        self.bell1 = Circle(10, Point(-17.5, -35))
        self.bell1 = Circle(10, Point(-17.5, -35))
        self.bell1.setFillColor('gray')
        self.bell1.setDepth(-10)
        self.clock.add(self.bell1) # 겹 추가
        # 시계 벨2
        self.bell2 = Circle(10, Point(17.5, -35))
        self.bell2.setFillColor('gray')
        self.bell2.setDepth(-10)
        self.clock.add(self.bell2) # 겹 추가
        
        self.clock.moveTo(600, 200)
        canvas.add(self.clock) # 추가 

# 침대
class Bed :
    def __init__(self) :
        self.bed = Layer() # 겹

        # 침대 매트리스1
        self.mat1 = Rectangle(400, 50, Point(200, -25))
        self.mat1.setFillColor('white')
        self.bed.add(self.mat1) # 겹 추가
        # 침대 매트리스2
        self.mat2 = Polygon(Point(0, -50), Point(400, -50), Point(440, -180), Point(40, -180))
        self.mat2.setFillColor('white')
        self.bed.add(self.mat2) # 겹 추가
        # 침대 매트리스3
        self.mat3 = Polygon(Point(400, 0), Point(400, -50), Point(440, -180), Point(440, -130))
        self.mat3.setFillColor('white')
        self.bed.add(self.mat3) # 겹 추가
        
        # 침대 모형1
        self.wood1 = Polygon(Point(0, -50), Point(40, -180), Point(40, -280), Point(0, -150))
        self.wood1.setFillColor('brown')
        self.bed.add(self.wood1) # 겹 추가
        # 침대 모형2
        self.wood2 = Polygon(Point(40, -280), Point(0, -150), Point(-15, -150), Point(25,-280 ))
        self.wood2.setFillColor('brown')
        self.bed.add(self.wood2) # 겹 추가
        self.bed.moveTo(300,400)
        # 침대 모형3
        self.wood3 = Polygon(Point(0, -150), Point(-15, -150), Point(-15, 150), Point(0, 150))
        self.wood3.setFillColor('brown')
        self.bed.add(self.wood3) # 겹 추가
        # 침대 모형4
        self.wood4 = Rectangle(400, 150, Point(200, 75))
        self.wood4.setFillColor('brown')
        self.bed.add(self.wood4) # 겹 추가
        # 침대 모형5
        self.wood5 = Polygon(Point(400, 0), Point(440, -130), Point(440, -40), Point(400, 150))
        self.wood5.setFillColor('brown')
        self.bed.add(self.wood5) # 겹 추가
        
        self.bed.scale(0.8)
        self.bed.moveTo(50, 600)
        self.bed.setDepth(60)
        canvas.add(self.bed) # 추가
        
        # 담요
        self.blanket = Rectangle(200, 145, Point(300, 500))
        self.blanket.setFillColor("tan")
        self.blanket.setBorderColor("tan")
        self.blanket.setDepth(10)
        canvas.add(self.blanket) # 추가

        
# 주인공 
class Man1 :
    def __init__(self) :
        self.guy = Layer() # 겹

        # 주인공 겹 구성
        self.face = Face()
        self.eyes = Eyes()
        self.mouth = Mouth()
        self.body = Body()
        self.arms = Arms()
        self.hands = Hands()
        # 겹 추가
        self.guy.add(self.face.faces)
        self.guy.add(self.eyes.eyes1)
        self.guy.add(self.eyes.eyes2)
        self.guy.add(self.mouth.mouth1)
        self.guy.add(self.body.bodys)
        self.guy.add(self.arms.arm1)
        self.guy.add(self.arms.arm2)
        self.guy.add(self.hands.hand1)
        self.guy.add(self.hands.hand2)
        
        self.guy.move(200, 500)
        canvas.add(self.guy) # 추가

    # 움직이는 주인공
    def moving(self, angle) :
        self.guy.rotate(angle)

# 주인공 얼굴
class Face :
    def __init__(self) :
        self.faces = Circle(50, Point(-100, 0))
        self.faces.setBorderColor("bisque")
        self.faces.setFillColor("bisque")
        self.faces.setDepth(17)

# 주인공 눈
class Eyes :
    def __init__(self) :
        # 주인공 왼 눈
        self.eyes1 = Path(Point(30, 70), Point(30, 90))
        self.eyes1.setBorderColor("black")
        self.eyes1.setBorderWidth(6)
        self.eyes1.setDepth(15)
        self.eyes1.move(-140, -60)
        # 주인공 오른쪽 눈
        self.eyes2 = Path(Point(30, 70), Point(30, 90))
        self.eyes2.setBorderColor("black")
        self.eyes2.setBorderWidth(6)
        self.eyes2.setDepth(15)
        self.eyes2.move(-140, -100)

# 주인공 입
class Mouth :
    def __init__(self) :
        self.mouth1 = Circle(10, Point(-70, -3))
        self.mouth1.setFillColor("black")
        self.mouth1.setDepth(15)

# 주인공 몸체
class Body :
    def __init__(self) :
        self.bodys = Ellipse(200, 80, Point(10, 0))
        self.bodys.setBorderColor("red")
        self.bodys.setFillColor("red")
        self.bodys.setDepth(19)

# 주인공 팔
class Arms :
    def __init__(self) :
        # 주인공 왼팔
        self.arm1 = Ellipse(100, 30, Point(-10, -60))
        self.arm1.rotate(-33)
        self.arm1.setBorderColor("orange")
        self.arm1.setFillColor("orange")
        self.arm1.setDepth(18)
        # 주인공 오른팔
        self.arm2 = Ellipse(100, 30, Point(-10, 60))
        self.arm2.rotate(33)
        self.arm2.setBorderColor("orange")
        self.arm2.setFillColor("orange")
        self.arm2.setDepth(16)

    # 움직이는 팔
    def movings(self, angle) :
        self.arm1.rotate(angle)
        self.arm2.rotate(-angle)

# 주인공 손
class Hands :
    def __init__(self) :
        # 주인공 왼손
        self.hand1 = Circle(15, Point (23, 77))
        self.hand1.setBorderColor("bisque")
        self.hand1.setFillColor("bisque")
        self.hand1.setDepth(14)
        # 주인공 오른손
        self.hand2 = Circle(15, Point(20, -80))
        self.hand2.setBorderColor("bisque")
        self.hand2.setFillColor("bisque")
        self.hand2.setDepth(14)

# 방 문
class Door :
    def __init__(self) :
        # 문 틀
        self.doors = Rectangle(190, 400, Point(910, 590))
        self.doors.setFillColor("chocolate")
        self.doors.setBorderColor("black")
        canvas.add(self.doors) # 겹 추가
        
        # 문
        self.doors_sign = Rectangle(170, 380, Point(910, 590))
        self.doors_sign.setBorderColor("black")
        canvas.add(self.doors_sign) # 겹 추가
        
        # 문 손잡이
        self.doors_hand = Circle(10, Point(840, 550))
        self.doors_hand.setFillColor("black")
        self.doors_hand.setDepth(10)
        canvas.add(self.doors_hand) # 겹 추가


# 장면 1, 애니메이션
class Animation :
    def __init__(self, scene1) :
        man, blanket, bed, window, table, sun, door, door_sign, door_hand, clock= scene1.get_anim_data()
        self.mans = man
        self.blankets = blanket
        self.beds = bed
        self.clock = clock
        self.table = table
        self.suns = sun
        self.window = window
        self.doors = door
        self.doors_sign = door_sign
        self.doors_hand = door_hand

    def move_man(self) :
        text = Text("08 : 20", 25, Point(600, 100))
        text.setFontColor('red')
        canvas.add(text) # 추가
        for i in range(50) :
            if i == 10 :
                text1 = Text("Z", 30)
                text1.move(100, 400)
                canvas.add(text1) # 추가
            elif i == 30 :
                time.sleep(1)
                text1.move(20, -20)
            elif i == 45 :
                time.sleep(1)
                text1.move(20, -20)
                time.sleep(2)
                canvas.remove(text1) # 사라짐
                time.sleep(1)
        text4 = Text(" (( ", 30, Point(500, 200))
        text5 = Text(" )) ", 30, Point(700, 200))
        canvas.add(text4) # 추가
        canvas.add(text5) # 추가
        time.sleep(1)
        canvas.remove(text4) # 사라짐
        canvas.remove(text5) # 사라짐
        time.sleep(1)
        canvas.add(text4) # 추가
        canvas.add(text5) # 추가
        time.sleep(1)
        canvas.remove(text4) # 사라짐
        canvas.remove(text5) # 사라짐
        time.sleep(0.5)
        for i in range(10) :
            self.mans.moving(2.25)
            self.blankets.move(1, 0)
            time.sleep(0.06)
            self.mans.moving(2.25)
            self.blankets.move(1, 0)
        time.sleep(2)
        text3 = Text("....", 30, Point(50, 380))
        canvas.add(text3) # 추가
        time.sleep(3)
        canvas.remove(text3) # 사라짐
        text2 = Text("!!", 40, Point(50, 400))
        canvas.add(text2) # 추가
        time.sleep(2)
        
        # 배경 전환을 위한 사라짐
        canvas.remove(text2)
        canvas.remove(self.mans.guy)
        canvas.remove(self.blankets)
        canvas.remove(self.beds)
        canvas.remove(self.suns)
        canvas.remove(self.doors)
        canvas.remove(self.doors_sign)
        canvas.remove(self.doors_hand)
        canvas.remove(self.window)
        canvas.remove(self.clock)
        canvas.remove(self.table)
        canvas.remove(text)
        
def animate_man(scene1) :
    animation = Animation(scene1)
    animation.move_man()



# 장면 2: 눈 앞에서 차를 놓치다!
class Scene2 :
    def __init__(self) :
        self.sun = Sun2()
        self.ground = Ground()
        self.man = Man2()
        self.people = People()
        self.bus = Bus()
        self.station = Station()
        self.car = Car()
        self.tree = Tree()
        self.trees = Trees()
        self.building = Building()
        self.bird = Bird()
        
    def getting_anim_data(self) :
        return self.man, self.bus, self.people, self.car, self.sun, self.ground, self.station, self.tree.trees, self.trees.trees, self.building.building, self.bird


# 해
class Sun2 :
    def __init__(self) :
        self.sun = Circle(130, Point(35, 10))
        self.sun.setFillColor("red")
        self.sun.setBorderColor("orange")
        self.sun.setDepth(10)
        canvas.add(self.sun) # 추가

# 땅
class Ground :
    def __init__(self) :
        self.ground = Rectangle(1000, 350, Point(500, 700))
        self.ground.setFillColor("light green")
        self.ground.setBorderColor("black")
        self.ground.setDepth(60)
        canvas.add(self.ground) # 추가
        
# 주인공
class Man2 :
    def __init__(self) :
        self.guy2 = Layer() # 겹

        # 주인공 겹 구성
        self.faces2 = Face2()
        self.eyes2 = Eyes2()
        self.mouth2 = Mouth2()
        self.body2 = Body2()
        self.arms2 = Arms2()
        self.hands2 = Hand2()
        self.legs = Legs()
        # 겹 추가
        self.guy2.add(self.faces2.faces2)
        self.guy2.add(self.eyes2.eyes1)
        self.guy2.add(self.eyes2.eyes2)
        self.guy2.add(self.mouth2.mouth2)
        self.guy2.add(self.body2.bodys2)
        self.guy2.add(self.arms2.arms1)
        self.guy2.add(self.arms2.arms2)
        self.guy2.add(self.hands2.hands1)
        self.guy2.add(self.hands2.hands2)
        self.guy2.add(self.legs.leg1)
        self.guy2.add(self.legs.leg2)
        
        self.guy2.move(100, 500)
        self.guy2.setDepth(40)
        canvas.add(self.guy2) # 추가

    # 움직이는 주인공
    def moving(self, x) :
        self.guy2.move(x, 0)

# 주인공 얼굴
class Face2 :
    def __init__(self) :
        self.faces2 = Circle(30, Point(0, -60))
        self.faces2.setFillColor("bisque")
        self.faces2.setBorderColor("bisque")
        self.faces2.setDepth(30)

# 주인공 눈
class Eyes2 :
    def __init__(self) :
        # 주인공 왼쪽 눈
        self.eyes1 = Circle(3, Point(10, -65))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        # 주인공 오른쪽 눈
        self.eyes2 = Circle(3, Point(-10, -65))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(10)
        
# 주인공 입
class Mouth2 :
    def __init__(self) :
        self.mouth2 = Rectangle(20, 10, Point(0, -43))
        self.mouth2.setFillColor("black")
        self.mouth2.setBorderColor("black")
        self.mouth2.setDepth(3)

# 주인공 몸체
class Body2 :
    def __init__(self) :
        self.bodys2 = Ellipse(30, 100, Point(0, -21))
        self.bodys2.setFillColor("salmon")
        self.bodys2.setBorderColor("salmon")
        self.bodys2.setDepth(32)

# 주인공 팔
class Arms2 :
    def __init__(self) :
        # 주인공 왼팔
        self.arms1 = Ellipse(15, 50, Point(-27, -9))
        self.arms1.setFillColor("orange")
        self.arms1.setBorderColor("orange")
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        # 주인공 오른팔
        self.arms2 = Ellipse(15, 50, Point(25, -9))
        self.arms2.setFillColor("orange")
        self.arms2.setBorderColor("orange")
        self.arms2.rotate(-30)
        self.arms2.setDepth(34)

    # 움직이는 팔
    def shakings(self, angle) :
        self.arms1.rotate(angle)
        self.arms2.rotate(-angle)

# 주인공 손
class Hand2 :
    def __init__(self) :
        # 주인공 왼손
        self.hands1 = Circle(9, Point(-37, 10))
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        # 주인공 오른손
        self.hands2 = Circle(9, Point(37, 10))
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)

    # 움직이는 손
    def shakings(self, angle) :
        self.hands1.rotate(angle)
        self.hands2.rotate(-angle)

# 주인공 다리        
class Legs :
    def __init__(self) :
        # 주인공 왼쪽 다리
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("dark blue")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(-5, 15)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        # 주인공 오른쪽 다리
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("dark blue")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(5, 15)
        self.leg2.rotate(-19)
        self.leg2.setDepth(34)

    # 움직이는 다리
    def shakings(self, angle) :
        self.leg1.rotate(angle)
        self.leg2.rotate(-angle)

# 사람들
class People :
    def __init__(self) :
        self.person1 = Person1()
        self.person2 = Person2()

# 사람1
class Person1 :
    def __init__(self) :
        self.guy3 = Layer() # 겹

        # 사람1 겹 구성
        self.face3 = Face3()
        self.eyes3 = Eyes3()
        self.mouth3 = Mouth3()
        self.body3 = Body3()
        self.arms3 = Arms3()
        self.hands3 = Hand3()
        self.legs3 = Legs3()
        # 겹 추가
        self.guy3.add(self.face3.faces3)
        self.guy3.add(self.eyes3.eyes1)
        self.guy3.add(self.eyes3.eyes2)
        self.guy3.add(self.mouth3.mouth3)
        self.guy3.add(self.body3.bodys3)
        self.guy3.add(self.arms3.arms1)
        self.guy3.add(self.arms3.arms2)
        self.guy3.add(self.hands3.hands1)
        self.guy3.add(self.hands3.hands2)
        self.guy3.add(self.legs3.leg1)
        self.guy3.add(self.legs3.leg2)

        self.guy3.move(600, 500)
        self.guy3.setDepth(30)
        canvas.add(self.guy3) # 추가

# 사람1 얼굴
class Face3 :
    def __init__(self) :
        self.faces3 = Circle(30, Point(0, -60))
        self.faces3.setFillColor("bisque")
        self.faces3.setBorderColor("bisque")
        self.faces3.setDepth(30)

# 사람1 눈
class Eyes3 :
    def __init__(self):
        # 사람1 왼쪽 눈
        self.eyes1 = Circle(3, Point(10, -65))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        # 사람1 오른쪽 눈
        self.eyes2 = Circle(3, Point(-10, -65))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(29)

# 사람1 입
class Mouth3 :
    def __init__(self) :
        self.mouth3 = Rectangle(20, 10, Point(0, -43))
        self.mouth3.setFillColor("black")
        self.mouth3.setBorderColor("black")
        self.mouth3.setDepth(3)

# 사람1 몸
class Body3 :
    def __init__(self) :
        self.bodys3 = Ellipse(30, 100, Point(0, -3))
        self.bodys3.setFillColor("yellow")
        self.bodys3.setBorderColor("yellow")
        self.bodys3.setDepth(32)

# 사람1 팔
class Arms3 :
    def __init__(self) :
        # 사람1 왼팔
        self.arms1 = Ellipse(15, 50, Point(-27, -9))
        self.arms1.setFillColor("red")
        self.arms1.setBorderColor("red")
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        # 사람1 왼팔
        self.arms2 = Ellipse(15, 50, Point(25, -9))
        self.arms2.setFillColor("red")
        self.arms2.setBorderColor("red")
        self.arms2.rotate(-30)
        self.arms2.setDepth(30)

# 사람1 손
class Hand3 :
    def __init__(self) :
        # 사람1 왼손
        self.hands1 = Circle(7, Point(-37, 7))
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        # 사람1 오른손
        self.hands2 = Circle(7, Point(37, 7))
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)

# 사람1 다리
class Legs3 :
    def __init__(self) :
        # 사람1 왼쪽 다리
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("khaki")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(-5, 35)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        # 사람1 오른쪽 다리
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("khaki")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(5, 35)
        self.leg2.rotate(-19)
        self.leg2.setDepth(30)

# 사람2
class Person2 :
    def __init__(self) :
        self.guy4 = Layer() # 겹

        # 사람2 겹 구성
        self.face4 = Face4()
        self.eyes4 = Eyes4()
        self.mouth4 = Mouth4()
        self.body4 = Body4()
        self.arms4 = Arms4()
        self.hands4 = Hand4()
        self.legs4 = Legs4()
        # 사람2 겹 추가
        self.guy4.add(self.face4.faces4)
        self.guy4.add(self.eyes4.eyes1)
        self.guy4.add(self.eyes4.eyes2)
        self.guy4.add(self.mouth4.mouth4)
        self.guy4.add(self.body4.bodys4)
        self.guy4.add(self.arms4.arms1)
        self.guy4.add(self.arms4.arms2)
        self.guy4.add(self.hands4.hands1)
        self.guy4.add(self.hands4.hands2)
        self.guy4.add(self.legs4.leg1)
        self.guy4.add(self.legs4.leg2)
        
        self.guy4.move(650, 500)
        self.guy4.setDepth(30)
        canvas.add(self.guy4) # 추가

# 사람2 얼굴
class Face4 :
    def __init__(self) :
        self.faces4 = Circle(30, Point(50, -60))
        self.faces4.setFillColor("bisque")
        self.faces4.setBorderColor("bisque")
        self.faces4.setDepth(30)
        
# 사람2 눈
class Eyes4 :
    def __init__(self):
        # 사람2 왼쪽 눈
        self.eyes1 = Circle(3, Point(60, -65))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        # 사람2 오른쪽 눈
        self.eyes2 = Circle(3, Point(40, -65))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(29)
        
# 사람2 입
class Mouth4 :
    def __init__(self) :
        self.mouth4 = Rectangle(20, 10, Point(50, -43))
        self.mouth4.setFillColor("black")
        self.mouth4.setBorderColor("black")
        self.mouth4.setDepth(3)

# 사람2 몸체
class Body4 :
    def __init__(self) :
        self.bodys4 = Ellipse(30, 100, Point(50, -3))
        self.bodys4.setFillColor("brown")
        self.bodys4.setBorderColor("brown")
        self.bodys4.setDepth(32)

# 사람2 팔
class Arms4 :
    def __init__(self) :
        # 사람2 왼팔
        self.arms1 = Ellipse(15, 50, Point(23, -9))
        self.arms1.setFillColor("blue")
        self.arms1.setBorderColor("blue")
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        # 사람2 오른팔
        self.arms2 = Ellipse(15, 50, Point(75, -9))
        self.arms2.setFillColor("blue")
        self.arms2.setBorderColor("blue")
        self.arms2.rotate(-30)
        self.arms2.setDepth(30)

# 사람2 손
class Hand4 :
    def __init__(self) :
        # 사람2 왼손
        self.hands1 = Circle(7, Point(13, 7))
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        # 사람2 오른손
        self.hands2 = Circle(7, Point(87, 7))
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)

# 사람2 다리
class Legs4 :
    def __init__(self) :
        # 사람2 왼쪽 다리 
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("tan")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(45, 35)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        # 사람2 오른쪽 다리
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("tan")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(55, 35)
        self.leg2.rotate(-19)
        self.leg2.setDepth(30)

# 1번 나무
class Tree :
    def __init__(self) :
        self.trees = Layer() # 겹

        # 나무 겹 구성
        self.tree1 = Tree1()
        self.t_root1 = T_root1()
        self.leaf = Leaf()
        # 겹 추가
        self.trees.add(self.tree1.tree1s)
        self.trees.add(self.t_root1.t_root1s)
        self.trees.add(self.leaf.leafs)
        
        self.trees.moveTo(880, 580)
        self.trees.setDepth(60)
        canvas.add(self.trees) # 추가

# 나무 기둥
class Tree1 :
    def __init__(self) :
        self.tree1s = Rectangle(80, 200, Point(0, -100))
        self.tree1s.setFillColor("brown")

# 나무 뿌리
class T_root1 :
    def __init__(self) :
        self.t_root1s = Polygon(Point(-70, 0), Point(70, 0), Point(0, -50))
        self.t_root1s.setFillColor('brown')
        self.t_root1s.setDepth(60)
        
# 나뭇잎
class Leaf :
    def __init__(self) :
        self.leafs = Circle(80, Point(0, -200))
        self.leafs.setFillColor('dark green')

# 2번 나무
class Trees :
    def __init__(self) :
        self.trees = Layer() # 겹

        # 나무 겹 구성
        self.tree1 = Tree1()
        self.t_root1 = T_root1()
        self.leaf = Leaf()
        # 겹 추가
        self.trees.add(self.tree1.tree1s)
        self.trees.add(self.t_root1.t_root1s)
        self.trees.add(self.leaf.leafs)
        
        self.trees.moveTo(660, 580)
        self.trees.setDepth(60)
        canvas.add(self.trees) # 추가                

# 학교 버스
class Bus :
    def __init__(self):
        self.bus = Layer() # 겹

        # 버스 몸통
        self.busbody = Rectangle(400, 250, Point(200, -125))
        self.busbody.setFillColor('darkblue')
        self.bus.add(self.busbody) # 겹 추가
        
        # 버스 창문1
        self.window1 = Rectangle(150, 100, Point(100, -170))
        self.window1.setFillColor('lightskyblue')
        self.bus.add(self.window1) # 겹 추가     
        # 버스 창문2
        self.window2 = Rectangle(150, 100, Point(200, -170))
        self.window2.setFillColor('lightskyblue')
        self.bus.add(self.window2) # 겹 추가        
        # 버스 창문3
        self.window3 = Rectangle(150, 100, Point(300, -170))
        self.window3.setFillColor('lightskyblue')
        self.bus.add(self.window3) # 겹 추가

        # 버스 타이어1
        self.tire1 = Circle(50, Point(100, 0))
        self.tire1.setFillColor('black')
        self.bus.add(self.tire1) # 겹 추가
        # 버스 타이어2
        self.tire2 = Circle(50, Point(300, 0))
        self.tire2.setFillColor('black')
        self.bus.setDepth(10)
        self.bus.add(self.tire2) # 겹 추가
        
        # 버스 문구1
        self.text1 = Text('한동대학교 유산균 출시!', 50, Point(195, -50))
        self.text1.setFontColor('white')
        self.text1.setFontSize(30)
        self.text1.setDepth(-40)
        self.bus.add(self.text1) # 겹 추가
       # 버스 문구2
        self.text2 = Text('Why Not Change the World?', 50, Point(195, -95))
        self.text2.setFontColor('white')
        self.text2.setFontSize(20)
        self.text2.setDepth(-40)
        self.bus.add(self.text2) # 겹 추가
        
        self.bus.moveTo(-400, 550)
        canvas.add(self.bus) # 추가
        
    # 움직이는 버스
    def moving(self, x) :
        self.bus.move(x, 0)

# 하나로마트
class Building:
    def __init__(self) :
        self.building = Layer() # 겹

        # 건물
        self.sq1 =Rectangle(600, 500, Point(300, -275))
        self.sq1.setFillColor('lightgray')
        self.building.add(self.sq1) # 겹 추가
        
        # 건물 창문1
        self.window1 = Rectangle(450,100, Point(300 ,-80))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1) # 겹 추가
        # 건물 창문2
        self.window1 = Rectangle(450,100, Point(300 ,-210))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1) # 겹 추가
        # 건물 창문3
        self.window1 = Rectangle(450,100, Point(300 ,-340))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1) # 겹 추가

        # 건물 간판
        self.sign = Rectangle(450, 80, Point(300, -450))
        self.sign.setFillColor('green')
        self.sign.setDepth(-20)
        self.building.add(self.sign) # 겹 추가

        # 건물 이름
        self.text = Text('NH하나로마트', 80, Point(300, -450))
        self.text.setFontColor('white')
        self.text.setFontSize(60)
        self.text.setDepth(-40)
        self.building.add(self.text) # 겹 추가
        
        self.building.moveTo(70, 560)
        self.building.setDepth(80)
        canvas.add(self.building) # 추가

# 버스 정류장
class Station:
    def __init__(self) :
        self.station = Layer() # 겹

        # 버스 정류장 기둥1
        self.station1 = Rectangle(24, 240, Point(12, -120) )
        self.station1.setFillColor('white')
        self.station1.setDepth(60)
        self.station.add(self.station1) # 겹 추가
        # 버스 정류장 기둥2
        self.station2 = Rectangle(240, 40, Point(120, -228))
        self.station2.setFillColor('white')
        self.station2.setDepth(60)
        self.station.add(self.station2) # 겹 추가
        # 버스 정류장 기둥3
        self.station3 = Rectangle(24, 240, Point(226, -120) )
        self.station3.setFillColor('white')
        self.station3.setDepth(70)
        self.station.add(self.station3) # 겹 추가

        # 버스 정류장 표시1
        self.sign = Rectangle(50, 240, Point(360, -120))
        self.sign.setFillColor('white')
        self.sign.setDepth(30)
        self.station.add(self.sign) # 겹 추가
        # 버스 정류장 표시2
        self.sign2 = Circle(50, Point(360, -240))
        self.sign2.setFillColor('blue')
        self.sign2.setDepth(30)
        self.station.add(self.sign2) # 겹 추가

        
        self.minibus = Layer() # 겹

        # 간판 버스 그림 몸통
        self.busbody = Rectangle(60,40, Point(0, -15))
        self.busbody.setFillColor('white')
        self.minibus.add(self.busbody) # 겹 추가
        
        # 간판 버스 그림 타이어1
        self.tire = Circle(10, Point(-15,10))
        self.tire.setFillColor('black')
        self.minibus.add(self.tire) # 겹 추가
        # 간판 버스 그림 타이어2
        self.tire2 = Circle(10, Point(15, 10))
        self.tire2.setFillColor('black')
        self.minibus.add(self.tire2) # 겹 추가
        
        # 간판 버스 그림 표시
        self.text = Text('BUS', 20, Point(0, -15))
        self.text.setDepth(-20)
        self.minibus.add(self.text) # 겹 추가
        
        self.station.moveTo(535, 590)
        self.minibus.moveTo(360, -220)
        self.minibus.setDepth(-20)
        self.station.add(self.minibus) # 겹 추가
        canvas.add(self.station) # 추가

# 교수님 차
class Car:
    def __init__(self) :
        self.car = Layer() # 겹

        # 교수님 차 몸통
        self.carbody = Rectangle(250, 80, Point(100, -30))
        self.carbody.setFillColor('black')
        self.car.add(self.carbody) # 겹 추가

        # 교수님 차 지붕
        self.carhead = Polygon(Point(30,-70), Point(180, -70), Point(140, -115), Point(60, -115))
        self.carhead.setFillColor('black')
        self.carhead.setDepth(50)
        self.car.add(self.carhead) # 겹 추가

        # 교수님 차 타이어1
        self.tire1 = Circle(20, Point(40, 10))
        self.tire1.setFillColor('gray')
        self.car.add(self.tire1) # 겹 추가
        # 교수님 차 타이어2
        self.tire2 = Circle(20, Point(160,10))
        self.tire2.setFillColor('gray')
        self.car.add(self.tire2) # 겹 추가

        # 교수님 차 창문
        self.window = Polygon(Point(45, -75), Point(160,-75), Point(140, -105), Point(60, -105)) 
        self.window.setFillColor('skyblue')
        self.car.add(self.window) # 겹 추가

        # 교수님 차 문 손잡이 
        self.hand = Circle(7, Point(120, -25) )
        self.hand.setFillColor('white')
        self.hand.setDepth(-10)
        self.car.add(self.hand) # 겹 추가

        # 교수님 차 등
        self.light = Rectangle(20, 40, Point(190, -25))
        self.light.setFillColor('yellow')
        self.light.setDepth(-10)
        self.car.add(self.light) # 겹 추가
        
        self.car.moveTo(-250, 560)
        self.car.setDepth(10)
        canvas.add(self.car) # 추가

    # 움직이는 교수님 차
    def moving(self, x) :
        self.car.move(x, 0)

# 새
class Bird:
    def __init__(self):
        self.bird = Layer() # 겹

        # 새 얼굴
        self.face = Circle(23, Point(23, -23))
        self.face.setFillColor('red')
        self.face.setBorderWidth(2)
        self.face.setDepth(60)
        self.bird.add(self.face) # 겹 추가

        # 새 머리1
        self.hair1 = Ellipse(10, 20, Point(30, -46))
        self.hair1.setFillColor('red')
        self.hair1.setBorderWidth(2)
        self.bird.add(self.hair1) # 겹 추가
        # 새 머리2
        self.hair2 = Ellipse(10,20, Point(33, -46))
        self.hair2.setFillColor('red')
        self.hair1.setBorderWidth(2)
        self.hair2.rotate(45)
        self.bird.add(self.hair2) # 겹 추가
        
        # 새 눈썹1
        self.eyebrow1 = Polygon(Point(0, -23), Point(12,-22), Point(5, -29))
        self.eyebrow1.setFillColor('black')
        self.bird.add(self.eyebrow1) # 겹 추가
        # 새 눈썹2
        self.eyebrow1 = Polygon(Point(23, -23), Point(12,-22), Point(17, -29))
        self.eyebrow1.setFillColor('black')
        self.bird.add(self.eyebrow1) # 겹 추가

        # 새 왼쪽 눈
        self.eye1 = Circle(4, Point(8,-20))
        self.eye1.setFillColor('white')
        self.eye1.setDepth(60)
        self.bird.add(self.eye1) # 겹 추가
        # 새 오른쪽 눈
        self.eye2 = Circle(4, Point(16,-20))
        self.eye2.setFillColor('white')
        self.eye2.setDepth(60)
        self.bird.add(self.eye2) # 겹 추가
        # 새 왼쪽 눈동자
        self.eye3 = Circle(1, Point(9, -19))
        self.eye3.setFillColor('black')
        self.bird.add(self.eye3) # 겹 추가
        # 새 오른쪽 눈동자
        self.eye4 = Circle(1, Point(14, -19))
        self.eye4.setFillColor('black')
        self.bird.add(self.eye4) # 겹 추가

        # 새 부리1
        self.mouth1 = Ellipse(23, 14, Point(23, -7))
        self.mouth1.setFillColor('white')
        self.bird.add(self.mouth1) # 겹 추가
        # 새 부리2
        self.mouth2 = Polygon(Point(12, -15), Point(16, -8), Point(4,-8))
        self.mouth2.setFillColor('yellow')
        self.bird.add(self.mouth2) # 겹 추가
        # 새 부리3
        self.mouth3 = Polygon(Point(12, -3), Point(16, -8), Point(5,-8))
        self.mouth3.setFillColor('yellow')
        self.bird.add(self.mouth3) # 겹 추가

        # 새 꼬리1
        self.tale = Polygon(Point(45,-23), Point(52, -27), Point(50, -29))
        self.tale.setFillColor('black')
        self.bird.add(self.tale) # 겹 추가
        # 새 꼬리2
        self.tale2 = Polygon(Point(45,-23), Point(52, -19), Point(50, -17))
        self.tale2.setFillColor('black')
        self.bird.add(self.tale2) # 겹 추가
        # 새 꼬리3
        self.tale3 = Polygon(Point(45,-23), Point(54, -21), Point(54, -23))
        self.tale3.setFillColor('black')
        self.bird.setDepth(20)
        self.bird.add(self.tale3) # 겹 추가
        
        self.bird.moveTo(800, 100)
        canvas.add(self.bird) # 추가

    # 움직이는 새
    def moving(self, x) :
        self.bird.move(-x, 2*x)
    def moving2(self, x) :
        self.bird.move(-x, -4*x)


# 장면 2, 애니메이션
class Animation2 :
    def __init__(self, scene2) :
        man, bus, people, car, sun, ground, station, tree, trees, building, bird = scene2.getting_anim_data()
        self.suns = sun
        self.mans = man
        self.bus = bus
        self.peoples = people
        self.car = car
        self.grounds = ground
        self.stations = station
        self.tree = tree
        self.trees = trees
        self.building = building
        self.bird = bird

    # 팔의 기준축 -- adjustReference를 한 번 이용해보자!
    def animating(self) :
        self.mans.arms2.arms1.adjustReference(0, -12)
        self.mans.arms2.arms2.adjustReference(0, -12)
        self.mans.hands2.hands1.adjustReference(0, -30)
        self.mans.hands2.hands2.adjustReference(0, -30)
        self.mans.legs.leg1.adjustReference(1, -12)
        self.mans.legs.leg2.adjustReference(1, -12)

        for i in range(18) :
            time.sleep(0.15)
            self.bird.moving(7)
            
        for i in range(6):
            time.sleep(0.5)
            self.mans.moving(5)
            self.mans.arms2.shakings(-7)
            self.mans.hands2.shakings(-7)
            self.mans.legs.shakings(-10)
            
        for i in range(8) :
            time.sleep(0.5)
            self.mans.moving(5)
            self.mans.arms2.shakings(7)
            self.mans.hands2.shakings(7)
            self.mans.legs.shakings(10)
        
        for i in range(10) :
            time.sleep(0.3)
            self.bus.moving(70)
        
        time.sleep(1)
        canvas.remove(self.peoples.person1.guy3) # 사라짐
        canvas.remove(self.peoples.person2.guy4) # 사라짐
        
        time.sleep(1)
        text = Text("what..?", 20, Point(200, 380))
        canvas.add(text) # 추가
        time.sleep(1)
        canvas.remove(text) # 사라짐
        text1 = Text("Wait!!", 30, Point(200, 380))
        canvas.add(text1) # 추가
        time.sleep(0.5)
        canvas.remove(text1) # 사라짐
        
        for i in range(10) :
            time.sleep(0.1)
            self.mans.moving(9)
            self.mans.arms2.shakings(-8)
            self.mans.hands2.shakings(-8)
            self.mans.legs.shakings(-10)
            
        for i in range(10) :
            time.sleep(0.1)
            self.mans.moving(9)
            self.mans.arms2.shakings(8)
            self.mans.hands2.shakings(8)
            self.mans.legs.shakings(10)
            
        for i in range(20) :
            time.sleep(0.09)
            self.bus.moving(80)
        time.sleep(2)
        
        for i in range(15) :
            self.mans.arms2.shakings(10)
            self.mans.hands2.shakings(12)

        # 속상한 눈썹1
        change_eye1 = Rectangle(15, 5, Point(335, 429))
        change_eye1.setFillColor("black")
        change_eye1.setBorderColor("black")
        change_eye1.rotate(-30)
        change_eye1.setDepth(19)
        canvas.add(change_eye1) # 추가
        
        # 속상한 눈썹2
        change_eye2 = Rectangle(15, 5, Point(365, 429))
        change_eye2.setFillColor("black")
        change_eye2.setBorderColor("black")
        change_eye2.rotate(30)
        change_eye2.setDepth(19)
        canvas.add(change_eye2) # 추가
        
        time.sleep(0.3)
        text3 = Text("What should I do?", 20, Point(300, 380))
        canvas.add(text3) # 추가
        
        for i in range(100) :
            time.sleep(0.01)
            self.bird.moving2(5)
        time.sleep(1)
        
        for i in range(6) :
            time.sleep(0.3)
            self.car.moving(70)
        time.sleep(1)
        
        # 배경 전환을 위한 사라짐
        canvas.remove(text3)
        canvas.remove(change_eye1)
        canvas.remove(change_eye2)
        canvas.remove(self.mans.guy2)
        canvas.remove(self.suns.sun)
        canvas.remove(self.grounds.ground)
        canvas.remove(self.stations.station)
        canvas.remove(self.tree)
        canvas.remove(self.trees)
        canvas.remove(self.building)
        self.car.car.moveTo(-1000, 0)

def animate_people_bus(scene2) :
    animation2 = Animation2(scene2)
    animation2.animating()



# 장면 3: 교수님을 만나다!
class Scene3 :
    def __init__(self) :
        self.man3 = Man3()
        self.car2 = Car2()
        self.window3 = Window3()
        self.professor = Professor()
        self.sun3 = Sun3()
        
    def get_data(self) :
        return self.man3, self.car2, self.window3, self.professor, self.sun3

# 해
class Sun3 :
    def __init__(self) :
        self.sun3 = Circle(150 ,Point(-10, -10))
        self.sun3.setFillColor('red')
        self.sun3.setBorderColor('orange')
        self.sun3.setDepth(10)
        canvas.add(self.sun3) # 추가

# 주인공
class Man3 :
    def __init__(self) :
        self.guy = Layer() # 겹

        # 주인공 머리
        self.hand3 = Circle(23)
        self.hand3.setBorderColor("bisque")
        self.hand3.setFillColor("bisque")
        self.hand3.setDepth(34)
        self.hand3.move(170, 9)
        self.guy.add(self.hand3) # 겹 추가

        # 주인공 얼굴
        self.face3 = Circle(110, Point(0, -300))
        self.face3.setBorderColor("bisque")
        self.face3.setFillColor("bisque")
        self.face3.setDepth(50)
        self.guy.add(self.face3) # 겹 추가
        
        # 주인공 왼쪽 눈
        self.eyes1 = Circle(15, Point(50, -330))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(1)
        self.guy.add(self.eyes1) # 겹 추가
        # 주인공 오른족 눈
        self.eyes2 = Circle(15, Point(-50, -330))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(1)
        self.guy.add(self.eyes2) # 겹 추가
        
        # 주인공 입
        self.mouth3 = Circle(21, Point(0, -250))
        self.mouth3.setFillColor("black")
        self.mouth3.setDepth(10)
        self.guy.add(self.mouth3) # 겹 추가

        # 주인공 몸체
        self.body3 = Ellipse(250, 700, Point(0, 0))
        self.body3.setFillColor('salmon')
        self.body3.setBorderColor('salmon')
        self.body3.setDepth(70)
        self.guy.add(self.body3) # 겹 추가
        
        # 주인공 팔
        self.arm3 = Ellipse(70, 270, Point(139, -100))
        self.arm3.setFillColor("orange")
        self.arm3.setBorderColor("orange")
        self.arm3.rotate(-18)
        self.arm3.setDepth(34)
        self.guy.add(self.arm3) # 겹 추가
        
        self.guy.moveTo(100, 600)
        self.guy.setDepth(10)
        canvas.add(self.guy) # 추가

    # 움직이는 주인공
    def moving_head(self, x) :
        self.face3.move(0, x)
        self.mouth3.move(0, x)
        self.eyes1.move(0, x)
        self.eyes2.move(0, x)

# 교수님 차
class Car2 :
    def __init__(self) :
        self.car = Polygon(Point(100, 600), Point(300, 600), Point(400, 400), Point(700, 400), Point(900, 600), Point(1100, 600), Point(1100, 900), Point(100, 900))
        self.car.setDepth(50)
        self.car.setFillColor('black')
        canvas.add(self.car) # 추가

class Window3 :
    def __init__(self) :
        self.window = Polygon(Point(300, 630), Point(410, 420), Point(690, 420), Point(910, 630))
        self.window.setDepth(40)
        self.window.setBorderColor('light blue')
        self.window.setFillColor('darkgoldenrod')
        canvas.add(self.window) # 추가


class Professor :
    def __init__(self) :
        self.pros = Layer() # 겹
        
        # 교수님 몸체
        self.body = Ellipse(250, 550, Point(200, 0))
        self.body.setFillColor('black')
        self.body.setBorderColor('black')
        self.body.setDepth(45)
        self.pros.add(self.body) # 겹 추가

        # 교수님 얼굴
        self.face = Circle(70, Point(200, -300))
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.face.setDepth(23)
        self.pros.add(self.face) # 겹 추가
        
        # 교수님 왼쪽 눈
        self.eye1 = Path(Point(160,-300),Point(170,-310),Point(180,-300))
        self.eye1.setBorderWidth(3)
        self.eye1.setDepth(20)
        self.pros.add(self.eye1) # 겹 추가
        # 교수님 오른쪽 눈
        self.eye2 = Path(Point(220,-300),Point(230,-310),Point(240,-300))
        self.eye2.setBorderWidth(3)
        self.eye2.setDepth(20)
        self.pros.add(self.eye2) # 겹 추가

        # 안경(glasses)1
        self.glasses1 = Rectangle(35, 25, Point(170, -304))
        self.glasses1.setDepth(22)
        self.glasses1.setBorderWidth(3)
        self.glasses1.setBorderColor('black')
        self.pros.add(self.glasses1) # 겹 추가
        # 안경(glasses)2
        self.glasses2 = Rectangle(35, 25, Point(230, -304))
        self.glasses2.setDepth(22)
        self.glasses2.setBorderWidth(3)
        self.glasses2.setBorderColor('black')
        self.pros.add(self.glasses2) # 겹 추가
        # 안경테(glasses frame)1
        self.gf1 = Path(Point(130,-311),Point(151,-301))
        self.gf1.setBorderWidth(3)
        self.gf1.setDepth(22)
        self.pros.add(self.gf1) # 겹 추가
        # 안경테(glasses frame)2
        self.gf2 = Path(Point(190,-300),Point(212,-300))
        self.gf2.setBorderWidth(3)
        self.gf2.setDepth(22)
        self.pros.add(self.gf2) # 겹 추가
        # 안경테(glasses frame)3
        self.gf3 = Path(Point(249,-301),Point(270,-311))
        self.gf3.setBorderWidth(3)
        self.gf3.setDepth(22)
        self.pros.add(self.gf3) # 겹 추가

        # 교수님 입
        self.mouth = Rectangle(30, 15, Point(200, -260))
        self.mouth.setFillColor("black")
        self.mouth.setBorderColor("black")
        self.mouth.setDepth(22)
        self.pros.add(self.mouth) # 겹 추가
        
        self.pros.moveTo(400, 800)
        self.pros.setDepth(20)
        canvas.add(self.pros) # 추가


# 장면 3, 애니메이션
class Animation3 :
    def __init__(self, scene3) :
        man, car, window, professor, sun = scene3.get_data()
        self.man = man
        self.car = car
        self.window = window
        self.professor = professor
        self.sun = sun
    
    def animating(self) :
        time.sleep(2)
        text = Text("What are you doing?", 30, Point(600, 300))
        canvas.add(text) # 추가
        time.sleep(2)
        canvas.remove(text) # 사라짐
        text1 = Text("Oh! Hi Professor!!", 30, Point(300, 150))
        canvas.add(text1) # 추가
        time.sleep(2)
        canvas.remove(text1) # 사라짐
        text2 = Text("Hmm....", 30, Point(600, 300))
        canvas.add(text2) # 추가
        time.sleep(2)
        canvas.remove(text2) # 사라짐
        text3 = Text("I guess you lost your bus, right?", 30, Point(600, 300))
        canvas.add(text3) # 추가
        time.sleep(2)
        canvas.remove(text3) # 사라짐
        time.sleep(1)
        tear = Ellipse(15, 20, Point(153, 269))
        tear.setDepth(10)
        tear.setFillColor("blue")
        tear.setBorderColor("blue")
        canvas.add(tear) # 추가

        for i in range(5) :
            time.sleep(0.1)
            self.man.moving_head(5)
            tear.move(0, 30)
        
        canvas.remove(tear) # 사라짐
        text4 = Text("Yes..", 30, Point(300, 150))
        time.sleep(2)
        canvas.add(text4) # 추가
        time.sleep(2)
        canvas.remove(text4) # 사라짐
        text5 = Text("Hey, then... Get on my Car!", 30, Point(600, 300))
        canvas.add(text5) # 추가
        time.sleep(1)
        canvas.remove(text5) # 사라짐
        for i in range(5) :
            time.sleep(0.08)
            self.man.moving_head(-5)
        text6 = Text("Oh? Really?", 30, Point(300, 150))
        time.sleep(2)
        canvas.add(text6) # 추가
        time.sleep(1)
        canvas.remove(text6) # 사라짐

        # 배경 전환을 위한 사라짐
        canvas.remove(self.man.guy)
        canvas.remove(self.car.car)
        canvas.remove(self.window.window)
        canvas.remove(self.professor.pros)
        canvas.remove(self.sun.sun3)

def animate_Scene3(scene3) :
    animation3 = Animation3(scene3)
    animation3.animating()      



# 장면 4: 교수님의 응원, 감사합니다!
class Scene4 :
    def __init__(self) :
        self.man5 = Man5()
        self.professor2 = Professor2()
        self.chair1 = Chair1()
        self.chair2 = Chair2()
        self.sidewindow1 = Sidewindow1()
        self.sidewindow2 = Sidewindow2()
        self.sidetree1 = Sidetree1()
        self.ground2 = Ground2()
        self.handle = Handle()
        
    def get_datas(self) :
        return self.man5, self.professor2, self.chair1, self.chair2, self.sidewindow1, self.sidewindow2, self.sidetree1, self.handle

# 땅
class Ground2 :
    def __init__(self) :
        self.ground2 = Polygon(Point(0,500), Point(300, 280), Point(300, 380), Point(0, 600))
        self.ground2.setFillColor("light green")
        self.ground2.setBorderColor("black")
        self.ground2.setDepth(30)
        canvas.add(self.ground2) # 추가
     
# 자동차 창문1
class Sidewindow1 :
    def __init__(self) :
        self.sidewindow1 = Polygon(Point(0, 300), Point(300, 80), Point(300, 380), Point(0, 600))
        self.sidewindow1.setFillColor("light blue")
        self.sidewindow1.setDepth(30)
        canvas.add(self.sidewindow1) # 추가
# 자동차 창문2
class Sidewindow2 :
    def __init__(self) :
        self.sidewindow2 = Polygon(Point(700, 80), Point(1000, 300), Point(1000, 600), Point(700, 380))
        self.sidewindow2.setFillColor("light blue")
        self.sidewindow2.setDepth(30)
        canvas.add(self.sidewindow2) # 추가

# 자동차 의자1
class Chair1 :
    def __init__(self) :
        self.chair1 = Rectangle(300, 500, Point(300, 700))
        self.chair1.setFillColor('gray')
        self.chair1.setBorderColor('black')
        self.chair1.setDepth(25)
        canvas.add(self.chair1) # 추가
# 자동차 의자2
class Chair2 :
    def __init__(self) :
        self.chair2 = Rectangle(300, 500, Point(700, 700))
        self.chair2.setFillColor('gray')
        self.chair2.setBorderColor('black')
        self.chair2.setDepth(25)
        canvas.add(self.chair2) # 추가

# 자동차 운전 손잡이
class Handle:
    def __init__(self):
        self.handle = Ellipse(110, 140, Point(700, 680))
        self.handle.setBorderWidth(30)
        self.handle.setBorderColor("brown")
        self.handle.setDepth(7)
        canvas.add(self.handle) # 추가

# 주인공
class Man5 :
    def __init__(self) :
        self.final_guy = Layer() # 겹

        # 주인공 겹 구성
        self.final_body = Final_body()
        self.final_face = Final_face()
        self.final_eyes = Final_eyes()
        self.final_mouth = Final_mouth()
        self.final_arm1 = Final_arm1() 
        self.final_arm2 = Final_arm2()
        # 겹 추가
        self.final_guy.add(self.final_body.body)
        self.final_guy.add(self.final_face.face)
        self.final_guy.add(self.final_eyes.eyes1)
        self.final_guy.add(self.final_eyes.eyes2)
        self.final_guy.add(self.final_mouth.mouth)
        self.final_guy.add(self.final_arm1.arm)
        self.final_guy.add(self.final_arm2.arm)

        self.final_guy.moveTo(400, 700)
        self.final_guy.setDepth(10)
        canvas.add(self.final_guy) # 추가

# 주인공 몸체
class Final_body :
    def __init__(self) :
        self.body = Ellipse(150, 350, Point(-100, -100))
        self.body.setFillColor('salmon')
        self.body.setDepth(20)
        self.body.setBorderColor('salmon')

# 주인공 얼굴
class Final_face :
    def __init__(self) :
        self.face = Circle(60, Point(-95, -270))
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.face.setDepth(19)

# 주인공 눈
class Final_eyes :
    def __init__(self) :
        # 주인공 왼쪽 눈
        self.eyes1 = Circle(10, Point(-125, -289))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        # 주인공 오른쪽 눈
        self.eyes2 = Circle(10, Point(-65, -289))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(10)

# 주인공 입
class Final_mouth :
    def __init__(self) :
        self.mouth = Rectangle(30, 15, Point(-95, -240))
        self.mouth.setFillColor("black")
        self.mouth.setDepth(10)

# 주인공 왼팔
class Final_arm1 :
    def __init__(self) :
        self.arm = Ellipse(50, 200, Point(230, 560))
        self.arm.setFillColor('orange')
        self.arm.setBorderColor('orange')
        self.arm.setDepth(18)
        self.arm.rotate(20)
# 주인공 오른팔
class Final_arm2 :
    def __init__(self) :
        self.arm = Ellipse(50, 200, Point(370, 560))
        self.arm.setFillColor('orange')
        self.arm.setBorderColor('orange')
        self.arm.setDepth(18)
        self.arm.rotate(-20)
        
# 교수님
class Professor2 :
    def __init__(self) :
        self.male = Layer() # 겹

        # 교수님 겹 구성
        self.final_bodys = Final_bodys()
        self.final_faces = Final_faces()
        self.final_mouths = Final_mouths()
        self.final_eyess = Final_eyess()
        self.final_glasses = Final_glasses()
        self.final_gf = Final_gf()
        self.final_arm1s = Final_arm1s()
        self.final_arm2s = Final_arm2s()
        # 겹 추가 
        self.male.add(self.final_bodys.body)
        self.male.add(self.final_faces.face)
        self.male.add(self.final_arm1s.arm1)
        self.male.add(self.final_arm2s.arm2)        
        self.male.add(self.final_mouths.mouth)
        self.male.add(self.final_eyess.eye1)
        self.male.add(self.final_eyess.eye2)
        self.male.add(self.final_glasses.glasses1)
        self.male.add(self.final_glasses.glasses2)
        self.male.add(self.final_gf.gf1)
        self.male.add(self.final_gf.gf2)
        self.male.add(self.final_gf.gf3)
       
        self.male.setDepth(10)
        self.male.moveTo(800, 700)
        canvas.add(self.male) # 추가

# 교수님 몸체
class Final_bodys :
    def __init__(self) :
        self.body = Ellipse(150, 350, Point(-100, -100))
        self.body.setFillColor('black')
        self.body.setBorderColor('black')
        self.body.setDepth(20)

# 교수님 얼굴
class Final_faces :
    def __init__(self) :
        self.face = Circle(60, Point(-95, -270))
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.face.setDepth(19)

# 교수님 눈
class Final_eyess :
    def __init__(self) :
        # 교수님 왼쪽 눈
        self.eye1 = Path(Point(-109,-280),Point(-119,-290),Point(-129,-280))
        self.eye1.setBorderWidth(3)
        self.eye1.setDepth(10)
        # 교수님 오른쪽 눈
        self.eye2 = Path(Point(-60,-280),Point(-70,-290),Point(-80,-280))
        self.eye2.setBorderWidth(3)
        self.eye2.setDepth(10)

# 교수님 입
class Final_mouths :
    def __init__(self) :
        self.mouth = Rectangle(30, 15, Point(-95, -240))
        self.mouth.setFillColor("black")
        self.mouth.setDepth(18)

# 교수님 안경
class Final_glasses :
    def __init__(self) :
        # 교수님 안경1
        self.glasses1 = Rectangle(35, 25, Point(-120, -285))
        self.glasses1.setDepth(10)
        self.glasses1.setBorderWidth(3)
        self.glasses1.setBorderColor('black')
        # 교수님 안경2
        self.glasses2 = Rectangle(35, 25, Point(-70, -285))
        self.glasses2.setDepth(10)
        self.glasses2.setBorderWidth(3)
        self.glasses2.setBorderColor('black')

# 교수님 안경테
class Final_gf :
    def __init__(self) :
        # 교수님 안경테1
        self.gf1 = Path(Point(-36,-291),Point(-51,-281))
        self.gf1.setBorderWidth(3)
        self.gf1.setDepth(10)
        # 교수님 안경테2
        self.gf2 = Path(Point(-100,-281),Point(-88,-281))
        self.gf2.setBorderWidth(3)
        self.gf2.setDepth(10)
        # 교수님 안경테3
        self.gf3 = Path(Point(-138,-281),Point(-152,-291))
        self.gf3.setBorderWidth(3)
        self.gf3.setDepth(10)

# 교수님 왼팔
class Final_arm1s :
    def __init__(self) :
        self.arm1 = Ellipse(50, 180, Point(650, 575))
        self.arm1.setFillColor('beige')
        self.arm1.setBorderColor('beige')
        self.arm1.setDepth(9)
        self.arm1.adjustReference(0, -100)
        self.arm1.rotate(10)
        canvas.add(self.arm1) # 추가

    # 움직이는 교수님 왼팔
    def moving(self, x) :
        self.arm1.adjustReference(0+x, 0-x)
        self.arm1.rotate(x)
        
# 교수님 오른팔
class Final_arm2s :
    def __init__(self) :
        self.arm2 = Ellipse(50, 200, Point(700, 600))
        self.arm2.setFillColor('beige')
        self.arm2.setBorderColor('beige')
        self.arm2.setDepth(18)
        self.arm2.adjustReference(0, -100)
        self.arm2.rotate(-90)
        canvas.add(self.arm2) # 추가

# 나무
class Sidetree1 :
    def __init__(self) :
        self.trees = Layer() # 겹
        
        # 나무 겹 구성
        self.tree1 = Tree1s()
        self.tree2 = Tree2s()
        self.leaf = Leafs()
        # 겹 추가
        self.trees.add(self.tree1.tree)
        self.trees.add(self.tree2.tree)
        self.trees.add(self.leaf.leaf)
        
        self.trees.moveTo(600, 435)
        self.trees.setDepth(26)
        canvas.add(self.trees) # 추가

    # 움직이는 나무
    def moving(self, x) :
        self.trees.move(-x, x)

# 나무 기둥
class Tree1s :
    def __init__(self) :
        self.tree = Rectangle(50, 100, Point(-400, -130))
        self.tree.setFillColor('brown')
        self.tree.setBorderColor('black')
        self.tree.setDepth(26)

# 나무 뿌리
class Tree2s :
    def __init__(self) :
        self.tree = Polygon(Point(-470, -80), Point(-330, -80), Point(-400, -130))
        self.tree.setFillColor('brown')
        self.tree.setBorderColor('brown')
        self.tree.setDepth(26)

# 나뭇잎
class Leafs :
    def __init__(self) :
        self.leaf = Circle(40, Point(-400, -200))
        self.leaf.setFillColor('dark green')
        self.leaf.setDepth(23)


# 장면 4, 애니메이션
class Animation4 :
    def __init__(self, scene4) :
        man, professor, chair1, chair2, sidewindow1, sidewindow2, sidetree1, handle = scene4.get_datas()
        self.man = man
        self.professor = professor
        self.chair1 = chair1
        self.chair2 = chair2
        self.sidewindow1 = sidewindow1
        self.sidewindow2 = sidewindow2
        self.sidetree1 = sidetree1
        self.handle = handle
    
    def animating(self) :
                
        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(-i)
        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(i)
        for i in range(70) :
            time.sleep(0.08)
            self.sidetree1.moving(4)
            
        text = Text("Are you tired?", 30, Point(610, 300))        
        text.setDepth(5)
        canvas.add(text) # 추가
        time.sleep(2)
        canvas.remove(text) # 사라짐
        
        text1 = Text("I'm a little tired \n because it's the end of the semester...", 30, Point(330, 300))
        text1.setDepth(5)
        canvas.add(text1) # 추가
        time.sleep(2)
        canvas.remove(text1) # 사라짐
        
        text2 = Text("You're getting through really well.", 30, Point(610, 300))
        text2.setDepth(5)
        canvas.add(text2) # 추가
        time.sleep(2)
        canvas.remove(text2) # 사라짐

        text3 = Text("Professor... am I really doing well?", 30, Point(330, 300))
        text3.setDepth(5)
        canvas.add(text3) # 추가
        time.sleep(2)
        canvas.remove(text3) # 사라짐

        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(-i)
        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(i)

        text4 = Text("I'd really like to compliment you \n on the hard work and time you've invested.", 30, Point(610, 300))
        text4.setDepth(5)
        canvas.add(text4) # 추가
        time.sleep(3)
        canvas.remove(text4) # 사라짐
        
        text3 = Text("I really wanted to hear this cheering!!! \n Thank you.", 30, Point(330, 300))
        text3.setDepth(5)
        canvas.add(text3) # 추가
        time.sleep(3)
        canvas.remove(text3) # 사라짐

        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(-i)
        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(i)

def animate_Scene4(scene4) :
    animation4 = Animation4(scene4)
    animation4.animating()



# 전체 실행 코드
def main():
    # Scene 1
    canvas.setBackgroundColor("light green")
    scene1 = Scene1()
    animate_man(scene1)
    # Scene 2
    canvas.setBackgroundColor("light blue")
    scene2 = Scene2()
    animate_people_bus(scene2)
    # Scene 3
    canvas.setBackgroundColor("light blue")
    scene3 = Scene3()
    animate_Scene3(scene3)
    # Scene 4
    canvas.setBackgroundColor("darkgoldenrod")
    scene4 = Scene4()
    animate_Scene4(scene4)
    canvas.wait()
    canvas.close()


## 실행
main()
