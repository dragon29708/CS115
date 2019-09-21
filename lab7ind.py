'''
Prologue
Name: Andrew Cassidy
Section: 003
Email: andrew.cassidy@uku.edu
Preconditions: Have the user input their name into a box to wish them 
happy birthday.
Postconditions: Ouput to the user their name, with the text box gone. Also, 
create a house, cirle, point, rectangle, triangle, and an oval. All being 
are colored that shows up after the user clicks.
'''

from graphics import *

def main():
    # create a 800 x 1000 pixel window
    win = GraphWin("Greeting Card", 800,1000)
    # establish the center point for later use
    center = Point(400, 500)
    below_center = Point(400, 600)
    # create happy birthday / ask user for name prompt
    prompt = Text(center,'Happy Birthday! Please Enter Your Name Below:')
    prompt.draw(win)
    # have user input name and output it to the screen. also, undraw the input box
    input_box = Entry(below_center,15)
    input_box.draw(win)
    win.getMouse() # pause for input
    name = input_box.getText()
    draw_name = Text(Point(400,550),name)
    draw_name.draw(win)
    input_box.undraw()
    # set window background to yellow
    win.setBackground('Gray')
    # create house objects
    leftwall = Line(Point(100,900), Point(100,200))
    rightwall = Line(Point(700,900), Point(700,200))
    betweenwalls = Line(Point(100,200),Point(700,200))
    leftroof = Line(Point(100,200),Point(400,50))
    rightroof = Line(Point(700,200),Point(400,50))
    floor = Line(Point(100,900),Point(700,900))
    # draw house objects
    leftwall.draw(win)
    rightwall.draw(win)
    betweenwalls.draw(win)
    leftroof.draw(win)
    rightroof.draw(win)
    floor.draw(win)
    # random shapes 
    circle = Circle(Point(400, 350),75)
    rec = Rectangle(Point(375,400),Point(425,375))
    eye1 = Oval(Point(375,350),Point(350,300))
    eye2 = Oval(Point(425,350),Point(400,300))
    tri = Polygon(Point(325,300),Point(475,300),Point(400,250))
    # draw random shapes
    circle.draw(win)
    rec.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    tri.draw(win)
    # color random shapes
    circle.setFill('Blue')
    rec. setFill('Green')
    eye1.setFill('Yellow')
    eye2.setFill('Orange')
    tri.setFill('Red')
    # get mouse and close window 
    win.getMouse()
    win.close()    
main()