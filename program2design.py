'''
Prologue:
Author: Andrew Cassidy
Worked With: Nahaba Hamada 
Email: andrew.cassidy@uky.edu, nkha229@uky.edu
Section: 003

Title: Program 2 Design

import the math library

make this function by copying it from the assignment:
def distance (x1,y1, x2,y2 ):
# All four parameters are integers.
# They represent the coordinates of two points.
# The distance between the two points is returned.
    return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

main function
    Title of the program.
    print Find the Invisible Cat!
    Initialize location of cat
    catx = 25
    caty = 25
    User selects whether or not they would like to enter testing mode.
    mode = input y or n for the mode you want
    Tell the user where the cat is if they are in testing mode.
    if mode == 'y' or mode == 'Y':
        blank space
        print the cats point  
    User selects the difficulty of the game.
    While loop to only allow difficulty to range from 1-25.
    while diff > 25 or diff < 1:
        print Invalid difficulty, 1-25 allowed
        diff = input('Difficulty? (smaller is harder) ')
        If statement to set the default difficulty to 5.
        if diff == '' or diff == ' ':
            diff = 5
        else:
            diff = make diff an integer
    Initializing the x and y coordinate variables for the user.
    userx = 0
    usery = 0
    Creating a variable that counts the amount of tries.
    tries = 0
    If structure to determine whether the user is in test mode or not.
    if mode == 'n' or mode == 'N':
        While loop when not in test mode.
        blank space
        while distance between catx,caty and userx,usery > diff:
            Give the game a new guess of where the cat is.
            Add 1 to the try count
            If structure to output to the user how close they are from the cat.
            if distance between catx,caty and userx,usery > diff and distance between catx,caty and userx,usery <= diff + diff / 10:
                print Almost there! 
            elif distance between catx,caty and userx,usery > diff / 10 and distance between catx,caty and userx,usery <= diff + diff / 8:
                print Close. 
            elif distance between catx,caty and userx,usery > diff / 8 and distance between catx,caty and userx,usery <= diff + diff / 6:
                print Far.
            elif distance between catx,caty and userx,usery > diff / 6 and distance between catx,caty and userx,usery <= diff + diff / 4:
                print Really far.
            else: 
                print Not even close.
    else:
        While loop while in test mode.
        blank line
        while distance(catx,caty,userx,usery) > diff:
            Give the game a new guess of where the cat is.
            Tell user the distance between the click and the mouse location.
            print Distance is distance between catx,caty and userx,usery
            add 1 to try count
            If structure to output to the user how close they are from the cat.
            if distance between catx,caty and userx,usery > diff and distance between catx,caty and userx,usery <= diff + diff / 10:
                print Almost there! 
            elif distance between catx,caty and userx,usery > diff / 10 and distance between catx,caty and userx,usery <= diff + diff / 8:
                print Close. 
            elif distance between catx,caty and userx,usery > diff / 8 and distance between catx,caty and userx,usery <= diff + diff / 6:
                print Far.
            elif distance between catx,caty and userx,usery > diff / 6 and distance between catx,caty and userx,usery <= diff + diff / 4:
                print Really far.
            else: 
                print Not even close.
    End of game. Show the user their stats.
    print You found him!
    print Yay!!
    print It took you, tries amount, tries
end of main function
'''