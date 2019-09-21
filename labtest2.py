'''
Name: Andrew Cassidy
Section: 003
Email: andrew.cassidy@uky.edu
'''

# Import the graphics and math libraries.
from graphics import *
from math import *

# Function to compute the distance between two points
def distance (click1, click2):
    # Variables that hold the x and y coordinates of two points.
    x1 = click1.getX()
    x2 = click2.getX()
    y1 = click1.getY()
    y2 = click2.getY()
    # Returns the distance computation.
    return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# Main function.
def main():
    win = GraphWin('Lab Test 2',650,450)
    # Variables for locations.
    lower_middle = Point(325,400)
    # Initial prompt.
    click_text = Text(lower_middle,'Click 6 Times')
    click_text.draw(win)
    # Area accumulator variable.
    acu = 0
    # Main loop for program.
    for i in range(3):
        # Get two points from the user's clicks.
        user_click1 = win.getMouse()
        user_click2 = win.getMouse()
        # Distance between the users two clicks.
        d = distance(user_click1, user_click2)
        # Draw a circle at click1 with radius d.
        cir = Circle(user_click1,d)
        cir.draw(win)
        # Calculate the area of the circle that was just drawn. Then add the area to an acumulator.
        area = pi * (d ** 2)
        acu += area
        # If statement to control the color of the circle.
        if area > 3500:
            cir.setFill('Blue')
        else:
            cir.setFill('Red')
    # Undraw the first prompt.
    click_text.undraw()
    # Display the total area of the three circles, rounded to one decimal place.
    area_text = Text(Point(295,375),'Total Area:')
    area_num = Text(Point(370,375),round(acu,1))
    area_text.draw(win)
    area_num.draw(win)
    # Prompt user to click to close.
    close_text = Text(lower_middle,'Click to Close')
    close_text.draw(win)
    # Close program after pause.
    win.getMouse()
    win.close()
main()