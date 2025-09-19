class Character:
   def __init__(self, name, health, max_health, armor, luck):
      self.name = name
      self.health = health
      self.max_health = max_health
      self.armor = armor
      self.luck = luck

class DarkKnight:
   def __init__(self):
      self.name = "DARK KNIGHT"
      self.health = 30
      self.armor = 15

class Goblin:
   def __init__(self):
      self.name = "GOBLIN"
      self.health = 8
      self.armor = 5

class Orc:
   def __init__(self):
      self.name = "ORC"
      self.health = 15
      self.armor = 10
