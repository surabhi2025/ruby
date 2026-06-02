import turtle
import random

def draw_star():
    turtle.fillcolor(random.choice(["light blue", "blue", "yellow", "light yellow", "purple",]))
    turtle.begin_fill()
    
    for i in range(5):
        turtle.forward(50)   
        turtle.right(144)
    
    turtle.end_fill()



for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    draw_star()   

turtle.done()
