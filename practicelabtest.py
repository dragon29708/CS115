# Prologue

# Author: Andrew Cassidy
# Email: andrew.cassidy@uky.edu

# Title: Practice CS 115 Lab Test 1

# Preconditions: Have the user input 3 numbers so that we can caluculate
# whether there exists an even number or not in the numbers they entered.

# Postconditions: Output to the user if the numbers inputted are all even,
# at least one even, or have no even numbers at all. Afterwards, output
# the average and the sum of the 3 numbers inputted.


def main():

    # print the title
    print('Practice Lab Test\n')

    # have user enter 3 integer numbers
    num1 = int(input('Enter a number '))
    num2 = int(input('Enter a number '))
    num3 = int(input('Enter a number '))

    # variables that represent the amount of evens inputted
    least1even = False
    alleven = False
    noeven = False

    # if statments to find the amount of even numbers
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        alleven = True
    elif num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0:
        least1even = True
    else:
        noeven = True

    # sum and average of the inputted numbers
    thesum = num1 + num2 + num3
    avg = (thesum) / 3

    # if/elif/elif structure to control the output based on the amount of evens
    if least1even == True:
        print('At least one is even')
    elif alleven == True:
        print('All are even')
    elif noeven == True:
        print('None are even')

    # print the sum and average of the 3 numbers
    print('The average is', round(avg, 2))
    print('The sum is', thesum)


main()
