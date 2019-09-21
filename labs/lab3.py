# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 3 Slopes and Testing (Individual)

# Purpose: Given the x and y components corresponding to two points, compute the
# distance and slope between the two points.

# Preconditions - The inputs the user provides are the respective x and y's to 
# two points in space. The numbers could be either a float or an integer so we 
# will convert them into floats just in case.

# Postconditions - The outputs sent to the screen are of the distance and slope
# between the two points given by the user.

#-------------------------------------------------------------------------------

# 1. We import the square root function from the math library
from math import sqrt

# 2. Creation of our main function
def main():
    
    # 3. Prints to the user the title of the program
    print('Slope Calculator')


    # 4. Asks for 4 inputs that correspond to two points  
    x1 = float(input('Enter first x: '))
    y1 = float(input('Enter first y: '))
    x2 = float(input('Enter second x: '))
    y2 = float(input('Enter second y: '))

    # 5. Print two blank lines
    print()
    print()

    # 6. Creation of the variable representing the distance between two points
    distance = sqrt(( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2) 
    
    # 7. Creation of the variable representing the slope between two points
    slope = ( y1 - y2 ) / ( x1 - x2 ) 
    
    # 8. Prints the distance and slope variables determined above
    print('The distance between the two points is',distance)
    print('The slope is',slope)
    
main() 

#-------------------------------------------------------------------------------

# Calculated A-D expected outputs 

# A = 7.433, -2.8
# B = 9.0, 0.0
# C = 992.5, 9925.0
# D = Error - division by zero
