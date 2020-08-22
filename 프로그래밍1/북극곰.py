from cs1graphics import *
import time

canvas = Canvas(900,700, 'skyblue', "Polar bears' tear")

# 첫 장면 - 제목: Polar bear tears
class Title:
    def __init__(self):
        self.title = Layer()
        self.bg = Rectangle(900,700,Point(450,350))
        self.bg.setFillColor('white')
        self.bg.setBorderColor('white')
        self.title.add(self.bg)
        self.text = Text('Polar bear tears', 80, Point(450,350))
        self.title.add(self.text)
        canvas.add(self.title)
        time.sleep(2)
        canvas.remove(self.title)

# 빙판 바닥
class Ground:
    def __init__(self):
        self.shape = Circle(1200, Point(900,1310))
        self.shape.setFillColor("white")
        self.shape.setBorderColor('white')
        self.shape.setDepth(100)

# 태양
class Sun:
    def __init__(self):
        self.layer = Layer()
        self.sun = Circle(80)
        self.sun.setFillColor('red')
        self.sun.setBorderColor('red')
        self.layer.add(self.sun)
        for i in range(4):
            name = "sun" + str(i+1)
            self.name = Rectangle(60,10)
            self.name.setBorderColor('orange')
            self.name.setFillColor('orange')
            self.name.move(135 - 40 * i, 20 + 42 * i)
            self.name.rotate(30 * i)
            self.layer.add(self.name)
        
# 북극곰
class Bear:
    def __init__(self,sad = False):
        self.body = BBody()
        self.face = BFace(sad)
        self.arm1 = BArm1()
        self.arm2 = BArm2()
        self.leg1 = BLeg1()
        self.leg2 = BLeg2()
        self.layer = Layer()
        self.layer.add(self.body.layer)
        self.layer.add(self.face.layer)
        self.layer.add(self.arm1.shape)
        self.layer.add(self.arm2.shape)
        self.layer.add(self.leg1.shape)
        self.layer.add(self.leg2.shape)
    def move(self,x,y): # 북극곰 움직이기
        self.layer.move(x,y)
    def jumpup(self):
        self.leg1.up()
        self.leg2.up()
        self.arm1.up()
        self.arm2.up()
        self.layer.move(0,-20)
    def jumpdown(self):
        self.leg1.down()
        self.leg2.down()
        self.arm1.down()
        self.arm2.down()
        self.layer.move(0,20)

# 북극곰 몸
class BBody:
    def __init__(self):
        self.layer = Layer()
        self.body = Ellipse(110,120,Point(450,455))
        self.body.setFillColor('white')
        self.body.setDepth(53)
        self.inbody = Ellipse(80,85,Point(450,455))
        self.inbody.setBorderColor((202,202,202))
        self.inbody.setFillColor((202,202,202))
        self.inbody.setDepth(52)
        self.layer.add(self.body)
        self.layer.add(self.inbody)

# 북극곰 왼쪽팔
class BArm1:
    def __init__(self):
        self.shape = Ellipse(65,30,Point(430,435))
        self.shape.adjustReference(-25,0)
        self.shape.rotate(50)
        self.shape.setFillColor('white')
    def up(self): # 손 올리기
        self.shape.rotate(-150)
    def down(self): # 손 내리기
        self.shape.rotate(150)

# 북극곰 오른쪽팔        
class BArm2:
    def __init__(self):
        self.shape = Ellipse(65,30, Point(470,435))
        self.shape.adjustReference(25,0)
        self.shape.rotate(-50)
        self.shape.setFillColor('white')
    def up(self): # 손 올리기
        self.shape.rotate(150)
    def down(self): # 손 내리기
        self.shape.rotate(-150)

# 북극곰 왼쪽발
class BLeg1:
    def __init__(self):
        self.shape = Ellipse(45,20, Point(420,520))
        self.shape.setFillColor('white')
    def up(self):# 위로 점프
        self.shape.rotate(-45)
    def down(self): # 아래로 착지
        self.shape.rotate(45)

# 북극곰 오른쪽발
class BLeg2:
    def __init__(self):
        self.shape = Ellipse(45,20, Point(480,520))
        self.shape.setFillColor('white')
    def up(self): # 위로 점프
        self.shape.rotate(45)
    def down(self): # 아래로 착지
        self.shape.rotate(-45)

