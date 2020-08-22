from cs1graphics import *
import time
canvas = Canvas(1000, 700)

class Scene1 :
    #canvas.setBackgroundColor("light green")
    def __init__(self) :
        self.man = Man1()
        self.bed = Bed()
        self.window1 = Window1()
        self.table = Table()
        self.sun = Sun()
        self.door = Door()
        self.clock = Clock()

    def get_anim_data(self) :
        return self.man, self.bed.blanket, self.bed.beds, self.window1.window, self.table.drawer, self.sun.suns, self.door.doors, self.door.doors_sign, self.door.doors_hand, self.clock.clock

class Table:
    def __init__(self) :
        self.drawer = Layer()
        self.drawer1 =Rectangle(150,200, Point(75, -100) )
        self.drawer1.setFillColor('rosybrown')
        self.drawer1.setDepth(60)
        self.drawer.add(self.drawer1)
        
        self.door1 =Rectangle(130, 50, Point(75, -37.5) )
        self.door1.setFillColor('brown')
        self.door1.setDepth(30)
        self.drawer.add(self.door1)
        
        self.door2 =Rectangle(130, 50, Point(75, -100) )
        self.door2.setFillColor('brown')
        self.door2.setDepth(30)
        self.drawer.add(self.door2)
        
        self.door3 =Rectangle(130, 50, Point(75, -162.5))
        self.door3.setFillColor('brown')
        self.door3.setDepth(30)
        self.drawer.add(self.door3)
        
        self.upperside=Polygon(Point(0,-200), Point(50, -240), Point(200, -240), Point(150, -200))
        self.upperside.setFillColor('rosybrown')
        self.drawer.add(self.upperside)
        
        self.rightside = Polygon(Point(150,-200), Point(200, -240), Point(200, -40), Point(150, 0))
        self.rightside.setFillColor('rosybrown')
        self.drawer.add(self.rightside)
        
        self.drawer.moveTo(500, 450)
        canvas.add(self.drawer)



class Clock :
    def __init__(self) :
        self.clock = Layer()
        self.clocks = Circle(35, Point(0, 0))
        self.clocks.setFillColor('gray')
        self.clocks.setDepth(60)
        self.line1 = Polygon(Point(0, 0), Point(-20, 15))
        self.line2 = Polygon(Point(0, 0), Point(20, 20))
        self.line3 = Polygon(Point(0, 0), Point(-25, 44))
        self.line4 = Polygon(Point(0, 0), Point(25, 44))
        self.line3.setDepth(80)
        self.line4.setDepth(80)
        self.clock.add(self.clocks)
        self.clock.add(self.line1)
        self.clock.add(self.line2)
        self.clock.add(self.line3)
        self.clock.add(self.line4)
        self.handline = Circle(22, Point(0, -35))
        self.handline.setDepth(80)
        self.clock.add(self.handline)
        self.bell1 = Circle(10, Point(-17.5, -35))
        self.bell1 = Circle(10, Point(-17.5, -35))
        self.bell1.setFillColor('gray')
        self.bell1.setDepth(-10)
        self.bell2 = Circle(10, Point(17.5, -35))
        self.bell2.setFillColor('gray')
        self.bell2.setDepth(-10)
        self.clock.add(self.bell1)
        self.clock.add(self.bell2)
        self.clock.moveTo(600, 200)
        canvas.add(self.clock)

        
class Window1 :
    def __init__(self) :
        self.window = Layer()
        self.bigwindow = Rectangle(300, 300, Point(150, -150))
        self.bigwindow.setFillColor('Brown')
        self.window.add(self.bigwindow)
        self.window1 = Rectangle(132.5, 280, Point(76.25, -150))
        self.window1.setFillColor('sky blue')
        self.window1.setDepth(30)
        self.window.add(self.window1)
        self.window2 = Rectangle(132.5, 280, Point(225, -150))
        self.window2.setFillColor('sky blue')
        self.window2.setDepth(30)
        self.window.add(self.window2)
        self.window.moveTo(100, 300)
        canvas.add(self.window)
        
class Animation :
    def __init__(self, scene1) :
        man, blanket, bed, window, table, sun, door, door_sign, door_hand, clock= scene1.get_anim_data()
        self.mans = man
        self.blankets = blanket
        self.beds = bed
        self.table = table
        self.suns = sun
        self.doors = door
        self.doors_sign = door_sign
        self.doors_hand = door_hand
        self.window = window
        self.clock = clock
        #self.drawer = drawer
        

    def move_man(self) :
        text = Text("08 : 20", 25)
        text.move(600, 100)
        text.setFontColor('red')
        canvas.add(text)
        for i in range(50) :
            if i == 10 :
                text1 = Text("Z", 30)
                text1.move(100, 400)
                canvas.add(text1)
            elif i == 30 :
                time.sleep(1)
                text1.move(20, -20)
            elif i == 45 :
                time.sleep(1)
                text1.move(20, -20)
                time.sleep(2)
                canvas.remove(text1)
                time.sleep(1)
        text4 = Text(" (( ", 30)
        text4.move(500, 200)
        text5 = Text(" )) ", 30)
        text5.move(700, 200)
        canvas.add(text4)
        canvas.add(text5)
        time.sleep(1)
        canvas.remove(text4)
        canvas.remove(text5)
        time.sleep(1)
        canvas.add(text4)
        canvas.add(text5)
        time.sleep(1)
        canvas.remove(text4)
        canvas.remove(text5)
        time.sleep(0.5)

        for i in range(10) :
        
            self.mans.moving(2.25)
            
            self.blankets.move(1, 0)
            #self.arms.movings(-5)
            time.sleep(0.06)
            self.mans.moving(2.25)
            self.blankets.move(1, 0)

        
        time.sleep(2)
        text3 = Text("....", 30)
        text3.move(50, 380)
        canvas.add(text3)
        time.sleep(3)
        canvas.remove(text3)
        text2 = Text("!!", 40)
        
        text2.move(50, 400)
        canvas.add(text2)
        time.sleep(2)

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



        
class Bed :
    def __init__(self) :
        self.beds = Rectangle(400, 150, Point(200, 500))
        self.blanket = Rectangle(200, 145, Point(300, 500))
        self.beds.setFillColor("gray")
        self.beds.setDepth(50)
        self.blanket.setFillColor("tan")
        self.blanket.setBorderColor("tan")
        self.blanket.setDepth(10)
        self.beds.setDepth(60)
        canvas.add(self.beds)
        canvas.add(self.blanket)
        

