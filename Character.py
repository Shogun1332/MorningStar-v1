import random
from enum import Enum

class Character:
    name
    race
    job
    abilityScores
    level
    abilities
    currentHP
    maxHP

    def __init__(self, name, race, job, abilityScores, level, abilities):
        self.name = name
        self.race = race
        self.job = job
        self.abilityScores = abilityScores
        self.level = level
        self.abilities = abilities

    def printCharacter():
        print('--------------------------------------------------------------------------')
        print('| Name: ' + self.name)
        print('--------------------------------------------------------------------------')
        print('| Race: ' + self.race)
        print('--------------------------------------------------------------------------')
        print('| Class: ' + self.job + ' | Level: ' + self.level)
        print('--------------------------------------------------------------------------')
        print('| Current Health: ' + self.currentHP + ' | Max Health: ' + self.maxHP)
        print('--------------------------------------------------------------------------')
        print('| Ability Scores')
        print('| Strength: ' + str(self.abilityScores[0]))
        print('| Dexterity: ' + str(self.abilityScores[1]))
        print('| Constitution: ' + str(self.abilityScores[2]))
        print('| Wisdom: ' + str(self.abilityScores[3]))
        print('| Intelligence: ' + str(self.abilityScores[4]))
        print('| Charisma: ' + str(self.abilityScores[5]))
        print('--------------------------------------------------------------------------')
        print('')
        print('')
        print('')
        input('Press Enter to return to your Adventure...')

    def levelUp():
        self.level = self.level + 1

    class Inventory:
        itemName

        #def printInventory():

        #def dropItem(itemName):

        #def addItem(itemName):

        #def useItem(itemName):

class Race(Enum):
    Human = 1
    Elf = 2
    Dwarf = 3
    Orc = 4
    Dragonborn = 5
    Random = 6

class Job(Enum):
    Fighter = 1
    Wizard = 2
    Cleric = 3
    Thief = 4
    Archer = 5
    Random = 6

