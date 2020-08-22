from cs1graphics import *
import time
canvas = Canvas(1000, 700)
"""
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
        self.sun = Sun2()
        self.car = Car()
        self.tree = Tree()
        self.trees = Trees()
        self.building = Building()
        self.bird = Bird()
        

    def getting_anim_data(self) :
        return self.man, self.bus, self.people, self.car, self.sun, self.ground, self.station, self.tree.trees, self.trees.trees, self.building.building, self.bird

class Man2 :
    def __init__(self) :
        self.guy2 = Layer()
        
        self.faces2 = Face2()
        self.mouth2 = Mouth2()
        self.body2 = Body2()
        self.arms2 = Arms2()
        self.legs = Legs()
        self.eyes2 = Eyes2()
        self.hands2 = Hand2()
        
        self.guy2.add(self.faces2.faces2)
        self.guy2.add(self.mouth2.mouth2)
        self.guy2.add(self.body2.bodys2)
        self.guy2.add(self.arms2.arms1)
        self.guy2.add(self.arms2.arms2)
        self.guy2.add(self.legs.leg1)
        self.guy2.add(self.legs.leg2)
        self.guy2.add(self.eyes2.eyes1)
        self.guy2.add(self.eyes2.eyes2)
        self.guy2.add(self.hands2.hands1)
        self.guy2.add(self.hands2.hands2)
        
        self.guy2.move(100, 500)
        self.guy2.setDepth(40)
        canvas.add(self.guy2)
        
    def moving(self, x) :
        self.guy2.move(x, 0)

class Bird:
    def __init__(self):
        self.bird = Layer()
        
        self.face = Circle(23, Point(23, -23))
        self.face.setFillColor('red')
        self.face.setBorderWidth(3)
        self.face.setDepth(60)
        self.bird.add(self.face)
        
        self.hair1 = Ellipse(10, 20, Point(30, -46))
        self.hair1.setFillColor('red')
        self.hair1.setBorderWidth(2)
        self.bird.add(self.hair1)
        
        self.hair2 = Ellipse(10,20, Point(33, -46))
        self.hair2.setFillColor('red')
        self.hair1.setBorderWidth(2)
        self.hair2.rotate(45)
        self.bird.add(self.hair2)
        
        self.eyebrow1 = Polygon(Point(0, -23), Point(12,-22), Point(5, -29))
        self.eyebrow1.setFillColor('yellow')
        self.bird.add(self.eyebrow1)

        self.eyebrow1 = Polygon(Point(23, -23), Point(12,-22), Point(17, -29))
        self.eyebrow1.setFillColor('yellow')
        self.bird.add(self.eyebrow1)
        
        self.eye1 = Circle(4, Point(8,-20))
        self.eye1.setFillColor('white')
        self.eye1.setDepth(60)
        self.bird.add(self.eye1)
        
        self.eye2 = Circle(4, Point(16,-20))
        self.eye2.setFillColor('white')
        self.eye2.setDepth(60)
        self.bird.add(self.eye2)
        
        self.eye3 = Circle(1, Point(9, -19))
        self.eye3.setFillColor('black')
        self.bird.add(self.eye3)
        
        self.eye4 = Circle(1, Point(14, -19))
        self.eye4.setFillColor('black')
        self.bird.add(self.eye4)
        
        self.mouth1 = Ellipse(23, 14, Point(23, -7))
        self.mouth1.setFillColor('white')
        self.bird.add(self.mouth1)
        
        self.mouth2 = Polygon(Point(12, -15), Point(16, -8), Point(4,-8))
        self.mouth2.setFillColor('yellow')
        self.bird.add(self.mouth2)
        
        self.mouth3 = Polygon(Point(12, -3), Point(16, -8), Point(5,-8))
        self.mouth3.setFillColor('yellow')
        self.bird.add(self.mouth3)
        
        self.tale = Polygon(Point(45,-23), Point(52, -27), Point(50, -29))
        self.tale.setFillColor('black')
        self.bird.add(self.tale)
        
        self.tale2 = Polygon(Point(45,-23), Point(52, -19), Point(50, -17))
        self.tale2.setFillColor('black')
        self.bird.add(self.tale2)
        
        self.tale3 = Polygon(Point(45,-23), Point(54, -21), Point(54, -23))
        self.tale3.setFillColor('black')
        self.bird.add(self.tale3)
        self.bird.setDepth(20)
        
        self.bird.moveTo(800, 100)
        canvas.add(self.bird)
    def moving(self, x) :
        self.bird.move(-x, 2*x)
    def moving2(self, x) :
        self.bird.move(-x, -4*x)



class Tree :
    def __init__(self) :
        self.tree1 = Tree1()
        self.tree2 = Tree2()
        self.leaf = Leaf()
        self.trees = Layer()
        self.trees.add(self.tree1.tree1s)
        self.trees.add(self.tree2.tree2s)
        self.trees.add(self.leaf.leafs)
        self.trees.moveTo(850, 580)
        self.trees.setDepth(60)
        canvas.add(self.trees)
        
        
class Tree1 :
    def __init__(self) :
        self.tree1s = Rectangle(80, 200, Point(0, -100))
        self.tree1s.setFillColor("brown")
        #canvas.add(self.tree1s)

class Tree2 :
    def __init__(self) :
        self.tree2s = Polygon(Point(-70, 0), Point(70, 0), Point(0, -50))
        self.tree2s.setFillColor('brown')
        self.tree2s.setDepth(60)
        #canvas.add(self.tree2s)

class Leaf :
    def __init__(self) :
        self.leafs = Circle(80, Point(0, -200))
        self.leafs.setFillColor('dark green')
        #canvas.add(self.leafs)
class Trees :
    def __init__(self) :
        self.tree1 = Tree1()
        self.tree2 = Tree2()
        self.leaf = Leaf()
        self.trees = Layer()
        self.trees.add(self.tree1.tree1s)
        self.trees.add(self.tree2.tree2s)
        self.trees.add(self.leaf.leafs)
        self.trees.moveTo(650, 580)
        self.trees.setDepth(60)
        canvas.add(self.trees)
        
        
class Trees1 :
    def __init__(self) :
        self.tree1s = Rectangle(80, 200, Point(0, -100))
        self.tree1s.setFillColor("brown")
        #canvas.add(self.tree1s)

class Trees2 :
    def __init__(self) :
        self.tree2s = Polygon(Point(-70, 0), Point(70, 0), Point(0, -50))
        self.tree2s.setFillColor('brown')
        self.tree2s.setDepth(60)
        #canvas.add(self.tree2s)

class Leafs :
    def __init__(self) :
        self.leafs = Circle(80, Point(0, -200))
        self.leafs.setFillColor('dark green')
        #canvas.add(self.leafs)

class Face2 :
    def __init__(self) :
        self.faces2 = Circle(30)
        self.faces2.setFillColor("bisque")
        self.faces2.setBorderColor("bisque")
        self.faces2.moveTo(0, -60)
        self.faces2.setDepth(30)

class Mouth2 :
    def __init__(self) :
        self.mouth2 = Rectangle(20, 10)
        self.mouth2.setFillColor("black")
        self.mouth2.setBorderColor("black")
        self.mouth2.setDepth(3)
        self.mouth2.move(0, -43)


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


class Eyes2 :
    def __init__(self) :
        self.eyes1 = Circle(3, Point(10, -65))
        self.eyes1.setFillColor("black")
        self.eyes1.setDepth(10)
        
        self.eyes2 = Circle(3, Point(-10, -65))
        self.eyes2.setFillColor("black")
        self.eyes2.setDepth(10)


class People :
    def __init__(self) :
        self.person1 = Person1()
        self.person2 = Person2()

class Person1 :
    def __init__(self) :
        self.guy3 = Layer()
        
        self.face3 = Face3()
        self.mouth3 = Mouth3()
        self.body3 = Body3()
        self.arms3 = Arms3()
        self.legs3 = Legs3()
        self.eyes3 = Eyes3()
        self.hands3 = Hand3()
        
        self.guy3.add(self.face3.faces3)
        self.guy3.add(self.body3.bodys3)
        self.guy3.add(self.mouth3.mouth3)
        self.guy3.add(self.legs3.leg1)
        self.guy3.add(self.legs3.leg2)
        self.guy3.add(self.arms3.arms1)
        self.guy3.add(self.arms3.arms2)
        self.guy3.add(self.eyes3.eyes1)
        self.guy3.add(self.eyes3.eyes2)
        self.guy3.add(self.hands3.hands1)
        self.guy3.add(self.hands3.hands2)

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

class Mouth3 :
    def __init__(self) :
        self.mouth3 = Rectangle(20, 10, Point(0, -43))
        self.mouth3.setFillColor("black")
        self.mouth3.setBorderColor("black")
        self.mouth3.setDepth(3)
        
class Body3 :
    def __init__(self) :
        self.bodys3 = Ellipse(30, 100, Point(0, -3))
        self.bodys3.setFillColor("yellow")
        self.bodys3.setBorderColor("yellow")
        self.bodys3.setDepth(32)

class Arms3 :
    def __init__(self) :
        self.arms1 = Ellipse(15, 50, Point(-27, -9))
        self.arms1.setFillColor("red")
        self.arms1.setBorderColor("red")
        self.arms1.rotate(30)
        self.arms1.setDepth(30)
        
        self.arms2 = Ellipse(15, 50, Point(25, -9))
        self.arms2.setFillColor("red")
        self.arms2.setBorderColor("red")
        self.arms2.rotate(-30)
        self.arms2.setDepth(30)

class Hand3 :
    def __init__(self) :
        self.hands1 = Circle(7, Point(-37, 7))
        self.hands1.setBorderColor("bisque")
        self.hands1.setFillColor("bisque")
        self.hands1.setDepth(14)

        self.hands2 = Circle(7, Point(37, 7))
        self.hands2.setBorderColor("bisque")
        self.hands2.setFillColor("bisque")
        self.hands2.setDepth(14)

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


class Person2 :
    def __init__(self) :
        self.guy4 = Layer()
        
        self.face4 = Face4()
        self.mouth4 = Mouth4()
        self.body4 = Body4()
        self.arms4 = Arms4()
        self.legs4 = Legs4()
        self.eyes4 = Eyes4()
        self.hands4 = Hand4()
        
        self.guy4.add(self.face4.faces4)
        self.guy4.add(self.body4.bodys4)
        self.guy4.add(self.mouth4.mouth4)
        self.guy4.add(self.legs4.leg1)
        self.guy4.add(self.legs4.leg2)
        self.guy4.add(self.arms4.arms1)
        self.guy4.add(self.arms4.arms2)
        self.guy4.add(self.eyes4.eyes1)
        self.guy4.add(self.eyes4.eyes2)
        self.guy4.add(self.hands4.hands1)
        self.guy4.add(self.hands4.hands2)
        
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
        
class Mouth4 :
    def __init__(self) :
        self.mouth4 = Rectangle(20, 10)
        self.mouth4.setFillColor("black")
        self.mouth4.setBorderColor("black")
        self.mouth4.setDepth(3)
        self.mouth4.move(50, -43)

class Body4 :
    def __init__(self) :
        self.bodys4 = Ellipse(30, 100)
        self.bodys4.setFillColor("brown")
        self.bodys4.setBorderColor("brown")
        self.bodys4.setDepth(32)
        self.bodys4.moveTo(50, -3)

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
        
                

class Bus :
    def __init__(self):
        self.bus = Layer()
        
        self.busbody = Rectangle(400, 250, Point(200, -125))
        self.busbody.setFillColor('darkblue')
        self.bus.add(self.busbody)
        
        self.window1 = Rectangle(150, 100, Point(100, -170))
        self.window1.setFillColor('lightskyblue')
        self.bus.add(self.window1)
        
        self.window2 = Rectangle(150, 100, Point(200, -170))
        self.window2.setFillColor('lightskyblue')
        self.bus.add(self.window2)

        self.window3 = Rectangle(150, 100, Point(300, -170))
        self.window3.setFillColor('lightskyblue')
        self.bus.add(self.window3)
        
        self.tire1 = Circle(50, Point(100, 0))
        self.tire1.setFillColor('black')
        self.bus.add(self.tire1)
        
        self.tire2 = Circle(50, Point(300, 0))
        self.tire2.setFillColor('black')
        self.bus.add(self.tire2)
        self.bus.setDepth(10)
        
        self.bus.moveTo(-400, 550)
        canvas.add(self.bus)
        
    def moving(self, x) :
        self.bus.move(x, 0)

class Building:
    def __init__(self) :
        self.building = Layer()
        self.sq1 =Rectangle(600, 500, Point(300, -275))
        self.sq1.setFillColor('lightgray')
        self.building.add(self.sq1)
        
        self.window1 = Rectangle(450,100, Point(300 ,-80))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1)
        
        self.window1 = Rectangle(450,100, Point(300 ,-210))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1)
        
        self.window1 = Rectangle(450,100, Point(300 ,-340))
        self.window1.setFillColor('skyblue')
        self.window1.setDepth(-20)
        self.building.add(self.window1)
        
        self.sign = Rectangle(450, 80, Point(300, -450))
        self.sign.setFillColor('green')
        self.sign.setDepth(-20)
        self.building.add(self.sign)
        
        self.text = Text('NH하나로마트', 80, Point(300, -450))
        self.text.setFontColor('white')
        self.text.setFontSize(60)
        self.text.setDepth(-40)

        self.building.add(self.text)
        
        self.building.moveTo(70, 560)
        self.building.setDepth(80)
        canvas.add(self.building)


class Station:
    def __init__(self) :
        self.station = Layer()
        
        self.station1 = Rectangle(24, 240, Point(12, -120) )
        self.station1.setFillColor('white')
        self.station1.setDepth(60)
        self.station.add(self.station1)

        self.station2 = Rectangle(240, 40, Point(120, -228))
        self.station2.setFillColor('white')
        self.station2.setDepth(60)
        self.station.add(self.station2)
    
        self.station3 = Rectangle(24, 240, Point(226, -120) )
        self.station3.setFillColor('white')
        self.station3.setDepth(70)
        self.station.add(self.station3)
      
        self.sign = Rectangle(50, 240, Point(360, -120) )
        self.sign.setFillColor('white')
        self.sign.setDepth(30)
        self.station.add(self.sign)
        
        self.sign2 = Circle(50, Point(360, -240))
        self.sign2.setFillColor('blue')
        self.sign2.setDepth(30)
        self.station.add(self.sign2)
        
        self.minibus = Layer()
        self.busbody = Rectangle(60,40, Point(0, -15))
        self.busbody.setFillColor('white')
        self.tire = Circle(10, Point(-15,10))
        self.tire.setFillColor('black')
        self.tire2 = Circle(10, Point(15, 10))
        self.tire2.setFillColor('black')
        self.text = Text('BUS', 20)
        self.text.moveTo(0, -15)
        self.text.setDepth(-20)
        
        self.minibus.add(self.text)
        self.minibus.add(self.busbody)
        self.minibus.add(self.tire)
        self.minibus.add(self.tire2)
        
        self.minibus.moveTo(360, -220)
        self.minibus.setDepth(-20)
        self.station.add(self.minibus)
        
        self.station.moveTo(535, 590)
        
        canvas.add(self.station)


class Sun2 :
    def __init__(self) :
        self.sun = Circle(175, Point(35, 10))
        self.sun.setFillColor("red")
        self.sun.setBorderColor("red")
        self.sun.setDepth(10)
        canvas.add(self.sun)

class Ground :
    def __init__(self) :
        self.ground = Rectangle(1000, 350, Point(500, 700))
        self.ground.setFillColor("light green")
        self.ground.setBorderColor("black")
        self.ground.setDepth(60)
        canvas.add(self.ground)


class Car:
    def __init__(self) :
        self.car = Layer()
        
        self.carbody = Rectangle(250, 80, Point(100, -30))
        self.carbody.setFillColor('black')
        self.car.add(self.carbody)
        
        self.carhead = Polygon(Point(30,-70), Point(180, -70), Point(140, -115), Point(60, -115))
        self.carhead.setFillColor('black')
        self.carhead.setDepth(50)
        self.car.add(self.carhead)
        
        self.tire1 = Circle(20, Point(40, 10))
        self.tire2 = Circle(20, Point(160,10))
        self.tire1.setFillColor('gray')
        self.tire2.setFillColor('gray')
        self.car.add(self.tire1)
        self.car.add(self.tire2)
        
        self.window = Polygon(Point(45, -75), Point(160,-75), Point(140, -105), Point(60, -105)) 
        self.window.setFillColor('skyblue')
        self.car.add(self.window)
        
        self.hand = Circle(7, Point(120, -25) )
        self.hand.setFillColor('white')
        self.hand.setDepth(-10)
        self.car.add(self.hand)
        
        self.light = Rectangle(20, 40, Point(190, -25))
        self.light.setFillColor('yellow')
        self.light.setDepth(-10)
        self.car.add(self.light)
        
        self.car.moveTo(-250, 560)
        self.car.setDepth(10)
        canvas.add(self.car)
    def moving(self, x) :
        self.car.move(x, 0)

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

   # 팔의 기준축을 어떻게 설정하지?? -- adjustReference를 한번 이용해보자!
    def animating(self) :
        self.mans.arms2.arms1.adjustReference(0, -12)
        self.mans.arms2.arms2.adjustReference(0, -12)
        self.mans.hands2.hands1.adjustReference(0, -30)
        self.mans.hands2.hands2.adjustReference(0, -30)
        self.mans.legs.leg1.adjustReference(1, -12)
        self.mans.legs.leg2.adjustReference(1, -12)
        #self.mans.arms2.arms2.adjustReference(-7, 7)

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
            self.bus.moving(80)
        
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
        
        time.sleep(0.3)
        text3 = Text("What should I do?", 20)
        text3.moveTo(300, 380)
        canvas.add(text3)
        for i in range(100) :
            time.sleep(0.01)
            self.bird.moving2(5)
        time.sleep(1)
        for i in range(6) :
            time.sleep(0.3)
            self.car.moving(70)

        time.sleep(1)
        canvas.remove(text3)
        canvas.remove(change_eye1)
        canvas.remove(change_eye2)
        canvas.remove(self.mans.guy2)
        #canvas.remove(self.car)
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

def main():
    # Scene 1
    #canvas.setBackgroundColor("light green")
    #scene1 = Scene1()
    #animate_man(scene1)
    # Scene 2
    canvas.setBackgroundColor("light blue")
    scene2 = Scene2()
    animate_people_bus(scene2)
    # Scene 3
    #canvas.setBackgroundColor("light blue")
    #scene3 = Scene3()
    #animate_Scene3(scene3)
    # Scene 4
    #canvas.setBackgroundColor("darkgoldenrod")
    #scene4 = Scene4()
    #animate_Scene4(scene4)

main()