class Man1 :
    def __init__(self) :
        self.guy = Layer()
        self.face = Face()
        self.body = Body()
        self.arms = Arms()
        self.hands = Hands()
        self.eyes = Eyes()
        self.mouse = Mouse()
        self.guy.add(self.face.faces)
        self.guy.add(self.body.bodys)
        self.guy.add(self.arms.arm1)
        self.guy.add(self.arms.arm2)
        self.guy.add(self.hands.hand1)
        self.guy.add(self.hands.hand2)
        self.guy.add(self.eyes.eyes1)
        self.guy.add(self.eyes.eyes2)
        self.guy.add(self.mouse.mouse1)
        self.guy.move(200, 500)
        canvas.add(self.guy)
    def moving(self, angle) :
        self.guy.rotate(angle)

class Face :
    def __init__(self) :
        self.faces = Circle(50)
        self.faces.setBorderColor("bisque")
        self.faces.setFillColor("bisque")
        self.faces.setDepth(17)
        self.faces.move(-100, 0)

class Body :
    def __init__(self) :
        self.bodys = Ellipse(200, 80)
        self.bodys.setBorderColor("red")
        self.bodys.setFillColor("red")
        self.bodys.setDepth(19)
        self.bodys.move(10, 0)
    
class Arms :
    def __init__(self) :
        self.arm1 = Ellipse(100, 30)
        self.arm1.rotate(-33)
        self.arm1.setBorderColor("orange")
        self.arm1.setFillColor("orange")
        self.arm1.setDepth(18)
        self.arm1.move(-10, -60)

        self.arm2 = Ellipse(100, 30)
        self.arm2.rotate(33)
        self.arm2.setBorderColor("orange")
        self.arm2.setFillColor("orange")
        self.arm2.setDepth(16)
        self.arm2.move(-10, 60)
        
    def movings(self, angle) :
        self.arm1.rotate(angle)
        self.arm2.rotate(-angle)

class Hands :
    def __init__(self) :
        self.hand1 = Circle(15)
        self.hand1.setBorderColor("bisque")
        self.hand1.setFillColor("bisque")
        self.hand1.setDepth(14)
        self.hand1.move(23, 77)

        self.hand2 = Circle(15)
        self.hand2.setBorderColor("bisque")
        self.hand2.setFillColor("bisque")
        self.hand2.setDepth(14)
        self.hand2.move(20, -80)

class Eyes :
    def __init__(self) :
        self.eyes1 = Path(Point(30, 70), Point(30, 90))
        self.eyes1.setBorderColor("black")
        self.eyes1.setBorderWidth(6)
        self.eyes1.setDepth(15)
        self.eyes1.move(-140, -60)

        self.eyes2 = Path(Point(30, 70), Point(30, 90))
        self.eyes2.setBorderColor("black")
        self.eyes2.setBorderWidth(6)
        self.eyes2.setDepth(15)
        self.eyes2.move(-140, -100)

class Mouse :
    def __init__(self) :
        self.mouse1 = Circle(10)
        self.mouse1.setFillColor("black")
        self.mouse1.setDepth(15)
        self.mouse1.move(-70, -3)


class Sun :
    def __init__(self) :
        self.suns = Circle(25, Point(70, -180))
        self.suns.setFillColor("red")
        self.suns.setDepth(10)
        self.suns.setBorderColor('orange')
        self.suns.moveTo(150, 100)
        canvas.add(self.suns)


class Door :
    def __init__(self) :
        self.doors = Rectangle(200, 400, Point(900, 600))
        self.doors.setFillColor("chocolate")
        self.doors.setBorderColor("black")
        self.doors_sign = Rectangle(180, 380, Point(900, 600))
        self.doors_sign.setBorderColor("black")
        self.doors_hand = Circle()
        self.doors_hand.setRadius(10)
        self.doors_hand.setFillColor("black")
        self.doors_hand.moveTo(830, 600)
        self.doors_hand.setDepth(10)
        canvas.add(self.doors_hand)
        canvas.add(self.doors)
        canvas.add(self.doors_sign)


