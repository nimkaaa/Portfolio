import random

cube = 0
counter = 0
i = 0

while i < 30:
   cube = random.randint(1, 6)
   print(f"It dropped: {cube}")
   i += 1
   print(f"Total throws: {i}")
   print("\n")