# 북극곰 얼굴
class BFace:
    def __init__(self, sad = False):
        self.layer = Layer()
        self.ear = BEar()
        self.eye = BEye()
        self.nose = BNose()
        self.mouth = BMouth(sad)
        self.face = Ellipse(130,115, Point(450,350))
        self.face.setFillColor('white')
        self.face.setDepth(51)
        self.layer.add(self.ear.layer)
        self.layer.add(self.face)
        self.layer.add(self.eye.layer)
        self.layer.add(self.nose.shape)
        self.layer.add(self.mouth.layer)

# 북극곰 귀
class BEar:
    def __init__(self):
        self.layer = Layer()
        for i in range(2):
            name = 'shape' + str(i+1)
            self.name = Layer()
            for j in range(2):
                name1 = 'shape' + str(i+1) + str(j+1)
                if j == 0:
                    self.name1 = Circle(25)
                    self.name1.setFillColor('white')
                elif j == 1:
                    self.name1 = Circle(18)
                    self.name1.setBorderColor((202,202,202))
                    self.name1.setFillColor((202,202,202))
                self.name1.move(405 + 90*i,305)
                self.name1.setDepth(55 - j)
                self.name.add(self.name1)
            self.layer.add(self.name)

# 북극곰 눈
class BEye:
    def __init__(self):
        self.layer = Layer()
        for i in range(2):
            name = 'shape' + str(i+1)
            self.name = Ellipse(7.5,10)
            if i == 0:
                self.name.move(430,345)
            else:
                self.name.move(470,345)
            self.name.setFillColor('black')
            self.layer.add(self.name)

# 북극곰 코
class BNose:
    def __init__(self):
        self.shape = Ellipse(20,10, Point(450,360))
        self.shape.setFillColor('black')
        self.shape.setDepth(49)

# 북극곰 입
class BMouth:
    def __init__(self, sad = False):
        self.layer = Layer()
        if sad:
            self.mouth = Path(Point(430,380),Point(450,370),Point(470,380))
        else:
            self.mouth = Path(Point(430,380),Point(450,390),Point(470,380))
        self.mouth.setDepth(49)
        self.space = Ellipse(50,40)
        self.space.move(450,380)
        self.space.setBorderColor((202,202,202))
        self.space.setFillColor((202,202,202))
        self.layer.add(self.mouth)
        self.layer.add(self.space)

# 눈사람
class Snowman:
    def __init__(self):
        self.face = SFace()
        self.body1 = SBody1()
        self.body2 = SBody2()
        self.arm = SArm()
        self.nose = SNose()
        self.hair = SHair()
        self.mouth = SMouth()
        self.eye = SEye()
        self.button = SButton()
        self.foot = SFoot()
        self.layer = Layer()
        self.layer.add(self.nose.shape)
        self.layer.add(self.hair.layer)
        self.layer.add(self.mouth.layer)
        self.layer.add(self.eye.layer)
        self.layer.add(self.body1.shape)
        self.layer.add(self.body2.shape)
        self.layer.add(self.face.shape)
        self.layer.add(self.arm.layer)
        self.layer.add(self.button.layer)
        self.layer.add(self.foot.layer)
    def move(self,x,y):
        self.layer.moveTo(x,y)
    # 눈사람의 부분들이 떨어지면서 만들어지는 애니메이션1
    def make1(self):
        self.foot.fall()
        self.body2.fall()
        self.body1.fall()
    # 눈사람의 부분들이 떨어지면서 만들어지는 애니메이션2
    def make2(self):
        self.face.fall()
        self.eye.fall()
        self.nose.fall()
        self.mouth.fall()
    # 눈사람의 부분들이 떨어지면서 만들어지는 애니메이션3
    def make3(self):
        self.arm.fall()
        self.button.fall()
        self.hair.fall()

# 눈사람 얼굴
class SFace:
    def __init__(self):
        self.shape = Polygon(Point(45, 115), Point(90, 115), Point(105, 145), Point(120, 155), Point(85, 235), Point(55, 235), Point(15, 155), Point(30, 145))
        self.shape.move(380,-220)
        self.shape.setFillColor('white')
        self.shape.setDepth(89)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.shape.move(0,50)
            time.sleep(0.1)

# 눈사람 코
class SNose:
    def __init__(self):
        self.shape = Polygon(Point(390, -50), Point(450, -60), Point(450, -40))
        self.shape.setFillColor('orange')
        self.shape.setDepth(88)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.shape.move(0,50)
            time.sleep(0.1)

