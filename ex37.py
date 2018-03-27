from sys import exit
from random import *
from sys import argv
script = argv

def introduction():
    print (script)
    print(f"Welcome to the {script} game!")

def entrance():
    print("You see doors to your left, right and in front, which do you choose?")
    choice = input("> ")

    if choice == "left":
        puzzle_room()
    elif choice == "front":
        genie_room()
    elif choice == "right":
        monster_room()
    else:
        dead("You stand there indecisively and starve to death.")


def dead(why):
    print(why, "Try again!")
    exit(0)

def win(why):
    print(why, "Good job!")
    exit(0)

def genie_room():
    print("There are 3 treasure boxes in front of you, which do you choose?")
    treasure = input("> ")

    if treasure == "1":
        print("You open the treasure box and find a burned skull..")
        print("A shriek pierces the room and a wisp of smoke flies into your nose.")
        print("You feel light headed and dizzy... then collapse")
        dead("You have been cursed!")
    elif treasure == "2":
        print("You open the treasure box and see a blinding flash of light.")
        print("The light fades and you realize you are at the entrance again..")
        entrance()
    elif treasure == "3":
        print("You open the treasure box and find a jewelled sword.")
        print("After you pick up the sword, the entire dungeon crumbles, but you wake up in your room.")
        win("With sword in hand, you rejoice!")
    else:
        print("So which you going to pick?")
        genie_room()

def puzzle_room():
    puzzle = randint(1,3)
    print("You see a giant board pop up with a puzzle to solve")
    print (puzzle)
    if puzzle == 1:
        puzzle1 = ((5+3)*2)**2
        print(puzzle1)
        answer = input("> ")
        if answer == "256":
            print("The board disappears and a door opens in the back of the room")
            genie_room()
        else:
            dead("The board turns red and flies out hitting you in the face.")
    elif puzzle == 2:
        puzzle2 = 0/(((3+5)**2)*3)
        print(puzzle2)
        answer = input("> ")
        if answer == "0":
            print("The board disappears and a door opens in the back of the room")
            genie_room()
        else:
            dead("The board turns red and flies out hitting you in the face.")
    elif puzzle == 3:
        puzzle3 = ((2*2)**2)**2
        print(puzzle3)
        answer = input("> ")
        if answer == "256":
            print("The board disappears and a door opens in the back of the room")
            genie_room()
        else:
            dead("The board turns red and flies out hitting you in the face.")

def monster_room():
    print("You see a giant Snorlax blocking the doorway. Which option do you pick?")
    print("Option 1: Squish behind the Snorlax")
    print("Option 2: Poke Snorlax")
    print("Option 3: Feed him candy.")
    option = input("> ")

    if option == "1":
        dead("You try to move behind the Snorlax, but it wakes up and squishes you to death.")
    elif option == "2":
        print("You poke Snorlax's belly. It shifts abit but nothing happens. Try again!")
        monster_room()
    elif option == "3":
        candy = ['chocolate','lollipop', 'cookie']
        print(f'Which candy will you give? {candy}')
        feed_candy = input('> ')
        if feed_candy=="lollipop":
            print("You give Snorlax a lollipop. It smiles and gives you a hug. You feel happy and move to the next door.")
            genie_room()
        else:
            print("Snorlax spits it out...")
            monster_room()
    else:
        dead("Snorlax's stomach growls and grabs you for lunch.")

introduction()
entrance()
