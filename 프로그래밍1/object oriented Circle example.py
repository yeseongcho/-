class Circle :
    def __init__(self, rad, p) :
        self.rad = rad
        self.area = self.comp_area(p)
        self.cir = self.comp_cir(p)
    def __str__(self) :
        return "(%6.2f %6.2f %6.2f)" % (self.rad, self.area, self.cir)
    def comp_area(self, pi) :
        return pi*self.rad**2
    def comp_cir(self, pi) :
        return 2*pi*self.rad
    def display(self) :
        print(self)

def main() :
    PI = 3.14
    try :  
        r = input("Enter a radius")
        r = float(r)
        circle = Circle(r, PI)
        circle.display()
        # 무엇을 의미하는지 확인할 수 있겠나
        print(circle.rad)
    except ValueError :
        print("Please enter a number")
        main()
        

main()
