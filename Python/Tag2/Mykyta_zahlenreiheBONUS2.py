import random

prev = 1
befor_prev = 0
result = 0

print(befor_prev, prev, sep=',', end=',')

while result < 12586269025:

   result = prev + befor_prev
   befor_prev = prev
   prev = result

   if result == 12586269025:
      print(result, end='')
   else:
      print(result, end=',')
