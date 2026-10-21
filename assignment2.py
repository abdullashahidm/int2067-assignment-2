#--- Fox, goose & corn Riddle game ---#

"""
This code is my own individual and original work with very limited AI assistant. For
any part of codes that are referenced to, supported by AI, acknowledgement will be
specified
"""

#--- Imports ---#
import random
import sys

#--- Methods ---#
def water():
    wave_one=("~     ~         ~                 ~           ~        ~   ~ ~ ~                    ~           ~\n")
    wave_two=("~                            ~ ~       ~    ~      ~~~                 ~       ~         ~     ~    ~\n")
    wave_three=("      ~            ~~~                  ~~~              ~   ~         ~         ~          \n")
    waves=[wave_one,wave_two,wave_three]

    print(random.choice(waves))

def new_line():
    print("\n")

def validate_inputs(prompt,acceptable_inputs):
    user_choice_valid=False
    while not user_choice_valid:
        user_choice=input(prompt).strip().lower()
        if user_choice not in acceptable_inputs:
            print("Error: Please enter one of the stated options")
        else:
            user_choice_valid=True
    return(user_choice)

def print_scene(far_side,near_side):
    global boat_position

    far_side_objects=""
    for item in far_side:
        far_side_objects=far_side_objects+item+(" "*20)
    print(far_side_objects)
    new_line()

    print("- "*20,"Far shore","- "*30)
    
    water()

    if boat_position=="far":
        print("  "*20,"Boat")

    water()
    water()
    water()
    
    if boat_position=="near":
        print("  "*20,"Boat")
        water()
    
    print("- "*20,"Near shore","- "*30)
    new_line()
    
    near_side_objects=""
    for item in near_side:
        near_side_objects=near_side_objects+item+(" "*20)
    print(near_side_objects)

    new_line()

def check_game_result(far_side,near_side):
    
    if len(far_side)==3:
        return("won")

#--- Main ---#

# Goal of game
print("Welcome to the Fox Goose Corn Riddle game")
print("You must transport all 3 items across the river\nYou can only take one item at a time\nDo no leave the goose alone with corn, or forx alone with goose")

# Initialize some required items for the game
far_side=[]
near_side=["Fox","Goose","Corn"]
boat_position="near"

game_over=False
game_won=False

while not game_over:
    print_scene(far_side,near_side)
    
    user_move=validate_inputs(f"Boat is at {boat_position} shore, choose what to take to other shore.\nIf you would like to take nothing to the other side, Enter nil\nAlternately, enter 'quit' to exit game >",["quit","corn","goose","fox","nil"])
    new_line()
    print("--"*75)
    new_line()

    if boat_position=="near":
        boat_position="far"
    else:
        boat_position="near"

    if user_move=="quit":
        sys.exit("Exiting game, goodbye")

    if user_move=="corn":

        if "corn" in far_side:
            far_side.remove("Corn")
            near_side.append("Corn")
        else:
            near_side.remove("Corn")
            far_side.append("Corn")

    if user_move=="goose":

        if "goose" in far_side:
            far_side.remove("Goose")
            near_side.append("Goose")
        else:
            near_side.remove("Goose")
            far_side.append("Goose")

    if user_move=="fox":

        if "fox" in far_side:
            far_side.remove("Fox")
            near_side.append("Fox")
        else:
            near_side.remove("Fox")
            far_side.append("Fox")

    result=check_game_result(far_side,near_side)

    if result=="won":
        game_won=True
        game_over=True

if game_won:
    print("Congratulations, you have passed the game")
else:
    print("Game over, you did not complete successfully")