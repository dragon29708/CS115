# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 6 Individual

# Purpose: Create a program that uses a loop and if/else statements to compare inputted numbers.

# Preconditions: Have the user input 5 numbers in total. Run through a loop that compares the
# inputted values, changes a bool value, and replaces the first number with a new number.

# Postconditions: Output to the user when to enter numbers. Afterwards, output a general truth
# based on the comparision of the inputted values.


def main():

    # initialize first num flag to a true bool value
    num1_greater = True

    # prompt user to input a number
    num1 = int(input('Enter number: '))

    # for loop - need to occur 4 times
    for i in range(4):

        # ask user to input a new number
        new_num = int(input('Enter number: '))

        # if structure to compare the entered number to num1
        if num1 <= new_num:

            # set bool to false and replace the new number with the first num
            num1_greater = False
            num1 = new_num

    # if statement to output the final bool value
    if num1_greater == True:
        print('Yes. All numbers entered after the first were less than the first.')
    else:
        print('No. You entered a number that was of equal or greater value to the first number entered.')


main()