# 눈사람 머리
class SHair:
    def __init__(self):
        self.layer = Layer()
        for i in range(3):
            name = 'shape' + str(i + 1)
            self.name = Polygon(Point(460 - i * 10, -135), Point(450, -105))
            self.name.setBorderColor((81, 0, 0))
            self.name.setBorderWidth(4)
            self.name.setDepth(91)
            self.layer.add(self.name)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,50)
            time.sleep(0.1)

# 눈사람 입
class SMouth:
    def __init__(self):
        self.layer = Layer()
        self.mouth = Polygon(Point(425, -30), Point(440, 0), Point(460, 0), Point(475, -30))
        self.mouth.setFillColor('blue')
        self.mouth.setDepth(88)
        self.tooth = Rectangle(30, 11)
        self.tooth.move(450, -25)
        self.tooth.setFillColor('white')
        self.tooth.setDepth(88)
        self.layer.add(self.mouth)
        self.layer.add(self.tooth)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,50)
            time.sleep(0.1)

# 눈사람 귀
class SEye:
    def __init__(self):
        self.layer = Layer()
        for i in range(2):
            name = 'eye' + str(i+1)
            self.name = Circle(10)
            self.name.move(465 - i*35,-70)
            self.name.setFillColor('white')
            self.layer.add(self.name)
        for i in range(2):
            name = 'eyebrow' + str(i+1)
            self.name = Rectangle(20,5)
            self.name.move(465 - i*35,-89)
            self.name.setFillColor((99,2,0))
            self.layer.add(self.name)
        for i in range(2):
            name = 'pupil' + str(i+1)
            self.name = Circle(5)
            self.name.move(465 - i*35,-70)
            self.name.setFillColor('black')
            self.layer.add(self.name)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,50)
            time.sleep(0.1)

# 눈사람 몸체
class SBody1:
    def __init__(self):
        self.shape = Ellipse(70, 50, Point(450,-165))
        self.shape.setFillColor('white')
        self.shape.setDepth(90)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.shape.move(0,70)
            time.sleep(0.1)
            
# 눈사람 몸체2
class SBody2:
    def __init__(self):
        self.shape = Ellipse(100,80, Point(450,-110))
        self.shape.setFillColor('white')
        self.shape.setDepth(91)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.shape.move(0,70)
            time.sleep(0.1)

# 눈사람 단추
class SButton:
    def __init__(self):
        self.layer = Layer()
        for i in range(3):
            name = 'button' + str(i+1)
            self.name = Polygon(Point(70, 55), Point(83, 65), Point(77, 77), Point(63, 77), Point(57, 65))
            self.name.move(380,-230+i*30)
            self.name.setFillColor('black')
            self.name.setDepth(90)
            self.layer.add(self.name)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,70)
            time.sleep(0.1)

# 눈사람 발
class SFoot:
    def __init__(self):
        self.layer = Layer()
        for i in range(2):
            name = 'foot' + str(i+1)
            self.name =  Ellipse(40, 30)
            self.name.move(410+i*80,-75)
            self.name.setFillColor('white')
            self.name.setDepth(92)
            self.layer.add(self.name)            
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,70)
            time.sleep(0.1)

# 눈사람 팔
class SArm:
    def __init__(self):
        self.layer = Layer()
        for i in range(2):
            name = 'arm' + str(i+1)
            self.name = Polygon(Point(40, 70+i*100), Point(90, 130-i*20))
            self.name.move(330+i*110,-300-i*40)
            self.name.setBorderColor((81,0,0))
            self.name.setBorderWidth(7)
            self.name.setDepth(89)
            self.layer.add(self.name)
        for i in range(4):
            name = 'hand' + str(i+1)
            if i == 0:
                self.name = Polygon(Point(360, -210), Point(381, -212))
            elif i == 1:
                self.name = Polygon(Point(381, -212), Point(390, -235))
            elif i == 2:
                self.name = Polygon(Point(505, -230), Point(515, -212))
            else:
                self.name = Polygon(Point(515, -212), Point(535, -210))
            self.name.setBorderColor((81,0,0))
            self.name.setBorderWidth(7)
            self.name.setDepth(88)
            self.layer.add(self.name)
    # 위에서 떨어지는 애니메이션
    def fall(self):
        for i in range(10):
            self.layer.move(0,70)
            time.sleep(0.1)

