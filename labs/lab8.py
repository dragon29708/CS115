'''
Prologue
Name: Andrew Cassidy
Section: 003
Email: andrew.cassidy@uky.edu
Title: Lab 8 Individual
Purpose: Create a program that computes the square root of a number
Preconditions: Have the user input a number for which it will be square 
rooted.
Postconditions: Output to the user the interation of the particular step of
Newton's method for taking a square root. Afterwards, output the calculated 
square root and show that it is true by comparing it to the math libaries.
'''
# Import the math libary.
from math import *

def main():
    # Have the user input a number to be square-rooted.
    n = float(input('What number do you want to take the square root of? '))
    newguess = n / 2
    oldguess = 0
    i = 1
    # While loop to calculate the square root of n.
    while abs(newguess - oldguess) >= 1e-10:
        print('Iteration', i, newguess)
        # The new guess now becomes the old guess.
        oldguess = newguess
        # Newton's method for taking the square root.
        newguess = .5 * (oldguess + n / oldguess)
        i += 1
    # Output the square root of n. Also, show that the calculator worked.
    print('The square root from the math library is', sqrt(n))
    print('The difference between Newton\'s method and the math library function is', newguess - sqrt(n))
main()

'''
Test Cases:
1. 4.00, 6 iterations
2. 4.24, 6 iterations
3. 100.00, 11 iterations
4. -1.91, 4 iterations
5. 0.00,0 iterations
'''
