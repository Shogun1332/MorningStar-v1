#import Character
import random

print("                         _             __ _             ")
print("  /\/\   ___  _ __ _ __ (_)_ __   __ _/ _\ |_ __ _ _ __ ")
print(" /    \ / _ \| '__| '_ \| | '_ \ / _` \ \| __/ _` | '__|")
print("/ /\/\ \ (_) | |  | | | | | | | | (_| |\ \ || (_| | |   ")
print("\/    \/\___/|_|  |_| |_|_|_| |_|\__, \__/\__\__,_|_|   ")
print("                                 |___/                  ")

input('                 Press Enter to Begin                   ')
print("\n" * 50)

print("Unknown Man: 'Welcome to Ordania! A land of opportunity for enterprising adventurers such as yourself.'")
print("Unknown Man: 'I'm Ulrich, no one special really, but I try to help out the new kids around here.'")
print("Ulrich: 'Come with me to the Adventurer's Guild and we'll get you registered!'")
print("\n")
input("              Press Enter to Proceed to the Adventurer's Guild                   ")

print("\n" * 50)

print("______________________________________________________")
print("|    _      _             _                    _     |")
print("|   /_\  __| |_ _____ _ _| |_ _  _ _ _ ___ _ _( )___ |")
print("|  / _ \/ _` \ V / -_) ' \  _| || | '_/ -_) '_|/(_-< |")
print("| /_/_\_\__,_|\_/\___|_||_\__|\_,_|_| \___|_|   /__/ |")
print("|  / __|_  _(_) |__| |                               |")
print("| | (_ | || | | / _` |                               |")
print("|  \___|\_,_|_|_\__,_|                               |")
print("|                                                    |")
print("|____________________________________________________|")
print("\n" * 2)
print("Guild Attendant: 'Ulrich! Another new adventurer in town I take it?'")
print("Ulrich: 'That's right, this here is... Come to think of it, I never got your name friend?")
print("\n")
name = input("Enter your name: ")
print("Ulrich: '" + name.capitalize() + "? That's a good name. It really suits you!")
print("Ulrich: 'This is " + name.capitalize() + "! They'd like to get registered with the guild.'")
print("Guild Attendant: 'That's great news! We're always in need of new adventurers in Ordania.'")
print("Guild Attendant: 'There's just a few questions we need to have you answer to get you on the books...'")
race = ''
job = ''
while True:
    while True:
        if race == '':
            race = input('Choose your race: Human, Elf, Dwarf, Orc, Dragonborn, or Random: ')
            print('')
        if race.lower() == 'human':
            print('You have chosen Human. Humans are skilled at many things, but masters of none given their short lifespans.')
            break
        elif race.lower() == 'elf':
            print('You have chosen Elf. The elves are skilled in Magicks both arcane and natural. They live for thousands of years and often master many skills in that lifetime.')
            break
        elif race.lower() == 'dwarf':
            print('You have chosen Dwarf. Dwarves are exceptionally skilled craftsmen and fierce warriors that guard their mountain homes from all manner of fearsome foes.')
            break
        elif race.lower() == 'orc':
            print('You have chosen Orc. The Orcish people are nomadic and hardened by life on the plains of Ordania, their various clans are well known for producing strong warriors and some of the finest horses in the land.')
            break
        elif race.lower() == 'dragonborn':
            print('You have chosen Dragonborn. The Dragonborn are mysterious beings said to be descendant from dragons. A strong sense of community often unites their clans into tightknit groups that form villages or small towns.')
            break
        elif race.lower() == 'random':
            race = random.choice(['Human', 'Elf', 'Dwarf', 'Orc', 'Dragonborn'])
            continue
        else:
            print(race + '? Never heard of that before... Where did you say you were from again?')
            print('')

    race = race.capitalize()

    print("\n")

    if race == 'Elf' or race == 'Orc':
        print("Guild Attendant: 'Okay, so you're an " + race + ", but what do you do? What's your job as an adventurer?'")
    else:
        print("Guild Attendant: 'Okay, so you're a " + race + ", but what do you do? What's your job as an adventurer?'")

    print("\n")

    while True:
        if job == '':
            job = input('Choose your profession: Fighter, Wizard, Thief, Cleric, Archer, or Random: ')
            print('')
        if job.lower() == 'fighter':
            print("Ulrich: 'Oh ho! A fighter eh? I bet you're really strong! Can we arm wrestle later?'")
            break
        elif job.lower() == 'wizard':
            print("Ulrich: 'Hmmm... A wizard huh? Can you turn that guy into a sheep? No? I bet you're too busy pondering the mysteries of the Arcane, aren't you? Oh well, maybe later...'")
            break
        elif job.lower() == 'thief':
            print("Guild Attendant: 'Pretty brazen to just admit to anyone that you're a thief don't you think? I'm gonna guess you're plenty daring, but not too wise!'")
            break
        elif job.lower() == 'cleric':
            print("Ulrich: 'A Cleric? Well, I'll be, this is a stroke of luck! My daughter wanted to get married tomorrow, could you lead the ceremony for us?'")
            break
        elif job.lower() == 'archer':
            print("Guild Attendant: 'An archer? I hear there's good money to be made in trick shot contests, why choose to be an adventurer?'")
            break
        elif job.lower() == 'random':
            job = random.choice(['fighter', 'wizard', 'thief', 'priest', 'archer'])
            continue
        else:
            print("Well that's a new one! What exactly does a " + job + " do anyway?")
            print("\n")

    job = job.capitalize()

    print('') #Line Break
    break
input('')