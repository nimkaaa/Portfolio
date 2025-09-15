from turtle import *

leonardo = Turtle()

bgcolor("black")
leonardo.shape('turtle')
leonardo.color('green')
leonardo.pensize(3)
leonardo.speed(100)

for i in range(5):
    for j in range(4):
        for k in range(4):
            leonardo.forward(100)
            leonardo.left(90)
        leonardo.left(90)
    leonardo.left(360/5)

done()