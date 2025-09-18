import random
import time

#! ==============CLASSES==============

class Character:
   def __init__(self, name, health, armor, luck):
      self.name = name
      self.health = health
      self.armor = armor
      self.luck = luck

class DarkKnight:
   def __init__(self, health, armor):
      self.health = 30
      self.armor = 15

class Goblin:
   def __init__(self, health, armor):
      self.health = 8
      self.armor = 5

class Orc:
   def __init__(self, health, armor):
      self.health = 15
      self.armor = 10

#! ==============CLASSES==============
#* ==============FUCTIONS=============

def creatingCharacter():
   name = input("What's your name: ").upper()
   health = random.randint(10, 30) # бросок 2х кубиков - урон
   armor = random.randint(6, 12) # после броска 2х кубиков, если число на кубиках > брони врага - попал
   luck = random.randint(1, 10) # после броска 2х кубиков, если удача > числа на кубиках - повезло

   player = Character(name, health, armor, luck)
   return player

#* ==============FUCTIONS=============
#? ===============GAME================

print("Welcome to these lands, brave hero!")

time.sleep(1.5)

player = creatingCharacter()

time.sleep(1)

print("*loading your character*")

for i in range(2):
   time.sleep(1)
   print("...")

time.sleep(1)

print(f'''\nName: {player.name}
HP: {player.health}
Armor: {player.armor}
Luck: {player.luck}\n''')

time.sleep(1)

print("The great dark wizard stole the princess of your kingdom.\nAnd you, as a brave hero, decided to be the one to save her!\n\n")

time.sleep(2)

print("But beware, the dark wizard has many minions to stop you on your way!\nGood luck!\n")

time.sleep(2)

print("You find yourself in a dark forest, with two paths before you.\n")

time.sleep(1)

print("Do you choose the left path or the right path?")
choice = input("Type 'left' or 'right': ").lower()

if choice == 'left':
   print("\nYou walk down the left path and encounter a goblin!")
   goblin = Goblin(8, 5)
   time.sleep(1)
   print(f"Goblin stats - HP: {goblin.health}, Armor: {goblin.armor}")
   time.sleep(1)
   print("Prepare for battle!")
   # Battle logic would go here
#? ===============GAME================