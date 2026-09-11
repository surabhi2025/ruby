import math

class Circle:


    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    


r = float(input("Enter the radius: "))
c = Circle(r)


print("The area of the circle:", c.area)
print("The perimeter of the circle:", c.perimeter)

    

        

