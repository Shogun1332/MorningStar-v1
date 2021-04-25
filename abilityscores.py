#import main

class AbilityScores:
    #abilityScoresDict = {'Strength': 8, 'Dexterity': 8, 'Constitution': 8, 'Wisdom': 8, 'Intelligence': 8, 'Charisma': 8}
    abPoints = 27
    pointsCost = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9} 
    
    def __init__(self, race):
        self.race = race
        self.abilityScoresDict = {'Strength': 8, 'Dexterity': 8, 'Constitution': 8, 'Wisdom': 8, 'Intelligence': 8, 'Charisma': 8}
        if self.race == 'Human':
            print("Temp")
            #self.abilityScoresDict.values = {(self.abilityScoresDict.values+1) for self.abilityScoresDict.values in self.abilityScoresDict}
        elif self.race == 'Elf':
            self.abilityScoresDict['Dexterity'] = self.abilityScoresDict['Dexterity'] + 1
            self.abilityScoresDict['Intelligence'] = self.abilityScoresDict['Intelligence'] + 2
        elif self.race == 'Dwarf':
            self.abilityScoresDict['Strength'] = self.abilityScoresDict['Strength'] + 1
            self.abilityScoresDict['Constitution'] = self.abilityScoresDict['Constitution'] + 2
        elif self.race == 'Orc':
            self.abilityScoresDict['Constitution'] = self.abilityScoresDict['Constitution'] + 1
            self.abilityScoresDict['Strength'] = self.abilityScoresDict['Strength'] + 2
        elif self.race == 'Dragonborn':
            self.abilityScoresDict['Wisdom'] = self.abilityScoresDict['Wisdom'] + 1
            self.abilityScoresDict['Charisma'] = self.abilityScoresDict['Charisma'] + 2 

    def printAbilityScores(self):
        print("________________________")
        print("| Ability Scores       |")
        print("|----------------------|")
        print("| Strength: " + str(self.abilityScoresDict['Strength']) + "          |")
        print("|----------------------|")
        print("| Dexterity: " + str(self.abilityScoresDict['Dexterity']) + "         |")
        print("|----------------------|")
        print("| Constitution: " + str(self.abilityScoresDict['Constitution']) + "      |")
        print("|----------------------|")
        print("| Wisdom: " + str(self.abilityScoresDict['Wisdom']) + "            |")
        print("|----------------------|")
        print("| Intelligence: " + str(self.abilityScoresDict['Intelligence']) + "      |")
        print("|----------------------|")
        print("| Charisma: " + str(self.abilityScoresDict['Charisma']) + "          |")
        print("|______________________|")

    def printPointsCost(self):
        print("________________________")
        print("| Score |     Cost     |")
        print("|-------|--------------|")
        print("|   8   |       " + str(self.pointsCost[8]) + "      |")
        print("|-------|--------------|")
        print("|   9   |       " + str(self.pointsCost[9]) + "      |")
        print("|-------|--------------|")
        print("|  10   |       " + str(self.pointsCost[10]) + "      |")
        print("|-------|--------------|")
        print("|  11   |       " + str(self.pointsCost[11]) + "      |")
        print("|-------|--------------|")
        print("|  12   |       " + str(self.pointsCost[12]) + "      |")
        print("|-------|--------------|")
        print("|  13   |       " + str(self.pointsCost[13]) + "      |")
        print("|-------|--------------|")
        print("|  14   |       " + str(self.pointsCost[14]) + "      |")
        print("|-------|--------------|")
        print("|  15   |       " + str(self.pointsCost[15]) + "      |")
        print("|_______|______________|")

    def increaseScore(self, abilityScore):
        self.abilityScore = abilityScore
        