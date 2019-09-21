'''
Prolog -
Names: Nahaba Hamada, Andrew Cassidy, John DeMoor
Section: 003
E - mails: nkha229@uky.edu, arca248@uky.edu, john.demoor@uky.edu
Purpose: Test return methods for function in python.
Preconditions: No inputs.
Postconditions: Output 3 for loops using pop1 - 3 function.
'''

from math import *

def pop1(t1 ):
    '''
    Returns a string of the value calculated
    '''
    value1 = 1 / (1 + e ** (-1 * t1))
    return print(value1)

def pop2(t2 ):
    '''
    Returns a float of the value calculated
    '''
    value2 = 1 / (1 + e ** (-1 * t2))
    return value2

def pop3(t3, lst):
    '''
    Places a calculated value into the first element of a list.
    '''
    lst[0] = 1 / (1 + e ** (-1 * t3))

def main():
    '''
    Tests the validity of the functions pop1, pop2 and pop3.
    '''
    print('Testing Functions in Python:\n')
    # Loop that tests pop1
    for t in range(-6, 7):
        print(t, ' ', end='')
        pop1(t)
    total = 0
    print()
    # Loop that tests pop2
    for t in range(-6, 7):
        result = pop2(t)
        total += result
        print("Total is", total)
    result = [0]
    total = 0
    print()
    # Loop that tests pop3
    for t in range(-6, 7):
        pop3(t,result)
        total += result[0]
        print("The second total is", total)
main()
