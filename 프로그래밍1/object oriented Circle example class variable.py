
class Circle :
    PI = 3.14
    def __init__(self, rad) :
        self.rad = rad
        self.area = self.comp_area()
        self.cir = self.comp_cir()
    def __str__(self) :
        return "(%6.2f %6.2f %6.2f)" % (self.rad, self.area, self.cir)
    def comp_area(self) :
        return self.PI*self.rad**2
        #return Circle.PI*self.rad**2
    def comp_cir(self) :
        return 2*self.PI*self.rad
        #return 2*Circle.PI*self.rad
    def display(self) :
        print(self)

def main() :
    try :
        r = input("Enter a radius")
        r = float(r)
        circle = Circle(r)
        circle.display()
    except ValueError :
        print("Please enter a number")  
        main()

main()

# No change main function -- 객체지향 프로그램의 가장 큰 장점이다!! by 
"""
class Circle :
    PI = 3.14
    def __init__(self, rad) :
        self.rad = rad
        #self.area = self.comp_area()
        #self.cir = self.comp_cir()
    def __str__(self) :
        return "(%6.2f %6.2f %6.2f)" % (self.rad, self.comp_area(), self.comp_cir())
    def comp_area(self) :
        return self.PI*self.rad**2
        #return Circle.PI*self.rad**2
    def comp_cir(self) :
        return 2*self.PI*self.rad
        #return 2*Circle.PI*self.rad
    def display(self) :
        print(self)

def main() :
    try :
        r = input("Enter a radius")
        r = float(r)
        circle = Circle(r)
        circle.display()
    except ValueError :
        print("Please enter a number")
        main()

main()
"""
