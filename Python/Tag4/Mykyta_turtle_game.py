from turtle import *

leonardo = Turtle()

bgcolor("black")
leonardo.shape('turtle')
leonardo.color('green')
leonardo.pensize(2)
leonardo.speed(1)

def change_color(x, y):
   leonardo.color('red')
   leonardo.goto(x, y)

onscreenclick(change_color)

done()