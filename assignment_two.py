#--- Fox, Goose, Corn Riddle Game ---#

#--- Imports ---#

import sys
import random

#--- Classes ---#

class Boat:
    
    def __init__(self,pos="near"):
        self.name="Boat"
        self.position=pos

#--- Methods ---#

def welcome():
    print("Welcome to the game!")
    print("The farmer has a boat which can take the farmer and one other item at a time")
    print("Your job is to get the Goose, Fox & Corn all across the river while making sure that")
    print("a) The Goose must not eat the Corn, and")
    print("b) The Fox must not eat the Goose")

def water():
    wave_one=("~     ~         ~                 ~           ~        ~   ~ ~ ~                    ~           ~\n")
    wave_two=("~                            ~ ~       ~    ~      ~~~                 ~       ~         ~     ~    ~\n")
    wave_three=("      ~            ~~~                  ~~~              ~   ~         ~         ~          \n")
    waves=[wave_one,wave_two,wave_three]

    print(random.choice(waves))

def print_scene(boat,far_side,near_side):

    line=""
    
    for item in far_side:
        line+=(" "*15)+(item)
    print(line)

    print(("---"*15)+"Far shore"+("---"*15))

    water()

    if boat.position=="far":
        print(" "*45+"Boat")

    water()
    water()

    if boat.position=="near":
        print(" "*45+"Boat")
    
    water()

    print(("---"*15)+"Near shore"+("---"*15))

    line=""
    for item in near_side:
        line+=(" "*15)+item
    print(line)

def initialize_game():

    boat=Boat("near")

    return(boat,["Fox","Goose","Corn"],[])

def game_loop(boat,near_side,far_side):

    global main_loop_prompt

    while True:

        print_scene(boat,far_side,near_side)

        move=validated_move(main_loop_prompt,["fox","goose","corn","nil","quit"],near_side,far_side,boat)

        boat,near_side,far_side=item_movement(move,boat,near_side,far_side)

        check_result(boat,near_side,far_side)

def validated_move(prompt,acceptable_inputs,near_side,far_side,boat):

    move_validated=False

    while not move_validated:
    
        move=input(prompt).lower().strip()

        if move not in acceptable_inputs:
            print("Please enter a valid input")
        
        if move=="quit":
            sys.exit("Exiting game")

        elif move=="nil":
            move_validated=True

        elif boat.position=="near":
                if move.capitalize() in near_side:
                    move_validated=True
                else:
                    print("Error: This can not be done")
            
        elif boat.position=="far":
                if move.capitalize() in far_side:
                    move_validated=True
                else:
                    print("Error: The item you want to move is on the other side")

    return(move)

def item_movement(move,boat,near_side,far_side):

    move=move.capitalize()
    
    if boat.position=="near":
        boat.position="far"
    else:
        boat.position="near"

    if move=="Nil":
        pass
    else:
        if move in near_side:
            near_side.remove(move)
            far_side.append(move)
        else:
            far_side.remove(move)
            near_side.append(move)

    return(boat,near_side,far_side)

def check_result(boat,near_side,far_side):

    if len(far_side)==3:

        print_scene(boat,far_side,near_side)

        sys.exit("You win!")

    if boat.position=="near":
        unattended_side="far"
    else:
        unattended_side="near"

    if unattended_side=="near":
        if len(near_side)==2 and "Fox" in near_side and "Goose" in near_side:
            sys.exit("\n\nYou lose! The Fox ate the Goose while you were away")

        if len(near_side)==2 and "Goose" in near_side and "Corn" in near_side:
            sys.exit("\n\nYou lose! The Goose ate the corn while you were away")

    if unattended_side=="far":
        if len(far_side)==2 and "Fox" in far_side and "Goose" in far_side:
            sys.exit("\n\nYou lose! The Fox ate the Goose while you were away")

        if len(far_side)==2 and "Goose" in far_side and "Corn" in far_side:
            sys.exit("\n\nYou lose! The Goose ate the corn while you were away")

#--- Constants ---#

main_loop_prompt="Enter the name of the item to transport across the river\nIf you would like to transport no item, enter Nil\nEnter Quit to exit the game\n>"

#--- Main ---#

welcome()

boat,near_side,far_side=initialize_game()

game_loop(boat,near_side,far_side)