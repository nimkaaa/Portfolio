import random

attempts = 6
number = random.randint(1, 100)

while attempts > 0:
   guess = int(input("Guess a number between 1 and 100: "))
   attempts -= 1
   if guess > number and attempts > 0:
      print("Too high!")
      print(f"You have {attempts} more attempts, try one more time\n\n")
   elif guess < number and attempts > 0:
      print("Too low")
      print(f"You have {attempts} more attempts, try one more time\n\n")
   elif guess != number and attempts == 0:
      print("Nope! Game over!")
      print(f"The number was: {number}")
   else:
      print("Congratulations! That's right!\n")