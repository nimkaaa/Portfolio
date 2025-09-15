from turtle import *

leonardo = Turtle()

bgcolor("black")
leonardo.shape('turtle')
leonardo.color('green')
leonardo.pensize(2)
leonardo.speed(10)

# Letter A
leonardo.teleport(-300, 0)

leonardo.left(75)
leonardo.forward(150)
line_start_x, line_start_y = leonardo.position()
leonardo.forward(150)

leonardo.right(150)
leonardo.forward(150)
line_end_x, line_end_y = leonardo.position()
leonardo.forward(150)

leonardo.teleport(line_start_x, line_start_y)
leonardo.left(75)
leonardo.goto(line_end_x, line_end_y)

#Letter D
leonardo.teleport(-100, 0)

leonardo.left(90)
leonardo.forward(300)
leonardo.right(90)

for i in range(18):
    leonardo.right(10)
    if i < 17:
        leonardo.forward(26)

# Letter A
leonardo.teleport(50, 0)
leonardo.left(180)

leonardo.left(75)
leonardo.forward(150)
line_start_x, line_start_y = leonardo.position()
leonardo.forward(150)

leonardo.right(150)
leonardo.forward(150)
line_end_x, line_end_y = leonardo.position()
leonardo.forward(150)

leonardo.teleport(line_start_x, line_start_y)
leonardo.left(75)
leonardo.goto(line_end_x, line_end_y)

done()