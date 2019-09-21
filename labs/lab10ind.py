'''
Prologue:
Author: Andrew Cassidy
Email: andrew.cassidy@uky.edu
Section: 003

Title: Lab 10 Individual
Purpose: To create an program that has two function. 1. - Create a function
that evaluates whether a year is leap or not. 2. - Create an loop that will
iterate until the user inputs -1 as a year.
Preconditions: User inputs a year.
Postconditions: Both functions evaluate and output whether the year is leap or
not.
'''

def leapyear(year):
    '''
    Validates whether a year is a leap year or not. 
    Returns a boolean value of true or false.
    '''
    leap = False
    # Loop to confirm if a year is a leap year.
    if year % 4 == 0:
        # If year is divisiable by 4 and 100.
        if year % 100 == 0:
            # If year is divisible by 4, 100 and 400. 
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

def main():
    # Ask user for a year.
    year = int(input('Enter a year: '))
    # See if the user enters a year that is a leap year.
    while year != -1:
        if leapyear(year) == True:
            print('Yes, it is a leapyear')
        else:
            print('No, it is not a leapyear')
        year = int(input('Enter a year: '))
main()
