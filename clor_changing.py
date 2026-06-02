import turtle

def draw_colorful_squares(size):
    if size>100:
        turtle.Screen().bgcolor("red")
    elif size<100:
        turtle.Screen().bgcolor("blue")

    line = turtle.Turtle()

    for i in range(0,5):
        line.forward(size)
        line.right(90)
    return size
        

size = int(input("Enter the size of the square side: "))

square = draw_colorful_squares(size)
print(square)

turtle.done()