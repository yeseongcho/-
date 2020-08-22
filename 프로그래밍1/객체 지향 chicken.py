# 주석달아
# Dot 파트... 새끼들 없애는 걸.. 단지 배경색을 위조했을 뿐...


from cs1graphics import *
canvas = Canvas(1000, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Journey of Chicken")

import time

def animate_chickens(scene) :
    animation = Animation(scene) # class
    animation.move_group()
    animation.move_chicken2()

def main() :
    scene = Scene() 
    animate_chickens(scene)
    canvas.wait()
    canvas.close()


class Scene :
    def __init__(self) :
        self.ground = Ground() 
        self.sun = Sun() 
        self.family = Family() 

    def get_anim_data(self) :
        return self.family.group.layer, self.family.chick2.layer, self.family.chick2.wing

class Ground :
    def __init__(self) :
        self.grass = Rectangle(1000, 100, Point(500, 950))
        self.grass.setFillColor("green")
        self.grass.setBorderColor("green")
        self.grass.setDepth(100)
        canvas.add(self.grass)


class Sun :
    def __init__(self) :
        self.suns = Circle()
        self.suns.setRadius(50)
        self.suns.moveTo(40, 40)
        self.suns.setFillColor("red")
        canvas.add(self.suns)

class Family :
    def __init__(self) :
        self.group = Group() 
        self.group.layer.move(600, 200)
        self.chick2 = Chicken() 
        self.chick2.layer.move(800, 200)
        canvas.add(self.group.layer)
        canvas.add(self.chick2.layer)

class Group :
    def __init__(self) :
        self.hen = Chicken(True)
        self.chick1 = Chicken() 
        self.chick1.layer.move(120, 0)
        self.layer = Layer() 
        self.layer.add(self.hen.layer)
        self.layer.add(self.chick1.layer)

class Chicken :
    def __init__(self, hen=False) :
        self.body = Body(hen) 
        self.wing = Wing(hen) 
        self.eye = Eye(hen) 
        self.beak = Beak(hen) 
        self.dots = Dots(hen)
        self.layer = Layer()
        self.layer.add(self.body.shape)
        self.layer.add(self.wing.shape)
        self.layer.add(self.eye.shape)
        self.layer.add(self.beak.shape)
        self.layer.add(self.dots.shape)

class Body :
    def __init__(self, hen) :
        if hen :
            self.shape = Ellipse(70, 80)
            self.shape.setFillColor("white")
        else :
            self.shape = Ellipse(40, 50)
            self.shape.setFillColor("yellow")
            self.shape.move(0, 10)
        self.shape.setBorderColor("yellow")
        self.shape.setDepth(20)

class Wing:
    def __init__(self, hen) :
        if hen :
            self.shape = Ellipse(60, 40)
            self.shape.setFillColor("white")
            self.shape.setBorderColor("yellow")
            self.shape.move(15,20)
        else :
            self.shape = Ellipse(30, 20)
            self.shape.setFillColor("yellow")
            self.shape.setBorderColor("orange")
            self.shape.move(10, 20)
            self.shape.adjustReference(-5, -5)
        self.shape.setDepth(19)

    def flap(self, angle) :
        self.shape.rotate(angle)

class Eye :
    def __init__(self, hen) :
        if hen :
            
            self.shape = Circle()
            self.shape.setRadius(3)
            self.shape.moveTo(-20, -20)
            self.shape.setFillColor("black")
            self.shape.setBorderColor("black")
            self.shape.setDepth(15) # 중복을 없애는 방법은?
        else :
            self.shape = Circle()
            self.shape.setRadius(3)
            self.shape.moveTo(-10, 0)
            self.shape.setFillColor("black")
            self.shape.setBorderColor("black")
            self.shape.setDepth(15)
        

class Beak :
    def __init__(self, hen) :
        if hen :
            
            self.shape = Polygon(Point(-50, 0), Point(-35, -10), Point(35, -10), Point(-20, 0))
            self.shape.setFillColor("red")
            self.shape.setBorderColor("yellow")
            self.shape.setDepth(30)
        else :
            self.shape = Polygon(Point(-30, 15), Point(-10, -5), Point(10, -5), Point(-10,15))
            self.shape.setFillColor("red")
            self.shape.setBorderColor("yellow") 
            self.shape.setDepth(30)
# 질문이 좀 필요할 거 같은데...
class Dots :
    def __init__(self, hen) :
        self.shape = Layer()
        if hen :
            
            self.dotss1 = Ellipse(5, 20)
            self.dotss2 = Ellipse(5, 20)
            self.dotss1.setFillColor("red")
            self.dotss2.setFillColor("red")
            self.dotss1.setBorderColor("red")
            self.dotss2.setBorderColor("red")
            self.dotss1.move(0, -40)
            self.dotss2.move(5, -40)
            self.dotss1.setDepth(30)
            self.dotss2.setDepth(30)
            self.shape.add(self.dotss1)
            self.shape.add(self.dotss2)
        """
        else :
            self.shape = Layer()
            self.dotss1 = Ellipse(5, 20)
            self.dotss2 = Ellipse(5, 20)
            self.dotss1.setFillColor("light blue")
            self.dotss2.setFillColor("light blue")
            self.dotss1.setBorderColor("light blue")
            self.dotss2.setBorderColor("light blue")
            self.dotss1.move(0, -40)
            self.dotss2.move(5, -40)
            self.dotss1.setDepth(120)
            self.dotss2.setDepth(120)
            self.shape.add(self.dotss1)
            self.shape.add(self.dotss2)
           """ 
            
class Animation :
    def __init__(self, scene) :
        group, chicken, wing = scene.get_anim_data()
        self.group = group
        self.chicken2 = chicken
        self.wing2 = wing

    def move_group(self) :
        
        for i in range(80) :
            time.sleep(0.06)
            self.group.move(-5, -2)
            self.group.move(-5, 2)
            if i == 30 :
                text1 = Text("OH!", 20)
                text1.move(800, 160)
                canvas.add(text1)
            elif i == 40 :
                canvas.remove(text1)
                text2 = Text("WHERE IS MY MOMMY GOING?", 30)
                text2.move(500, 100)
                canvas.add(text2)
            elif i == 50 :
                canvas.remove(text2)
    def move_chicken2(self) :
        text3 = Text("Wait for ME~", 25)
        text3.move(500, 100)
        canvas.add(text3)
        for j in range(10) :
            for i in range(5) :
                time.sleep(0.06)
                self.chicken2.move(-10, -20)
                self.wing2.flap(-10)
            for i in range(5) :
                self.chicken2.move(-10, 20)
                self.wing2.flap(10)
        canvas.remove(text3)

main()
