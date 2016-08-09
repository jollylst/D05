#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(count=0):
    print("{} walks through the door to see a dimly lit hallway.".format(sys.argv[1]))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} take the stairs'.format(sys.argv[1]))
        if (count > 0):
            print("but {} is not happy about it".format(sys.argv[1]))
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == "go back":
        pass


def gold_room():
    print("This room is full of gold.  How much do you take, {}?".format(sys.argv[1]) )

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, {} wins!".format(sys.argv[1]))
        exit(0)
    else:
        dead("{} greedy goose!".format(sys.argv[1]))


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at {} then slaps your face off.".format(sys.argv[1]))
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(sys.argv[1]))
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} sees the great evil Cthulhu.".format(sys.argv[1]))
    print("He, it, whatever stares at {} and {} goes insane.".format(sys.argv[1]))
    print("Does {} flee for your life or eat your head?".format(sys.argv[1]))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def back_room():
    print("You enter the room and everybody is having a party with python.  They ask - what's your name?")

    visitor_name = input(">")

    while(visitor_name == ""):
        print("Sorry, I didn't hear your name.  Please try again")
        visitor_name = input(">")
    
    print("Welcome to our programmer party, " + visitor_name)
    exit(0)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("{} is in a dark room.".format(sys.argv[1]))
    print("There is a door to your right and left and straight and back.")
    print("Which one does {} take?".format(sys.argv[1]))

    next = input("> ")

    if next == "left":
        bear_room()        # tested ok
    elif next == "right":
        cthulhu_room()
    elif next == "straight":
        infinite_stairway_room()
    elif next == "back":
        back_room()
    else:
        dead("{} stumbles around the room until (s)he starves.".format(sys.argv[1]))

if __name__ == '__main__':
    main()
