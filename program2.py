'''
Prologue:
Author: Andrew Cassidy
Worked With: Nahaba Hamada 
Email: andrew.cassidy@uky.edu, nkha229@uky.edu
Section: 003

Title: Program 2 Phase I
Purpose: To create a game that allows the user to find a hidden cat
Preconditions: User will input whether they will enter test or normal mode. Then, 
they will enter their desired difficulty and keep inputting guess points until
they guess the correct location of the cat.
Postconditions: Keep asking the user for new guesses and let them know how close
their last guess was to finding the cat. After finding the cat, let the user
know they won and how my tries it took them to win.
'''

from math import *
from graphics import *
from random import *

def distance (cat_loc, user_input ):
# All four parameters are integers.
# They represent the coordinates of two points.
# The distance between the two points is returned.
    x1 = cat_loc.getX()
    x2 = user_input.getX()
    y1 = cat_loc.getY()
    y2 = user_input.getY()
    return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def main():
    win = GraphWin('Find the Animal!',500,500)
    win.setBackground('white')
    # Reference point variables.
    middle = Point(250,250)
    lower_middle = Point(250,400)
    lower_right = Point(400,400)
    upper_middle = Point(250,100)
    upper_right = Point(425,25)
    upper_left = Point(65,25)
    # Title of the program.
    title = Text(middle,'Find the Invisible Cat!')
    title.draw(win)
    win.getMouse()
    title.undraw()
    # Initialize location of cat.
    cat_point = Point(randint(50,375),randint(50,375))
    # User selects whether or not they would like to enter testing mode.
    mode_text = Text(lower_middle,'Testing mode? (Y/N) ')
    mode_text.draw(win)
    mode_input = Entry(Point(250,425),10)
    mode_input.draw(win)
    mode_input.setText('n')
    win.getMouse()
    mode = mode_input.getText()
    mode_input.undraw()
    mode_text.undraw()
    # Tell the user where the cat is if they are in testing mode.
    if mode == 'y' or mode == 'Y':
        test_text = Text(cat_point,'The cat is here!')
        test_text.draw(win)  
    # User selects the difficulty of the game.
    diff_text = Text(lower_middle,'Difficulty? (smaller is harder)')
    diff_text.draw(win)
    diff_input = Entry(Point(250,425),50)
    diff_input.draw(win)
    diff_input.setText('5')
    win.getMouse()
    diff = int(diff_input.getText())
    diff_text.undraw()
    diff_input.undraw()    
    # While loop to only allow difficulty to range from 1-25.
    while diff > 25 or diff < 1:
        invalid_text = Text(lower_middle,'Invalid difficulty, 1-25 allowed')
        invalid_text.draw(win)
        diff_input.draw(win)
        win.getMouse()
        diff = diff_input.getText()
        # If statement to set the default difficulty to 5.
        if diff == '' or diff == ' ':
            diff = 5
        else:
            diff = int(diff)
        diff_input.undraw()
        invalid_text.undraw()
    # Undraw the difficulty input text.
    diff_text.undraw()
    diff_input.undraw()
    # Initalizing user point variable.
    user_point = Point(0,0)
    # Create a variable that counts the amount of tries.
    t_text = Text(Point(35,25),'Tries:')
    t_text.draw(win)
    tries = 0
    try_text = Text(upper_left,tries)
    try_text.draw(win)    
    # Text object that changes color
    color_text = Text(Point(250,450),'CAT')
    color_text.setSize(20)
    color_text.draw(win)
    # User must keep clicking.
    user_text = Text(lower_middle,'Click to Find the Cat!')
    user_text.setSize(20)
    user_text.draw(win)    
    # While loop for interation with user.
    while distance(cat_point,user_point) > diff * 4:
        # Output changes if we are in test mode.
        d = distance(cat_point,user_point)
        if mode == 'y' or mode == 'Y':
            dist_text = Text(upper_right,'Distance:')
            dist_num = Text(Point(475,25),d)
            dist_text.draw(win)
            dist_num.draw(win)        
        # Give the game a new guess of where the cat is.
        user_point = win.getMouse()
        # Draw a circle where the user clicked.
        cir = Circle(user_point,5)
        cir.draw(win)
        if mode == 'y' or mode == 'Y':
            dist_text.undraw()
            dist_num.undraw()         
        # Ouput the number of tries.
        try_text.undraw()
        tries += 1
        try_text = Text(upper_left,tries)
        try_text.draw(win)
        # If structure to output to the user how close they are from the cat.
        if d > diff:
            if  d <= diff + 10 * diff:
                color_text.setFill('Red')
            elif d <= diff + 12 * diff:
                color_text.setFill('Orange Red')
            elif d <= diff + 15 * diff:
                color_text.setFill('Coral')
            elif d <= diff + 17 * diff:
                color_text.setFill('Light Blue')
            else: 
                color_text.setFill('Dodger Blue')
    # Display the picture of the cat.
    cat_image = Image(cat_point,'animal.gif')
    cat_image.draw(win)
    # Undraw Prompts.
    user_text.undraw()
    color_text.undraw()
    try_text.undraw()
    t_text.undraw()
    # End of game. Show the user their stats.
    found_text = Text(middle,'You found him! Tries Attempted:')
    found_text.setSize(15)
    found_text.setStyle('bold')
    found_text.draw(win)
    # How many tries it took the user.
    tries_attempt = Text(Point(250,275), tries)
    tries_attempt.setSize(15)
    tries_attempt.setStyle('bold')    
    tries_attempt.draw(win)
    # Close the window once done.
    win.getMouse()
    win.close()    
main()