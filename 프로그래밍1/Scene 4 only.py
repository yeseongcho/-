from cs1graphics import *
import time

canvas = Canvas(1000, 700)

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

class Ground2 :
    def __init__(self) :
        self.ground2 = Polygon(Point(0,500), Point(300, 280), Point(300, 380), Point(0, 600))
        self.ground2.setFillColor("light green")
        self.ground2.setBorderColor("black")
        self.ground2.setDepth(30)
        canvas.add(self.ground2)
class Handle:
    def __init__(self):
        self.handle = Ellipse(110, 140, Point(700, 680))
        self.handle.setBorderWidth(30)
        self.handle.setBorderColor("brown")
        self.handle.setDepth(7)
        canvas.add(self.handle)       

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
        self.final_guy.add(self.final_arm1.arm)
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
        canvas.add(self.tree)

class Tree2s :
    def __init__(self) :
        self.tree = Polygon(Point(-470, -80), Point(-330, -80), Point(-400, -130))
        self.tree.setFillColor('brown')
        self.tree.setBorderColor('brown')
        self.tree.setDepth(26)
        canvas.add(self.tree)

class Leafs :
    def __init__(self) :
        self.leaf = Circle(40, Point(-400, -200))
        self.leaf.setFillColor('dark green')
        self.leaf.setDepth(23)
        canvas.add(self.leaf)

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

def main():
    # Scene 1
    #canvas.setBackgroundColor("light green")
    #scene1 = Scene1()
    #animate_man(scene1)
    # Scene 2
    #canvas.setBackgroundColor("light blue")
    #scene2 = Scene2()
    #animate_people_bus(scene2)
    # Scene 3
    #canvas.setBackgroundColor("light blue")
    #scene3 = Scene3()
    #animate_Scene3(scene3)
    # Scene 4
    canvas.setBackgroundColor("darkgoldenrod")
    scene4 = Scene4()
    animate_Scene4(scene4)

main()