"""
class Scene2 :
    #canvas.setBackgroundColor("light blue")
    def __init__(self) :
        self.man = Man2()
        self.people = People()
        self.bus = Bus()
        self.ground = Ground()
        self.station = Station()
        self.suns = Sun2()
        self.cars = Car()

    def getting_anim_data(self) :
        return self.man, self.bus, self.people, self.cars


class Man2 :
    def __init__(self) :
        self.guy2 = Layer()
        self.faces2 = Face2()
        self.mouse2 = Mouse2()
        self.body2 = Body2()
        self.arms2 = Arms2()
        self.legs = Legs()
        self.eyes2 = Eyes2()
        self.hands2 = Hand2()
        #self.shoes = Shoes()
        
        self.guy2.add(self.faces2.faces2)
        self.guy2.add(self.mouse2.mouse2)
        self.guy2.add(self.body2.bodys2)
        self.guy2.add(self.arms2.arms1)
        self.guy2.add(self.arms2.arms2)
        self.guy2.add(self.legs.leg1)
        self.guy2.add(self.legs.leg2)
        self.guy2.add(self.eyes2.eyes1)
        self.guy2.add(self.eyes2.eyes2)
        self.guy2.add(self.hands2.hands1)
        self.guy2.add(self.hands2.hands2)
        #self.guy2.add(self.shoes.shoes1)
        #self.guy2.add(self.shoes.shoes2)
        
        self.guy2.move(100, 500)
        self.guy2.setDepth(40)
        canvas.add(self.guy2)
        
    def moving(self, x) :
        self.guy2.move(x, 0)

class Face2 :
    def __init__(self) :
        self.faces2 = Circle(30)
        self.faces2.setFillColor("bisque")
        self.faces2.setBorderColor("bisque")
        self.faces2.moveTo(0, -60)
        self.faces2.setDepth(30)

class Mouse2 :
    def __init__(self) :
        self.mouse2 = Rectangle(20, 10)
        self.mouse2.setFillColor("black")
        self.mouse2.setBorderColor("black")
        self.mouse2.setDepth(3)
        self.mouse2.move(0, -43)


class Body2 :
    def __init__(self) :
        self.bodys2 = Ellipse(30, 100)
        self.bodys2.setFillColor("salmon")
        self.bodys2.setBorderColor("salmon")
        self.bodys2.setDepth(32)
        self.bodys2.moveTo(0, -21)


class Arms2 :
    def __init__(self) :
        self.arms1 = Ellipse(15, 50)
        self.arms1.setFillColor("orange")
        self.arms1.setBorderColor("orange")
        self.arms1.moveTo(-27, -9)
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        
        self.arms2 = Ellipse(15, 50)
        self.arms2.setFillColor("orange")
        self.arms2.setBorderColor("orange")
        self.arms2.moveTo(25, -9)
        self.arms2.rotate(-30)
        self.arms2.setDepth(34)

    def shakings(self, angle) :
        #self.arms1.adjustReference(2, -4)
        self.arms1.rotate(angle)
        #self.arms2.adjustReference(-2, 4)
        self.arms2.rotate(-angle)


class Hand2 :
    def __init__(self) :
        self.hands1 = Circle(9)
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        self.hands1.move(-37, 10)
        
        self.hands2 = Circle(9)
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)
        self.hands2.move(37, 10)
    
    def shakings(self, angle) :
        self.hands1.rotate(angle)
        self.hands2.rotate(-angle)


        
class Legs :
    def __init__(self) :
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("dark blue")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(-5, 15)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("dark blue")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(5, 15)
        self.leg2.rotate(-19)
        self.leg2.setDepth(34)

    def shakings(self, angle) :
        self.leg1.rotate(angle)
        self.leg2.rotate(-angle)


class Shoes :
    def __init__(self) :
        self.shoes1 = Ellipse(20, 30)
        self.shoes1.setBorderColor("black")
        self.shoes1.setFillColor("black")
        self.shoes1.setDepth(14)
        self.shoes1.rotate(130)
        self.shoes1.move(-40, 65)

        self.shoes2 = Ellipse(20, 30)
        self.shoes2.setBorderColor("black")
        self.shoes2.setFillColor("black")
        self.shoes2.rotate(50)
        self.shoes2.setDepth(14)
        self.shoes2.move(40, 65)

    def shakings(self, angle) :
        self.shoes1.rotate(angle)
        self.shoes2.rotate(-angle)


class Eyes2 :
    def __init__(self) :
        self.eyes1 = Circle(3)
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        self.eyes1.moveTo(10, -65)
        
        self.eyes2 = Circle(3)
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(10)
        self.eyes2.moveTo(-10, -65)


class People :
    def __init__(self) :
        self.person1 = Person1()
        self.person2 = Person2()

class Person1 :
    def __init__(self) :
        self.guy3 = Layer()
        self.face3 = Face3()
        self.mouse3 = Mouse3()
        self.body3 = Body3()
        self.arms3 = Arms3()
        self.legs3 = Legs3()
        self.eyes3 = Eyes3()
        self.hands3 = Hand3()
        self.shoes3 = Shoes3()
        self.guy3.add(self.face3.faces3)
        self.guy3.add(self.body3.bodys3)
        self.guy3.add(self.mouse3.mouse3)
        self.guy3.add(self.legs3.leg1)
        self.guy3.add(self.legs3.leg2)
        self.guy3.add(self.arms3.arms1)
        self.guy3.add(self.arms3.arms2)
        self.guy3.add(self.eyes3.eyes1)
        self.guy3.add(self.eyes3.eyes2)
        self.guy3.add(self.hands3.hands1)
        self.guy3.add(self.hands3.hands2)
        self.guy3.add(self.shoes3.shoes1)
        self.guy3.add(self.shoes3.shoes2)

        self.guy3.move(600, 500)
        self.guy3.setDepth(30)
        canvas.add(self.guy3)

class Face3 :
    def __init__(self) :
        self.faces3 = Circle(30)
        self.faces3.setFillColor("bisque")
        self.faces3.setBorderColor("bisque")
        self.faces3.moveTo(0, -60)
        self.faces3.setDepth(30)
        canvas.add(self.faces3)

class Mouse3 :
    def __init__(self) :
        self.mouse3 = Rectangle(20, 10)
        self.mouse3.setFillColor("black")
        self.mouse3.setBorderColor("black")
        self.mouse3.setDepth(3)
        self.mouse3.move(0, -43)

        
class Body3 :
    def __init__(self) :
        self.bodys3 = Ellipse(30, 100)
        self.bodys3.setFillColor("yellow")
        self.bodys3.setBorderColor("yellow")
        self.bodys3.setDepth(32)
        self.bodys3.moveTo(0, -3)
        canvas.add(self.bodys3)

class Arms3 :
    def __init__(self) :
        self.arms1 = Ellipse(15, 50)
        self.arms1.setFillColor("red")
        self.arms1.setBorderColor("red")
        self.arms1.moveTo(-27, -9)
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        
        self.arms2 = Ellipse(15, 50)
        self.arms2.setFillColor("red")
        self.arms2.setBorderColor("red")
        self.arms2.moveTo(25, -9)
        self.arms2.rotate(-30)
        self.arms2.setDepth(30)
        
        canvas.add(self.arms1)
        canvas.add(self.arms2)

class Hand3 :
    def __init__(self) :
        self.hands1 = Circle(7)
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        self.hands1.move(-37, 7)

        self.hands2 = Circle(7)
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)
        self.hands2.move(37, 7)    

class Legs3 :
    def __init__(self) :
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("khaki")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(-5, 35)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("khaki")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(5, 35)
        self.leg2.rotate(-19)
        self.leg2.setDepth(30)

        canvas.add(self.leg1)
        canvas.add(self.leg2)


class Shoes3 :
    def __init__(self) :
        self.shoes1 = Ellipse(20, 30)
        self.shoes1.setBorderColor("black")
        self.shoes1.setFillColor("black")
        self.shoes1.rotate(90)
        self.shoes1.setDepth(14)
        self.shoes1.move(-33, 77)

        self.shoes2 = Ellipse(20, 30)
        self.shoes2.setBorderColor("black")
        self.shoes2.setFillColor("black")
        self.shoes2.rotate(90)
        self.shoes2.setDepth(14)
        self.shoes2.move(33, 77)


class Eyes3 :
    def __init__(self):
        self.eyes1 = Circle(3)
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        self.eyes1.moveTo(10, -65)
        
        self.eyes2 = Circle(3)
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(29)
        self.eyes2.moveTo(-10, -65)
        
        canvas.add(self.eyes1)
        canvas.add(self.eyes2)


class Person2 :
    def __init__(self) :
        self.guy4 = Layer()
        self.face4 = Face4()
        self.mouse4 = Mouse4()
        self.body4 = Body4()
        self.arms4 = Arms4()
        self.legs4 = Legs4()
        self.eyes4 = Eyes4()
        self.hands4 = Hand4()
        self.shoes4 = Shoes4()
        self.guy4.add(self.face4.faces4)
        self.guy4.add(self.body4.bodys4)
        self.guy4.add(self.mouse4.mouse4)
        self.guy4.add(self.legs4.leg1)
        self.guy4.add(self.legs4.leg2)
        self.guy4.add(self.arms4.arms1)
        self.guy4.add(self.arms4.arms2)
        self.guy4.add(self.eyes4.eyes1)
        self.guy4.add(self.eyes4.eyes2)
        self.guy4.add(self.hands4.hands1)
        self.guy4.add(self.hands4.hands2)
        self.guy4.add(self.shoes4.shoes1)
        self.guy4.add(self.shoes4.shoes2)
        
        self.guy4.move(650, 500)
        self.guy4.setDepth(30)
        canvas.add(self.guy4)

class Face4 :
    def __init__(self) :
        self.faces4 = Circle(30)
        self.faces4.setFillColor("bisque")
        self.faces4.setBorderColor("bisque")
        self.faces4.moveTo(50, -60)
        self.faces4.setDepth(30)
        canvas.add(self.faces4)
        
class Mouse4 :
    def __init__(self) :
        self.mouse4 = Rectangle(20, 10)
        self.mouse4.setFillColor("black")
        self.mouse4.setBorderColor("black")
        self.mouse4.setDepth(3)
        self.mouse4.move(50, -43)

class Body4 :
    def __init__(self) :
        self.bodys4 = Ellipse(30, 100)
        self.bodys4.setFillColor("brown")
        self.bodys4.setBorderColor("brown")
        self.bodys4.setDepth(32)
        self.bodys4.moveTo(50, -3)
        canvas.add(self.bodys4)

class Arms4 :
    def __init__(self) :
        self.arms1 = Ellipse(15, 50)
        self.arms1.setFillColor("blue")
        self.arms1.setBorderColor("blue")
        self.arms1.moveTo(23, -9)
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        
        self.arms2 = Ellipse(15, 50)
        self.arms2.setFillColor("blue")
        self.arms2.setBorderColor("blue")
        self.arms2.moveTo(75, -9)
        self.arms2.rotate(-30)
        self.arms2.setDepth(30)
        
        canvas.add(self.arms1)
        canvas.add(self.arms2)

class Hand4 :
    def __init__(self) :
        self.hands1 = Circle(7)
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)
        self.hands1.move(13, 7)

        self.hands2 = Circle(7)
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)
        self.hands2.move(87, 7)


class Legs4 :
    def __init__(self) :
        self.leg1 = Path(Point(225, 75), Point(210, 130))
        self.leg1.setBorderColor("tan")
        self.leg1.setBorderWidth(21)
        self.leg1.moveTo(45, 35)
        self.leg1.rotate(19)
        self.leg1.setDepth(30)
        
        self.leg2 = Path(Point(275, 75), Point(290, 130))
        self.leg2.setBorderColor("tan")
        self.leg2.setBorderWidth(21)
        self.leg2.moveTo(55, 35)
        self.leg2.rotate(-19)
        self.leg2.setDepth(30)
        
        canvas.add(self.leg1)
        canvas.add(self.leg2)

class Shoes4 :
    def __init__(self) :
        self.shoes1 = Ellipse(20, 30)
        self.shoes1.setBorderColor("black")
        self.shoes1.setFillColor("black")
        self.shoes1.rotate(90)
        self.shoes1.setDepth(14)
        self.shoes1.move(17, 77)

        self.shoes2 = Ellipse(20, 30)
        self.shoes2.setBorderColor("black")
        self.shoes2.setFillColor("black")
        self.shoes2.rotate(90)
        self.shoes2.setDepth(14)
        self.shoes2.move(83, 77)   

class Eyes4 :
    def __init__(self):
        
        self.eyes1 = Circle(3)
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        self.eyes1.moveTo(60, -65)
        
        self.eyes2 = Circle(3)
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(29)
        self.eyes2.moveTo(40, -65)
        
        canvas.add(self.eyes1)
        canvas.add(self.eyes2)
                

class Bus :
    def __init__(self) :
        
        self.auto = Layer()
        self.bodies = Bodies()
        self.wheels = Wheel()
        self.windows = Windows()
        self.logo = Logo()
        self.auto.add(self.bodies.bodiess)
        self.auto.add(self.wheels.wheelss1)
        self.auto.add(self.wheels.wheelss2)
        self.auto.add(self.windows.windowss1)
        self.auto.add(self.windows.windowss2)
        self.auto.add(self.windows.windowss3)
        self.auto.add(self.logo.logos)
        self.auto.move(-150, 550)
        self.auto.setDepth(20)
        canvas.add(self.auto)
        
    def moving(self, x) :
        self.auto.move(x, 0)

class Bodies :
    def __init__(self):
        self.bodiess = Rectangle(300, 175, Point(0, 0))
        self.bodiess.setFillColor("light gray")
        self.bodiess.setBorderColor("black")
        self.bodiess.setDepth(25)
        canvas.add(self.bodiess)
        
class Wheel :
    def __init__(self) :
        self.wheelss1 = Circle()
        self.wheelss1.setRadius(30)
        self.wheelss1.setFillColor("black")
        self.wheelss1.setDepth(24)
        self.wheelss1.moveTo(-67, 70)
        
        self.wheelss2 = Circle()
        self.wheelss2.setRadius(30)
        self.wheelss2.setFillColor("black")
        self.wheelss2.setDepth(24)
        self.wheelss2.moveTo(70, 70)
        
        canvas.add(self.wheelss1)
        canvas.add(self.wheelss2)

class Windows :
    def __init__(self) :
        self.windowss1 = Square(60)
        self.windowss1.setFillColor("light blue")
        self.windowss1.setBorderColor("black")
        self.windowss1.setDepth(23)
        self.windowss2 = Square(60)
        self.windowss2.setFillColor("light blue")
        self.windowss2.setBorderColor("black")
        self.windowss2.setDepth(23)
        self.windowss3 = Square(60)
        self.windowss3.setFillColor("light blue")
        self.windowss3.setBorderColor("black")
        self.windowss3.setDepth(23)
        self.windowss1.move(-80, 0)
        self.windowss2.move(0, 0)
        self.windowss3.move(80, 0)
        canvas.add(self.windowss1)
        canvas.add(self.windowss2)
        canvas.add(self.windowss3)

class Logo :
    def __init__(self) :
        self.logos = Text("Handong Global University", 20)
        self.logos.move(0, -20)
        self.logos.setDepth(5)
        canvas.add(self.logos)

class Station :
    def __init__(self) :
        self.roof = Roof()
        self.column = Column()

class Roof :
    def __init__(self) :
        self.roofs = Ellipse(200, 20)
        self.roofs.setFillColor("ghostwhite")
        self.roofs.setBorderColor("black")
        self.roofs.move(650, 475)
        canvas.add(self.roofs)

class Column :
    def __init__(self) :
        self.column1 = Rectangle(20, 150, Point(550, 540))
        self.column1.setFillColor("ghostwhite")
        self.column1.setBorderColor("black")
        self.column2 = Rectangle(20, 150, Point(750, 540))
        self.column2.setFillColor("ghostwhite")
        self.column2.setBorderColor("black")
        canvas.add(self.column1)
        canvas.add(self.column2)

class Sun2 :
    def __init__(self) :
        self.suns2 = Circle()
        self.suns2.setRadius(175)
        self.suns2.setFillColor("red")
        self.suns2.setBorderColor("orange")
        self.suns2.moveTo(35, 10)
        self.suns2.setDepth(10)
        canvas.add(self.suns2)

class Ground :
    def __init__(self) :
        self.ground = Rectangle(1000, 350, Point(500, 700))
        self.ground.setFillColor("light green")
        self.ground.setBorderColor("black")
        self.ground.setDepth(60)
        canvas.add(self.ground)

class Body_car :
    def __init__(self) :
        self.bodys_car = Polygon(Point(100, 500), Point(100, 550), Point(300, 550), Point(300, 500), Point(250, 500), Point(250, 450), Point(150, 450), Point(150, 500))
        self.bodys_car.moveTo(-100, 0)
        self.bodys_car.setFillColor("black")
        self.bodys_car.setDepth(25)
        canvas.add(self.bodys_car)

class Wheelss :
    def __init__(self) :
        self.wheelss1 = Circle()
        self.wheelss1.setRadius(25)
        self.wheelss1.setFillColor("black")
        self.wheelss1.setDepth(24)
        self.wheelss1.moveTo(-65, 70)
        self.wheelss2 = Circle()
        self.wheelss2.setRadius(25)
        self.wheelss2.setFillColor("black")
        self.wheelss2.setDepth(24)
        self.wheelss2.moveTo(70, 70)
        canvas.add(self.wheelss1)
        canvas.add(self.wheelss2)

class Windowss :
    def __init__(self) :
        self.windowss1 = Square(60)
        self.windowss1.setFillColor("light blue")
        self.windowss1.setBorderColor("black")
        self.windowss1.setDepth(23)
        self.windowss1.move(0, 0)
        canvas.add(self.windowss1)

class Car(Bus) :
    def __init__(self) :
        self.body_car = Body_car()
        self.autos = Layer()
        self.wheelss = Wheelss()
        self.windowss = Windowss()
        self.autos.add(self.body_car.bodys_car)
        self.autos.add(self.wheelss.wheelss1)
        self.autos.add(self.wheelss.wheelss2)
        self.autos.add(self.windowss.windowss1)
        self.autos.move(-150, 550)
        self.autos.setDepth(20)
        canvas.add(self.autos)

    def moving(self, x) :
        self.autos.move(x, 0)


class Animation2 :
    def __init__(self, scene2) :
        man, bus, people, car = scene2.getting_anim_data()
        self.mans = man
        self.buss = bus
        self.peoples = people
        self.cars = car

   # 팔의 기준축을 어떻게 설정하지?? -- adjustReference를 한번 이용해보자!
    def animating(self) :
        self.mans.arms2.arms1.adjustReference(0, -12)
        self.mans.arms2.arms2.adjustReference(0, -12)
        self.mans.hands2.hands1.adjustReference(0, -30)
        self.mans.hands2.hands2.adjustReference(0, -30)
        self.mans.legs.leg1.adjustReference(1, -12)
        self.mans.legs.leg2.adjustReference(1, -12)
        #self.mans.arms2.arms2.adjustReference(-7, 7)
        
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
            self.buss.moving(70)
        canvas.remove(self.peoples.person1.guy3)
        canvas.remove(self.peoples.person2.guy4)
        time.sleep(1)
        text = Text("what..?", 20)
        text.moveTo(200, 380)
        canvas.add(text)
        time.sleep(1)
        canvas.remove(text)
        text1 = Text("Wait!!", 30)
        text1.moveTo(200, 380)
        canvas.add(text1)
        time.sleep(0.5)
        canvas.remove(text1)
        
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
            self.buss.moving(80)
        
        time.sleep(2)
        for i in range(15) :
            self.mans.arms2.shakings(10)
            self.mans.hands2.shakings(12)
        
        change_eye1 = Rectangle(15, 5, Point(335, 429))
        change_eye1.setFillColor("black")
        change_eye1.setBorderColor("black")
        change_eye1.rotate(-30)
        change_eye1.setDepth(19)
        
        change_eye2 = Rectangle(15, 5, Point(365, 429))
        change_eye2.setFillColor("black")
        change_eye2.setBorderColor("black")
        change_eye2.rotate(30)
        change_eye2.setDepth(19)
        
        canvas.add(change_eye1)
        canvas.add(change_eye2)
        
        text3 = Text("What should I do?", 20)
        text3.moveTo(300, 380)
        canvas.add(text3)

        for i in range(6) :
            time.sleep(0.3)
            self.cars.moving(70)

def animate_people_bus(scene2) :
    animation2 = Animation2(scene2)
    animation2.animating()



class Scene3 :
    def __init__(self) :
        self.man3 = Man3()
        self.car2 = Car2()
        self.window3 = Window3()
        self.professor = Professor()
        self.sun3 = Sun3()
        
    def get_data(self) :
        return self.man3, self.car2, self.window3, self.professor, self.sun3

class Sun3 :
    def __init__(self) :
        self.sun3 = Circle(150 ,Point(-10, -10))
        self.sun3.setFillColor('red')
        self.sun3.setBorderColor('orange')
        canvas.add(self.sun3)
        self.sun3.setDepth(10)

class Man3 :
    def __init__(self) :
        self.guy = Layer()

        self.body3 = Ellipse(250, 700, Point(0, 0))
        self.body3.setDepth(70)
        self.body3.setFillColor('salmon')
        self.body3.setBorderColor('salmon')
        self.guy.add(self.body3)
        
        self.face3 = Circle(110, Point(0, -300))
        self.face3.setBorderColor("bisque")
        self.face3.setFillColor("bisque")
        self.face3.setDepth(50)
        self.guy.add(self.face3)
        
        self.arm3 = Ellipse(70, 270, Point(139, -100))
        self.arm3.setFillColor("orange")
        self.arm3.setBorderColor("orange")
        self.arm3.rotate(-18)
        self.arm3.setDepth(34)
        self.guy.add(self.arm3)

        self.hand3 = Circle(23)
        self.hand3.setBorderColor("bisque")
        self.hand3.setFillColor("bisque")
        self.hand3.setDepth(34)
        self.hand3.move(170, 9)
        self.guy.add(self.hand3)
        
        self.mouth3 = Circle(21, Point(0, -250))
        self.mouth3.setFillColor("black")
        self.mouth3.setDepth(10)
        self.guy.add(self.mouth3)

        self.eyes1 = Circle(15, Point(50, -330))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(1)
        self.guy.add(self.eyes1)
        self.eyes2 = Circle(15, Point(-50, -330))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(1)
        self.guy.add(self.eyes2)
        
        self.guy.moveTo(100, 600)
        self.guy.setDepth(10)
        
        canvas.add(self.guy)

    def moving_head(self, x) :
        self.face3.move(0, x)
        self.mouse3.move(0, x)
        self.eyes1.move(0, x)
        self.eyes2.move(0, x)
        
class Car2() :
    def __init__(self) :
        self.car = Polygon(Point(100, 600), Point(300, 600), Point(400, 400), Point(700, 400), Point(900, 600), Point(1100, 600), Point(1100, 900), Point(100, 900))
        self.car.setDepth(50)
        self.car.setFillColor('black')
        canvas.add(self.car)

class Window3 :
    def __init__(self) :
        self.window = Polygon(Point(300, 630), Point(410, 420), Point(690, 420), Point(910, 630))
        self.window.setDepth(40)
        self.window.setBorderColor('light blue')
        self.window.setFillColor('darkgoldenrod')
        canvas.add(self.window)


class Professor :
    def __init__(self) :
        self.pros = Layer()
        
        self.body = Ellipse(250, 550, Point(200, 0))
        self.body.setDepth(45)
        self.body.setFillColor('black')
        self.body.setBorderColor('black')
        self.pros.add(self.body)

        self.face = Circle(70, Point(200, -300))
        self.face.setDepth(23)
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.pros.add(self.face)

        self.mouth = Rectangle(30, 15, Point(200, -260))
        self.mouth.setFillColor("black")
        self.mouth.setBorderColor("black")
        self.mouth.setDepth(22)
        self.pros.add(self.mouth)

        self.eye1 = Path(Point(160,-300),Point(170,-310),Point(180,-300))
        self.eye1.setBorderWidth(3)
        self.eye1.setDepth(20)
        self.pros.add(self.eye1)
        self.eye2 = Path(Point(220,-300),Point(230,-310),Point(240,-300))
        self.eye2.setBorderWidth(3)
        self.eye2.setDepth(20)
        self.pros.add(self.eye2)

        # 안경(glasses)
        self.glasses1 = Rectangle(35, 25, Point(170, -304))
        self.glasses1.setDepth(22)
        self.glasses1.setBorderWidth(3)
        self.glasses1.setBorderColor('black')
        self.pros.add(self.glasses1)
        self.glasses2 = Rectangle(35, 25, Point(230, -304))
        self.glasses2.setDepth(22)
        self.glasses2.setBorderWidth(3)
        self.glasses2.setBorderColor('black')
        self.pros.add(self.glasses2)

        # 안경테(glasses frame)
        self.gf1 = Path(Point(130,-311),Point(151,-301))
        self.gf1.setBorderWidth(3)
        self.gf1.setDepth(22)
        self.pros.add(self.gf1)
        self.gf2 = Path(Point(190,-300),Point(212,-300))
        self.gf2.setBorderWidth(3)
        self.gf2.setDepth(22)
        self.pros.add(self.gf2)
        self.gf3 = Path(Point(249,-301),Point(270,-311))
        self.gf3.setBorderWidth(3)
        self.gf3.setDepth(22)
        self.pros.add(self.gf3)

        self.pros.moveTo(400, 800)
        self.pros.setDepth(20)
        canvas.add(self.pros)

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
        text = Text("What are you doing?", 30)
        text.moveTo(600, 300)
        canvas.add(text)
        time.sleep(2)
        canvas.remove(text)
        text1 = Text("Oh! Hi Professor!!", 30)
        text1.moveTo(300, 150)
        canvas.add(text1)
        time.sleep(2)
        canvas.remove(text1)
        text2 = Text("Hmm....", 30)
        text2.moveTo(600, 300)
        canvas.add(text2)
        time.sleep(2)
        canvas.remove(text2)
        text3 = Text("I guess you lost your bus, right?", 30)
        text3.moveTo(600, 300)
        canvas.add(text3)
        time.sleep(2)
        canvas.remove(text3)
        time.sleep(1)
        tear = Ellipse(15, 20, Point(153, 269))
        tear.setDepth(10)
        tear.setFillColor("blue")
        tear.setBorderColor("blue")
        canvas.add(tear)

        for i in range(5) :
            time.sleep(0.1)
            self.man.moving_head(5)
            tear.move(0, 30)
        
        canvas.remove(tear)
        text4 = Text("Yes..", 30)
        text4.moveTo(300, 150)
        time.sleep(2)
        canvas.add(text4)
        time.sleep(2)
        canvas.remove(text4)
        text5 = Text("Hey, then... Get on my Car!", 30)
        text5.moveTo(600, 300)
        canvas.add(text5)
        time.sleep(1)
        canvas.remove(text5)
        for i in range(5) :
            time.sleep(0.08)
            self.man.moving_head(-5)
        text6 = Text("Oh? Really?", 30)
        text6.moveTo(300, 150)
        time.sleep(2)
        canvas.add(text6)
        time.sleep(1)
        canvas.remove(text6)
        time.sleep(2)
        canvas.remove(self.man.body3)
        canvas.remove(self.man.face3)
        canvas.remove(self.car.car)
        canvas.remove(self.window.window)
        canvas.remove(self.professor.face)
        canvas.remove(self.professor.body)
        canvas.remove(self.sun.sun3)

def animate_Scene3(scene3) :
    animation3 = Animation3(scene3)
    animation3.animating()      




class Scene4 :
    def __init__(self) :
        self.man5 = Man5()
        self.professor2 = Professor2()
        self.chair1 = Chair1()
        self.chair2 = Chair2()
        #self.backmirror = Backmirror()
        self.sidewindow1 = Sidewindow1()
        self.sidewindow2 = Sidewindow2()
        self.sidetree1 = Sidetree1()
        #self.sidetree2 = Sidetree2()
        self.ground2 = Ground2()
    def get_datas(self) :
        return self.man5, self.professor2, self.chair1, self.chair2, self.sidewindow1, self.sidewindow2, self.sidetree1 #self.sidetree2

class Ground2 :
    def __init__(self) :
        self.ground2 = Polygon(Point(0,500), Point(300, 280), Point(300, 380), Point(0, 600))
        self.ground2.setFillColor("light green")
        self.ground2.setBorderColor("black")
        self.ground2.setDepth(30)
        canvas.add(self.ground2)
        

class Sidewindow1 :
    def __init__(self) :
        self.sidewindow1 = Polygon(Point(0, 300), Point(300, 80), Point(300, 380), Point(0, 600))
        self.sidewindow1.setFillColor("light blue")
        self.sidewindow1.setDepth(30)
        canvas.add(self.sidewindow1)

class Sidewindow2 :
    def __init__(self) :
        self.sidewindow2 = Polygon(Point(700, 80), Point(1000, 300), Point(1000, 600), Point(700, 380))
        self.sidewindow2.setFillColor("light blue")
        self.sidewindow2.setDepth(30)
        canvas.add(self.sidewindow2)

class Chair1 :
    def __init__(self) :
        self.chair1 = Rectangle(300, 500, Point(300, 700))
        self.chair1.setFillColor('gray')
        self.chair1.setBorderColor('gray')
        self.chair1.setDepth(25)
        canvas.add(self.chair1)

class Chair2 :
    def __init__(self) :
        self.chair2 = Rectangle(300, 500, Point(700, 700))
        self.chair2.setFillColor('gray')
        self.chair2.setBorderColor('gray')
        self.chair2.setDepth(25)
        canvas.add(self.chair2)


class Man5 :
    def __init__(self) :
        self.final_body = Final_body()
        self.final_face = Final_face()
        self.final_arm1 = Final_arm1() 
        self.final_arm2 = Final_arm2()
        self.final_mouth = Final_mouth()
        self.final_eyes = Final_eyes()
        
        self.final_guy = Layer()
        self.final_guy.add(self.final_body.body)
        self.final_guy.add(self.final_face.face)
        self.final_guy.add(self.final_arm1.arm) # 여기 어디가 에러가 떴는지 빨리 보자!
        self.final_guy.add(self.final_arm2.arm)
        self.final_guy.add(self.final_mouth.mouth)
        self.final_guy.add(self.final_eyes.eyes1)
        self.final_guy.add(self.final_eyes.eyes2)

        self.final_guy.moveTo(400, 700)
        self.final_guy.setDepth(10)
        canvas.add(self.final_guy)

class Final_body :
    def __init__(self) :
        self.body = Ellipse(150, 350, Point(-100, -100))
        self.body.setFillColor('salmon')
        self.body.setDepth(20)
        self.body.setBorderColor('salmon')
        canvas.add(self.body)

class Final_face :
    def __init__(self) :
        self.face = Circle()
        self.face.setRadius(60)
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.face.setDepth(19)
        self.face.moveTo(-95, -270)
        canvas.add(self.face)

class Final_arm1 :
    def __init__(self) :
        self.arm = Ellipse(50, 200)
        self.arm.setFillColor('orange')
        self.arm.setBorderColor('orange')
        self.arm.setDepth(18)
        self.arm.moveTo(230, 560)
        self.arm.rotate(20)
        canvas.add(self.arm)

class Final_arm2 :
    def __init__(self) :
        self.arm = Ellipse(50, 200)
        self.arm.setFillColor('orange')
        self.arm.setBorderColor('orange')
        self.arm.setDepth(18)
        self.arm.moveTo(370, 560)
        self.arm.rotate(-20)
        canvas.add(self.arm)

class Final_mouth :
    def __init__(self) :
        self.mouth = Rectangle(30, 15, Point(-95, -240))
        self.mouth.setFillColor("black")
        self.mouth.setDepth(10)

class Final_eyes :
    def __init__(self) :
        self.eyes1 = Circle(10, Point(-125, -289))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        
        self.eyes2 = Circle(10, Point(-65, -289))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(10)




class Professor2 :
    def __init__(self) :
        self.final_bodys = Final_bodys()
        self.final_faces = Final_faces()
        self.final_arm1s = Final_arm1s()
        self.final_arm2s = Final_arm2s()
        self.final_mouths = Final_mouths()
        self.final_eyess = Final_eyess()
        self.final_glasses = Final_glasses()
        self.final_gf = Final_gf()
        
        self.male = Layer()
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
        canvas.add(self.male)

class Final_bodys :
    def __init__(self) :
        self.body = Ellipse(150, 350)
        self.body.setFillColor('black')
        self.body.setDepth(20)
        self.body.setBorderColor('black')
        self.body.moveTo(-100, -100)

class Final_faces :
    def __init__(self) :
        self.face = Circle()
        self.face.setRadius(60)
        self.face.setFillColor('bisque')
        self.face.setBorderColor('bisque')
        self.face.setDepth(19)
        self.face.moveTo(-95, -270)

class Final_arm1s :
    def __init__(self) :
        self.arm1 = Ellipse(50, 180)
        self.arm1.setFillColor('beige')
        self.arm1.setBorderColor('beige')
        self.arm1.setDepth(9)
        self.arm1.moveTo(650, 575)
        self.arm1.adjustReference(0, -100)
        self.arm1.rotate(10)
        canvas.add(self.arm1)

    def moving(self, x) :
        self.arm1.adjustReference(0+x, 0-x)
        self.arm1.rotate(x)

class Final_arm2s :
    def __init__(self) :
        self.arm2 = Ellipse(50, 200)
        self.arm2.setFillColor('beige')
        self.arm2.setBorderColor('beige')
        self.arm2.setDepth(18)
        self.arm2.moveTo(700, 600)
        self.arm2.adjustReference(0, -100)
        self.arm2.rotate(-90)
        canvas.add(self.arm2)

class Final_mouths :
    def __init__(self) :
        self.mouth = Rectangle(30, 15, Point(-95, -240))
        self.mouth.setFillColor("black")
        self.mouth.setDepth(18)

class Final_eyess :
    def __init__(self) :
        self.eye1 = Path(Point(-109,-280),Point(-119,-290),Point(-129,-280))
        self.eye1.setBorderWidth(3)
        self.eye1.setDepth(10)
        
        self.eye2 = Path(Point(-60,-280),Point(-70,-290),Point(-80,-280))
        self.eye2.setBorderWidth(3)
        self.eye2.setDepth(10)

class Final_glasses :
    def __init__(self) :
        self.glasses1 = Rectangle(35, 25, Point(-120, -285))
        self.glasses1.setDepth(10)
        self.glasses1.setBorderWidth(3)
        self.glasses1.setBorderColor('black')
        
        self.glasses2 = Rectangle(35, 25, Point(-70, -285))
        self.glasses2.setDepth(10)
        self.glasses2.setBorderWidth(3)
        self.glasses2.setBorderColor('black')

class Final_gf :
    def __init__(self) :
        self.gf1 = Path(Point(-36,-291),Point(-51,-281))
        self.gf1.setBorderWidth(3)
        self.gf1.setDepth(10)
        self.gf2 = Path(Point(-100,-281),Point(-88,-281))
        self.gf2.setBorderWidth(3)
        self.gf2.setDepth(10)
        self.gf3 = Path(Point(-138,-281),Point(-152,-291))
        self.gf3.setBorderWidth(3)
        self.gf3.setDepth(10)


class Sidetree1 :
    def __init__(self) :
        self.tree1 = Tree1s()
        self.tree2 = Tree2s()
        self.leaf = Leafs()
        self.trees = Layer()
        self.trees.add(self.tree1.tree)
        self.trees.add(self.tree2.tree)
        self.trees.add(self.leaf.leaf)
        self.trees.moveTo(600, 435)
        self.trees.setDepth(26)
        canvas.add(self.trees)
    def moving(self, x) :
        self.trees.move(-x, x)

class Tree1s :
    def __init__(self) :
        self.tree = Rectangle(50, 100, Point(-400, -130))
        self.tree.setFillColor('brown')
        self.tree.setBorderColor('brown')
        self.tree.setDepth(26)
        #self.tree.rotate(-30)
        canvas.add(self.tree)

class Tree2s :
    def __init__(self) :
        self.tree = Polygon(Point(-470, -80), Point(-330, -80), Point(-400, -130))
        self.tree.setFillColor('brown')
        self.tree.setBorderColor('brown')
        self.tree.setDepth(26)
        #self.tree.rotate(-45)
        canvas.add(self.tree)

class Leafs :
    def __init__(self) :
        self.leaf = Circle(40, Point(-400, -200))
        self.leaf.setFillColor('dark green')
        self.leaf.setDepth(23)
        canvas.add(self.leaf)

class Animation4 :
    def __init__(self, scene4) :
        man, professor, chair1, chair2, sidewindow1, sidewindow2, sidetree1= scene4.get_datas()
        self.man = man
        self.professor = professor
        self.chair1 = chair1
        self.chair2 = chair2
        #self.backmirror = backmirror
        self.sidewindow1 = sidewindow1
        self.sidewindow2 = sidewindow2
        self.sidetree1 = sidetree1
        #self.sidetree2 = sidetree2
        
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
            
        text = Text("Are you tired?", 30)
        text.moveTo(600, 300)
        canvas.add(text)
        time.sleep(1)
        canvas.remove(text)
        
        text1 = Text("I'm a little tired \n because it's the end of the semester...", 30)
        text1.moveTo(330, 300)
        text1.setDepth(5)
        canvas.add(text1)
        time.sleep(1)
        canvas.remove(text1)
        
        text2 = Text("You're getting through really well.", 30)
        text2.moveTo(600, 300)
        text2.setDepth(5)
        canvas.add(text2)
        time.sleep(1)
        canvas.remove(text2)

        text3 = Text("Professor... am I really doing well?", 30)
        text3.moveTo(330, 300)
        text3.setDepth(5)
        canvas.add(text3)
        time.sleep(1)
        canvas.remove(text3)

        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(-i)
        #self.professor.final_arm1s.moving(-i)
        for i in range(10) :
            time.sleep(0.15)
            self.professor.final_arm1s.moving(i)

        text4 = Text("I'd really like to compliment you \n on the hard work and time you've invested.", 30)
        text4.moveTo(600, 300)
        text4.setDepth(5)
        canvas.add(text4)
        time.sleep(1)
        canvas.remove(text4)
        
        text3 = Text("I really wanted to hear this cheering. \n Thank you.", 30)
        text3.moveTo(330, 300)
        text3.setDepth(5)
        canvas.add(text3)
        time.sleep(1)
        canvas.remove(text3)
        

def animate_Scene4(scene4) :
    animation4 = Animation4(scene4)
    animation4.animating()
"""
def main():
    # Scene 1
    canvas.setBackgroundColor("light green")
    scene1 = Scene1()
    animate_man(scene1)
    # Scene 2
    #canvas.setBackgroundColor("light blue")
    #scene2 = Scene2()
    #animate_people_bus(scene2)
    # Scene 3
    #canvas.setBackgroundColor("light blue")
    #scene3 = Scene3()
    #animate_Scene3(scene3)
    # Scene 4
    #canvas.setBackgroundColor("darkgoldenrod")
    #scene4 = Scene4()
    #animate_Scene4(scene4)

main()