# 온도계
class Thermometer:
    def __init__(self):
        self.layer = Layer()
        self.bulb = Circle(30,Point(450,550))
        self.bulb.setFillColor('white')
        self.bulb.setDepth(30)
        self.layer.add(self.bulb)
        self.column = Rectangle(27,200,Point(450,450))
        self.column.setFillColor('white')
        self.column.setDepth(35)
        self.layer.add(self.column)
        self.alchol = Circle(13,Point(450,550))
        self.alchol.setFillColor('red')
        self.alchol.setBorderColor('red')
        self.alchol.setDepth(20)
        self.layer.add(self.alchol)
        self.eraser = Square(25, Point(450,530))
        self.eraser.setFillColor('white')
        self.eraser.setBorderColor('white')
        self.eraser.setDepth(25)
        self.layer.add(self.eraser)
    # 온도계 상승 - flag는 온도계가 몇번째 상승하는 것인지를 나타내는 표지
    # False = 첫번째 / True = 두번째
    def rise(self, flag = False):
        self.layer = Layer()
        canvas.add(self.layer)
        if flag :
            n = 470
            self.shape = Rectangle(10,70, Point(450, 510))
            self.shape.setFillColor('red')
            self.shape.setBorderColor('red')
            self.shape.setDepth(20)
            self.layer.add(self.shape)
        else:
            n = 540
        for i in range(7):
            self.shape = Square(10)
            self.shape.setFillColor('red')
            self.shape.setBorderColor('red')
            self.shape.setDepth(20)
            self.shape.moveTo(450,n-i*10)
            self.layer.add(self.shape)
            time.sleep(0.3)
        time.sleep(0.5)
        canvas.remove(self.layer)

# 곰들이 대화하는 애니메이션
class Conversation:
    def __init__(self):
        self.background = Rectangle(900,70,Point(450,650))
        self.background.setFillColor((200,200,200))
        self.background.setBorderColor((200,200,200))
        self.background.setDepth(40)
        self.text1 = Text("- Hey, Teddy.",20, Point(450,635))
        self.text1.setDepth(35)
        self.text2 = Text("- Yes", 20, Point(450,665))
        self.text2.setDepth(35)
        self.text3 = Text("- Do you wanna build a snowman~? ♪♬♪♬", 30, Point(450,650))
        self.text3.setDepth(35)
        self.text4 = Text("- Yes!!!", 20, Point(450,650))
        self.text4.setDepth(35)
    # 곰들의 대화
    def talk(self):
        time.sleep(1)
        canvas.add(self.background)
        canvas.add(self.text1)
        time.sleep(0.7)
        canvas.add(self.text2)
        time.sleep(0.7)
        canvas.remove(self.text1)
        canvas.remove(self.text2)
        canvas.add(self.text3)
        time.sleep(1.5)
        canvas.remove(self.text3)
        canvas.add(self.text4)
        time.sleep(1)
        canvas.remove(self.text4)
        canvas.remove(self.background)

# 눈사람 만들기 위해 주문을 외우는 애니메이션
class Spell:
    def __init__(self,scene):
        bear1, bear2, snowman = scene.anim_group()
        self.bear1 = bear1
        self.bear2 = bear2
        self.snowman = snowman
        self.layer = Layer()
        canvas.add(self.layer)
    # 곰들이 주문을 외우며 점프
    def jump(self):
        for i in range(2):
            self.bear1.jumpup()
            self.text1 = Text("เลิกทําการบ้านได้แล้ว", 20, Point(350,320))
            self.layer.add(self.text1)
            time.sleep(0.5)
            self.bear1.jumpdown()
            self.layer.remove(self.text1)
            self.bear2.jumpup()
            self.text2 = Text("เลิกทําการบ้านได้แล้ว", 20, Point(750,290))
            self.layer.add(self.text2)
            time.sleep(0.5)
            self.bear2.jumpdown()
            self.layer.remove(self.text2)
    # 곰들이 주문을 외우는 동안 눈사람이 완성됨
    def spell(self):
        self.jump()
        self.snowman.make1()
        self.jump()
        self.snowman.make2()
        self.jump()
        self.snowman.make3()
        time.sleep(1)
        self.text3 = Text("Wowowowowowowowow", 50, Point(450,130))
        self.layer.add(self.text3)
        self.bear1.jumpup()
        self.bear2.jumpup()
        time.sleep(1)
        self.bear1.jumpdown()
        self.bear2.jumpdown()
        time.sleep(1)
        canvas.remove(self.layer)

