from cs1graphics import *
canvas = Canvas(1000, 1000)
canvas.setBackgroundColor("light blue")
canvas.setTitle("P1 is good")
sq = Square(100)
canvas.add(sq)
sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)


tree = Polygon(Point(50, 80), Point(30,140), Point(70,140))
tree.setFillColor('darkGreen')
canvas.add(tree)
tree.addPoint(Point(50,120), 2)

sq.rotate(45)
tree.scale(2)


canvas.remove(tree)

sq.flip(20)

