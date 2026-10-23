#--- Fox, Goose, Corn Riddle Game ---#

#--- Imports ---#

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

    for item in far_side:
        line=(" "*15)+(item)
    print(line)

    print(("---"*15)+"Far shore"+("---"*15))

    water()

    if boat.position=="far":
        print(" "*20+"Boat")

    water()
    water()

    if boat.position=="near":
        print(" "*20+"Boat")
    
    water()

    print(("---"*15)+"Near shore"+("---"*15))

    for item in near_side:
        line=(" "*15)+item
    print(line)

def initialize_game():

    boat=Boat("near")

    return(boat,["Fox","Goose","Corn"],[])

def game_loop(boat,near_side,far_side):

    global main_loop_prompt

    while True:

        print_scene()

        move=validated_move(main_loop_prompt,["fox","goose","corn","nil","quit"],near_side,far_side,boat)

        ## Do the swapping as necessary

        ## Check for victory or loss

def validated_move(prompt,acceptable_inputs,near_side,far_side,boat):

    move_validated=False

    while not move_validated:
    
        move=input(prompt).lower().strip()

        if move not in acceptable_inputs:
            print("Please enter a valid input")
        
        elif boat.position=="near":
                if move in near_side:
                    move_validated=True
                else:
                    print("Error: The item you want to move is on the other side")
            
        elif boat.position=="far":
                if move in far_side:
                    move_validated=True
                else:
                    print("Error: The item you want to move is on the other side")

    return(move)


#--- Constants ---#

main_loop_prompt="Enter the name of the item to transport across the river\nIf you would like to transport no item, enter Nil\nEnter Quit to exit the game\n>"

#--- Main ---#

welcome()

boat,near_side,far_side=initialize_game()

game_loop(boat,near_side,far_side)