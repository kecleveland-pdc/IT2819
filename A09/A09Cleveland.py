class Shape:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Shape):
    def findArea(self):
        return print("The area of the triangle is " + str((self.sides[0] + self.sides[1] + self.sides[2]) / 2))

t = Triangle (3)
t.inputSides()
t.dispSides()
t.findArea()
