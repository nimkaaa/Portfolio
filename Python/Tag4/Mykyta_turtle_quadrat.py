from turtle import *

leonardo = Turtle()

bgcolor("black")
leonardo.shape('turtle')
leonardo.color('green')
leonardo.pensize(3)
leonardo.speed(10)

def schildkroete(turtle):
    turtle.teleport(-200, -200)
    for i in range(4):
        turtle.forward(400)
        turtle.left(90)
    
    turtle.teleport(-150, -150)
    for i in range(4):
        turtle.forward(300)
        turtle.left(90)
    
    turtle.teleport(0, 0)
    turtle.right(90)
    turtle.shapesize(5, 5, 3)

schildkroete(leonardo)

done()