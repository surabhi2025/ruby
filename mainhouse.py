import turtle

turtle.Screen().bgcolor("pink")
turtle.color("red","green")
turtle.pencolor("red")
turtle.pensize()

t = turtle.Turtle()

for i in range(0,6):
    t.forward(100)
    t.left(120)

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
