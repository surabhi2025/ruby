class Shape:

    def area(self):
        print("Area method not implemented")



class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

rec = Rectangle(5, 3)
print("The area of the rectangle is: ", rec.area)
    
     

    