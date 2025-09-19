import time
import funktions
import classes

print("\nWelcome to these lands, brave hero!\n")

player = funktions.creatingCharacter()

print("\n*loading your character*")

time.sleep(3)

print(f'''\n=========================
{player.name}
HP: {player.health}/{player.max_health}
Armor: {player.armor}
Luck: {player.luck}
=========================\n''')

input("(Enter to continue)\n")

print("The great dark wizard stole the princess of your kingdom.\nAnd you, as a brave hero, decided to be the one to save her!\n(Enter to continue)\n")

input()

print("But beware, the dark wizard has many minions to stop you on your way!\nGood luck!\n(Enter to continue)\n")

input()

print("You find yourself in a dark forest, with two paths before you.\n(Enter to continue)\n")

input()

print("Do you choose the left path or the right path?")
choice = ''
while choice != 'left' and choice != 'right':
   choice = input("Type 'left' or 'right': ").strip().lower()

if choice == 'left':
   print("\nYou walk down the left path and encounter a goblin!")
   goblin = classes.Goblin()
   print("Prepare for battle!\n")
   time.sleep(2)
   print(f"Goblin stats - HP: {goblin.health}, Armor: {goblin.armor}\n")

   funktions.battle(player, goblin)

   funktions.isAlive(player)

   funktions.showStats(player)
else:
   print("\nYou walk down the right path. Not much time passes before you reach a fork again.\n")

   time.sleep(4)

   print("You need to choose the path again - a slightly overgrown path leaving to the left, or a wider path leading to the right and out of the forest.\n")

