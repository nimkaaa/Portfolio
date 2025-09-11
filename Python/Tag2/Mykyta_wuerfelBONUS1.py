import random

def wuerfel():
   cube = random.randint(1, 6)
   print(f"Dropped: {cube}")

wuerfel()