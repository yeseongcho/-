from copy import*
class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Rectangle :
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.corner = Point(0, 0)
    def __str__(self) :
        return "(%5.2f, %5.2f)" % (self.width, self.height)

def main() :
    box = Rectangle(100.0, 200.0)
    nbox = Rectangle(100.0, 200.0)
    #print("1111")
    print(box, nbox)
    print(box is nbox)
    #print("1111")
    print(box == nbox)
    #print("1111")
    
   
main()