class Tide:
    def __init__(self) : 
        self.layer = Layer()
        for i in range(7):
            self.shape = Circle(75, Point(25 + (140 * i), 699))
            self.shape.setFillColor('skyblue')
            self.shape.setBorderColor('skyblue')
            self.shape.setDepth(40)
            self.layer.add(self.shape)
        self.tide = Rectangle(900, 700, Point(450, 1055))
        self.tide.setFillColor('skyblue')
        self.tide.setBorderColor('skyblue')
        self.tide.setDepth(40)
        self.layer.add(self.tide)
    # 침식
    def erode(self) :
        time.sleep(1)
        for i in range(16) :
            self.layer.move(0, -25)
            time.sleep(0.3)

class Banner:
    def __init__(self):
        self.layer = Layer()
        self.banner = Rectangle(300, 100, Point(450, 750))
        self.banner.setFillColor('black')
        self.banner.setDepth(10)
        self.text = Text('Help me !', 40, Point(450, 750))
        self.text.setFontColor('red')
        self.text.setDepth(9)
        self.layer.add(self.banner)
        self.layer.add(self.text)
    def riseup(self):
        for i in range(14):
            self.layer.move(0,-20)
            time.sleep(0.3)

'''
첫번째 장면
곰 두 마리가 빙판 위에 있음
'''
class Scene1:
    def __init__(self):
        self.layer = Layer()
        self.ground = Ground()
        self.sun = Sun()
        self.bear1 = Bear()
        self.bear2 = Bear()
        self.bear1.move(-100,80)
        self.bear2.move(300,50)
        self.snowman = Snowman()
        self.snowman.move(100,-100)
        canvas.add(self.sun.layer)
        self.layer.add(self.ground.shape)
        self.layer.add(self.snowman.layer)
        canvas.add(self.layer)
        canvas.add(self.bear1.layer)
        canvas.add(self.bear2.layer)
    # 애니메이션 있는 observation return
    def anim_group(self):
        return self.bear1, self.bear2, self.snowman
    def clear(self):
        canvas.remove(self.layer)
        canvas.remove(self.bear1.layer)
        canvas.remove(self.bear2.layer)
                          
'''
두번째 장면
설명: 곰들이 북극에서 잘 지내고 있었지만 점점 올라가는 온도로 인해
곰들의 주거지가 사라지고 있음을 암시하는 'By the way...'
온도계로 북극의 온도가 올라가고 있음을 표현
'''
class Scene2:
    def __init__(self):
        self.title = Layer()
        self.bg = Rectangle(900, 700, Point(450, 350))
        self.bg.setFillColor('white')
        self.bg.setBorderColor('white')
        self.title.add(self.bg)
        self.text1 = Text('By the way...', 80, Point(450, 350))
        self.title.add(self.text1)
        canvas.add(self.title)
        time.sleep(3)
        self.title.remove(self.text1)
        self.text2 = Text('Suddenly, \nthe temperature is rising!!!', 50, Point(450, 220))
        self.title.add(self.text2)
        self.therm = Thermometer()
        self.title.add(self.therm.layer)
        time.sleep(1)
        self.therm.rise()
        canvas.remove(self.title)
                          
'''
세번째 장면
'''
class Scene3(Scene1):
    def __init__(self):
        Scene1.__init__(self)
        canvas.remove(self.bear1.layer)
        canvas.remove(self.bear2.layer)

        self.text = Layer()
        self.text1 = Text("Help me~",30, Point(800,50))
        self.text1.setFontColor('black')
        self.text1.setDepth(10)
        self.text2 = Text("SOS!", 30, Point(150,80))
        self.text2.setFontColor('black')
        self.text2.setDepth(10)
        self.text3 = Text("Eung-ae Eung-ae", 30, Point(450,50))
        self.text3.setFontColor('black')
        self.text3.setDepth(10)
        self.text4 = Text("EongEongEong", 30, Point(550,150))
        self.text4.setFontColor('black')
        self.text4.setDepth(10)
        self.text5 = Text("Please", 30, Point(200,170))
        self.text5.setFontColor('black')
        self.text5.setDepth(10)
        canvas.add(self.text)
        
        self.shape = Rectangle(900, 700, Point(450, 1055))
        self.shape.setFillColor('white')
        self.shape.setBorderColor('white')
        self.shape.setDepth(40)
        self.layer.add(self.shape)
        self.bear3 = Bear(True)
        self.bear4 = Bear(True)
        self.bear3.move(-100,80)
        self.bear4.move(300,50)
        self.layer.add(self.bear3.layer)
        self.layer.add(self.bear4.layer)        
    def up(self):
        for i in range(10):
            self.layer.move(0,-25)
            time.sleep(0.3)
    def clear(self):
        canvas.remove(self.layer)
        canvas.remove(self.text)
        canvas.remove(self.banner.layer)
    def erode(self):
        self.tide = Tide()
        canvas.add(self.tide.layer)
        self.tide.erode()
    def sos(self):
        time.sleep(0.5)
        self.text.add(self.text1)
        time.sleep(0.5)
        self.text.add(self.text2)
        time.sleep(0.5)
        self.text.add(self.text3)
        time.sleep(0.5)
        self.text.add(self.text4)
        time.sleep(0.5)
        self.text.add(self.text5)
        time.sleep(0.5)
        
        self.banner = Banner()
        canvas.add(self.banner.layer)
        self.banner.riseup()
        time.sleep(1)
        

