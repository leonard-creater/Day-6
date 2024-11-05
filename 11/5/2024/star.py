import turtle

turtle.Screen().bgcolor("cyan")
sc=turtle.Screen()
sc.setup(500.500)

board=turtle.Turtle()
board.forward(200)
board.left(120)
board.forward(200)
board.left(120)


board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.forward(200)
board.right(120)
board.forward(200)
board.right(120)

turtle.done()