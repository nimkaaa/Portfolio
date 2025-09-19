import random
import classes
import time

def creatingCharacter():
   name = input("What's your name: ").upper()
   health = random.randint(10, 30) # Throw 2 dices = damage
   max_health = health
   armor = random.randint(6, 12) # After throwing 2 dices, if the number on the dices > enemy armor = hit
   luck = random.randint(1, 10) # After throwing 2 dices, if luck > numbers on the dices = lucky

   player = classes.Character(name, health, max_health, armor, luck)
   return player

def showStats(character):
   print(f'''=========================
{character.name}
HP: {character.health}
Armor: {character.armor}
Luck: {character.luck}
=========================''')

def throwDice():
   dice1 = random.randint(1, 6)
   dice2 = random.randint(1, 6)
   return dice1 + dice2

def battle(player, minion):
   global classes
   while player.health > 0 and minion.health > 0:
      input("Press Enter to attack...\n")
      attack_roll = throwDice()
      print(f"You rolled {attack_roll}!")

      if attack_roll > minion.armor:
         damage = throwDice()
         minion.health -= damage
         print(f"You hit the {minion.name} for {damage} damage!")
         if minion.health > 0:
            print(f"{minion.name}'s HP is now {minion.health}.\n")
      else:
         print("Your attack missed!\n")

      input("(Enter to continue)\n")

      if minion.health <= 0:
         print(f"\nYou have defeated the {minion.name}!")
         break

      print(f"{minion.name} attacks you!")
      attack_roll = throwDice()
      print(f"{minion.name} rolled {attack_roll}!")

      if attack_roll > player.armor:
         damage = throwDice()
         player.health -= damage
         print(f"{minion.name} hits you for {damage} damage! Your HP is now {player.health}.\n")
      else:
         print(f"{minion.name}'s attack missed!\n")

      time.sleep(2)

      if player.health <= 0:
         print(f"\nYou have been defeated by the {minion.name}...")
         break
   
   print("\n")

def isAlive(player):
   if player.health <= 0:
      print("Game Over", end="")
      exit()