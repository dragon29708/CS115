'''
Prolog
Names: Nahaba Hamada, Andrew Cassidy, John DeMoor
Section: 3
E-mail: nkha229@uky.edu, arca248@uky.edu, johndemoor@uky.edu
Purpose: Create two boxes that allow the user to click yes or no on and prompt
the user of their decision
Preconditions:
Postconditions:
'''

# import the graphics library
from graphics import *
# create main function
def main():
   # Create a graphics window
   win = GraphWin('Yes or No',500,500)
   # set height and width variables
   height = 100
   width = 100
   # Create two points for each box (upper left, lower right, center)
   upperL1 = Point(100,200)
   lowerR1 = Point(200,300)
   yesboxX1 = 100
   yesboxX2 = 200
   yesboxY1 = 200
   yesboxY2 = 300
   upperL2 = Point(300,200)
   lowerR2 = Point(400,300)
   noboxX1 = 300
   noboxX2 = 400
   noboxY1 = 200
   noboxY2 = 300   
   yescenter = Point(150,250)
   nocenter = Point(350,250)
   # Create the 2 boxes, draw them and color them
   yesbox = Rectangle(upperL1,lowerR1)
   nobox = Rectangle(upperL2,lowerR2)
   yesbox.draw(win)
   nobox.draw(win)
   yesbox.setFill("green")
   nobox.setFill("red")   
   # Label the two boxes Yes and No and draw them
   yes = Text(yescenter, 'YES')
   no = Text(nocenter, 'NO')
   yes.draw(win)
   no.draw(win)
   # Display a prompt "Click yes or no"
   clickprompt = Text(Point(250,400),'Click yes or no')
   clickprompt.draw(win)
   # get a click from user and get X and Y from the Point clicked
   userpt = win.getMouse()
   userptX = userclick.getX()
   userptY = userclick.getY()
   # while neither box is clicked (most difficult part!)
   while not (yesboxX1 <= userptX <= yesboxX2 and yesboxY1 <= userptY <= yesboxY2) and not (noboxX1 <= userptX <= noboxX2 and noboxY1 <= userptY <= noboxY2):
      # get another click and get X and Y from the Point clicked
      userpt = win.getMouse()
      userptX = userclick.getX()
      userptY = userclick.getY()
   # Check to see which box was clicked
   if yesboxX1 <= userptX <= yesboxX2 and yesboxY1 <= userptY <= yesboxY2:
      # output text with You Clicked Yes!!
      yestext = Text(Point(150,350),'You Clicked Yes\!\!')
      yestext.draw(win)
   elif noboxX1 <= userptX <= noboxX2 and noboxY1 <= userptY <= noboxY2:
      # output text with You Clicked No!!
      notext = Text(Point(350,350),'You Clicked No\!\!')
      notext.draw(win)
   # Prompt for "click to close"
   closetext = Text(Point(250,250),'Click to Close')
   closetext.draw(win)
   # Wait for Click
   win.getMouse()
   # close win
   win.close()
main()