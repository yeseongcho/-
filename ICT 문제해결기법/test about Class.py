class Point1D :
    def __init__(self, x) :
        self.x = x
    def print_x(self) :
        print('x : ', self.x)

class Point2D(Point1D) :
    def __init__(self, x, y) :
        Point1D.__init__(self, x)
        self.y = y
    def print_y(self) :
        print('y: ', self.y)

p = Point2D(10, 20)
print(p.x)
print(p.y)
