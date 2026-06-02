
import turtle

def draw_star(board):
    turtle.Screen().bgcolor("light grey")
    board.forward(100)

    board.left(120)
    board.forward(100)

    board.left(120)
    board.forward(100)

    board.penup()
    board.right(150)
    board.forward(50)

    board.pendown()
    board.right(90)
    board.forward(100)

    board.right(120)
    board.forward(100)

    board.right(120)
    board.forward(100)
board = turtle.Turtle()
turtle.done()
star = draw_star(board)
print(star)
turtle.Screen().bgcolor("light grey")