'''
네번째 장면
설명: 북극의 온도가 지속적으로 올라가고 있음을 표현
'''
class Scene4:
    def __init__(self):
        self.title = Layer()
        self.bg = Rectangle(900, 700, Point(450, 350))
        self.bg.setFillColor('white')
        self.bg.setBorderColor('white')
        self.title.add(self.bg)
        self.text = Text('The temperature is getting \nhigher and higher!!!', 50, Point(450, 220))
        self.title.add(self.text)
        self.therm = Thermometer()
        self.title.add(self.therm.layer)
        canvas.add(self.title)
        self.therm.rise(True)
        canvas.remove(self.title)

'''
다섯번째 장면
설명: 북극의 온도가 올라가서 결국 북극곰들의 터전이 사라졌음을 암시하는 'Finally...'
'''
class Scene5:
    def __init__(self):
        self.title = Layer()
        self.bg = Rectangle(900, 700, Point(450, 350))
        self.bg.setFillColor('white')
        self.bg.setBorderColor('white')
        self.title.add(self.bg)
        self.text = Text('Finally, the North Pole...', 50, Point(450, 350))
        self.title.add(self.text)
        canvas.add(self.title)
        time.sleep(3)
        canvas.remove(self.title)

'''
여섯번째 장면
설명: 북극곰이 눈물을 흘리는 모습을 통해 환경오염의 문제에 대한 심각성을 깨닫게 하는 장면
'''
class Scene6:
    def __init__(self):
        self.bg = Rectangle(900, 700, Point(450, 350))
        self.bg.setFillColor('skyblue')
        self.bg.setBorderColor('skyblue')
        canvas.add(self.bg)
        self.face = BFace(True)
        canvas.add(self.face.layer)
        self.layer = Layer()
        self.tear = Ellipse(20,35,Point(530,349))
        self.tear.setFillColor('skyblue')
        self.tear.setBorderColor('skyblue')
        self.eye = Ellipse(33,45,Point(530,351))
        self.eye.setFillColor('black')
        self.eye.setDepth(40)
        self.layer.add(self.tear)
        self.layer.add(self.eye)
    # 북극곰 얼굴 확대
    def make_big(self):
        for i in range(30):
            self.face.layer.scale(1.05)
            self.face.layer.move(-50,-38)
    # 북극곰의 눈물
    def cry(self):
        canvas.add(self.layer)
        time.sleep(2)
        for i in range(20):
            self.tear.move(0,20)
            time.sleep(0.3)

# 마지막 장면
class Scene7:
    def __init__(self):
        self.title = Layer()
        self.bg = Rectangle(900, 700,Point(450, 350))
        self.bg.setFillColor('black')
        self.bg.setBorderColor('black')
        self.title.add(self.bg)
        self.text = Text('- The End -', 50, Point(450, 350))
        self.text.setFontColor('white')
        self.title.add(self.text)
        self.name = Text('김시우 박선영 한성진', 20, Point(450,670))
        self.name.setFontColor('white')
        self.title.add(self.name)
        canvas.add(self.title)

'''
애니메이션1
: 곰들이 눈사람을 만들자는 대화 후에 주문을 외우며 눈사람을 만든다.
'''
def animate1():
    scene = Scene1()
    conversation = Conversation()
    conversation.talk()
    spell = Spell(scene)
    spell.spell()
    scene.clear()

def animate2():
    scene = Scene3()
    scene.up()
    scene.erode()
    scene.sos()
    scene.clear()
    
'''
애니메이션2
: 곰이 눈물을 흘린다.
'''
def animate3():
    scene = Scene6()
    scene.make_big()
    scene.cry()
    
def main():
    title = Title()
    animate1()
    scene2 = Scene2()
    animate2()
    scene4 = Scene4()
    scene5 = Scene5()
    animate3()
    scene7 = Scene7()
    canvas.wait()
    canvas.close()

main()
