import random
from turtle import *

# Screen Configutation
screen = Screen()
screen.setup(width=800, height=1000)
screen.title("CATCH TURTLE v0.0.1")
bgpic("bg.gif")

# Turtle Configutation
leo = Turtle()
leo.penup()
leo.shape('turtle')
leo.color('green')
leo.speed(10)
leo.shapesize(1.5)

# ============GAME==============

score = 0
attempts = 1
MAX_ATTEMPTS = 10

def isHitted(x_user, y_user, x_turtle, y_turtle):
   return abs(x_user - x_turtle) < 20 and abs(y_user - y_turtle) < 20


def moveTurtle(x_user, y_user):
   global score, attempts
   x_turtle, y_turtle = leo.position()
   if isHitted(x_user, y_user, x_turtle, y_turtle):
      score += 1
      print(f"Attempt#{attempts}\nScore: {score}\n\n")
   elif not isHitted(x_user, y_user, x_turtle, y_turtle) and score == 0:
      print(f"Attempt#{attempts}\nScore: {score}\n\n")
   else:
      score -= 1
      print(f"Attempt#{attempts}\nScore: {score}\n\n")
   
   attempts += 1
   if attempts > MAX_ATTEMPTS:
      print("Game Over!")
      onscreenclick(None)
      bye()
      return

   x_turtle = random.randint(-350, 300)
   y_turtle = random.randint(-350, 300)
   leo.goto(x_turtle, y_turtle)
           
onscreenclick(moveTurtle)
mainloop()