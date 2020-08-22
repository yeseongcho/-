from cs1graphics import *



class Question:
    def __init__(self):
        self.layer = Layer()
        self.hook = Hook()
        self.circle = Circle()
        self.layer.add(self.hook.shape)
        self.layer.add(self.circle.shape)

class Hook:
    def __init__(self):
        self.circle1 = H_circle1()
        self.circle2 = H_circle2()
        self.rectangle1 = H_rectangle1()
        self.rectangle2 = H_rectangle2()
        self.layer = Layer()
        self.layer.add(self.circle1.shape)
        self.layer.add(self.circle2.shape)
        self.layer.add(self.rectangle1.shape)
        self.layer.add(self.rectangle2.shape)



class H_circle1:
    def __init__(self):
        self.shape = Ellipse(100,100)
        self.shape.setFillColor("white")
        self.shape.move(300,275)

class H_circle2:
    def __init__(self):
        self.shape = Ellipse(50,50)
        self.shape.setFillColor("orange")
        self.shape.move(300,275)

class H_rectangle1:
    def __init__(self):
        self.shape = Rectangle(30,60)
        self.shape.setFillColor("orange")
        self.shape.move(275,275)

class H_rectangle2:
    def __init__(self):
        self.shape = Rectangle(20,80)
        self.shape.setFillColor("white")
        self.shape.move(300,325)


class Circle:
    def __init__(self):
        self.shape = Ellipse(70,70)
        self.shape.setFillColor("white")
        self.shape.setDepth(20)
        self.shape.move(380,680)

canvas = Canvas(1000, 550)
canvas.setBackgroundColor("orange")
question = Question()
canvas.add(question.layer)
