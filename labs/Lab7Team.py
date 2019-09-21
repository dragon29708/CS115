# Prolog
# Names: Nahaba Hamada, Andrew Cassidy, John DeMoor
# Section: 3
# E-mail: nkha229@uky.edu

# Purpose: Draw a fractal using graphics

# Preconditions: Have libraries, lines, points, methods properly set.

# Postconditions: A fractal with a seed of 501 and 2000 iterations will be drawn. 

# Import needed libraries

from graphics import *
import random

def drawPt(p, win):
      # drawPt will draw Point p as a small red circle on the GraphWin win.  
      # pre-conditions:  Point P and GraphWin win
      # post-conditions: no return value, changes GraphWin by displaying a
      #   red circle of radius 3 centered at point P
      c = Circle (p, 3)
      c.setFill("red")
      c.setOutline("red")
      c.draw(win)

def main():
      
      # Define seed
      random.seed(501)
      
      # Create a graphics window, sized 500 by 600, with a title of Gaskets
      win = GraphWin("Gaskets", 500,600)
      
      # Get a random number that falls in the range of the width of the graphics 
      # window and another one in the range of the height of the graphics window. 
      x1 = random.randrange(1,501)
      y1 = random.randrange(1,601)
      
      x2 = random.randrange(1,501)
      y2 = random.randrange(1,601)      

      x3 = random.randrange(1,501)
      y3 = random.randrange(1,601)     

      x4 = random.randrange(1,501)
      y4 = random.randrange(1,601)      
      
      # Make a point with those numbers as the x and y of a Point and call it A. # Repeat the process for a Point called B and a Point called C. # Repeat the process one more time for a Point called start.
      A = Point(x1,y1)
      B = Point(x2,y2)
      C = Point(x3,y3)
      start = Point(x4,y4)
    
      # Draw all four Points using the drawPt function given.
      drawPt(A,win)
      drawPt(B,win)
      drawPt(C,win)
      drawPt(start,win)
      
      # Create a Text object somewhere near the bottom of the graphics window. Its text message should be an empty string. Draw it.
      prompt = Text(Point(485, 585), '')
      prompt.draw(win)
      
      # Create a loop that will run 2000 times.
      for i in range(2000):
      
          # Get a random number from 1 to 6 (the die in the video)
            a = random.randrange(1,7)
          # Use the die number to choose which of the 3 Points, A, B or C will be used
            if a == 1 or a == 2:
                  use = A
            elif a == 3 or a == 4:
                  use = B
            else:
                  use = C
          # Make a line with one end being the start Point and the other being the chosen Point (A,B or C)
            line = Line(start,use)
          # Use a method for Lines which finds the midpoint of the line
            mid = line.getCenter()
          # Draw the midpoint of the Line using drawPt (given function)
            drawPt(mid,win)
          # After that logic, update the start Point to be the midpoint
            start = mid
          # Use setText method of the Text object created before the loop to display the counter of the loop
            prompt.setText(i+1)
      # After loop, do usual pause and close   
      win.getMouse()
      win.close()      
          
main()
