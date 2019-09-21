'''
Prologue
Name: Andrew Cassidy
Section: 003
Email: andrew.cassidy@uku.edu
Title: Lab 9 Individual
Preconditions: User inputs an integer length for a random list.
Postconditions: Output that you are correcting the original list for highs and 
lows such as 200 and 50 respectively. Afterwards, output the average of the 
remaining list.
'''

# Import the random library.
from random import *

def main():
    # Create a variable for the user inputted sample number.
    sample_num = int(input('How many samples? '))
    print('generating random list')
    # Initializing our random list
    rand_list = []
    # For loop to create n random elements in a list.
    for i in range(sample_num):
        rand_list.append(randint(1,350))
    print('The list is',rand_list)
    # Set all numbers in list, who are greater than 200, equal to 200.
    upper_lim = 200
    print('\nFiltering for highs with upperlimit = 200')
    for i in range(sample_num):
        if rand_list[i] > upper_lim:
            rand_list[i] = upper_lim
    print('The list is',rand_list)
    # Set all numbers in list, who are less than 50, equal to 50.
    lower_lim = 50
    print('\nFiltering for lows with lowerlimit = 50')
    for i in range(sample_num):
        if rand_list[i] < lower_lim:
            rand_list[i] = lower_lim
    print('The list is',rand_list)
    # Find and print the avg of the list of numbers.
    if sample_num == 0:
        print('\nSize is zero, average value is zero')
    else:
        avg = sum(rand_list) / len(rand_list)
        print('\nThe average value is', round(avg,3))
main()

'''
Test Cases:
sample_num = 0
    How many samples? 0
    generating random list
    The list is []

    Filtering for highs with upperlimit = 200
    The list is []

    Filtering for lows with lowerlimit = 50
    The list is []

    Size is zero, average value is zero
sample_num = 1, upper limit is in problem. It will be analagous for 50 as well.
    How many samples? 1
    generating random list
    The list is [200]

    Filtering for highs with upperlimit = 200
    The list is [200]

    Filtering for lows with lowerlimit = 50
    The list is [200] 
    The average value is 200.0
sample_num = 4, a value lower than 50 and also greater than 200 is in the list.
Also, there are values in the correct threshold so that the do not change.
    How many samples? 4
    generating random list
    The list is [252, 77, 34, 154]

    Filtering for highs with upperlimit = 200
    The list is [200, 77, 34, 154]

    Filtering for lows with lowerlimit = 50
    The list is [200, 77, 50, 154]

    The average value is 120.25
sample_num = -1
    How many samples? -1
    ERROR
'''
