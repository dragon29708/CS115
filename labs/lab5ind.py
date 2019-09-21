# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 5 Individual

# Purpose: Create a program that compares two inputed dates and compare them to see which is
# earlier / later / same compared to the other.

# Preconditions: Given 6 inputs corresponding to two separate dates, we need to create a program
# that utalizes logic to sort out whether the two dates are the same or different. If they are
# determined to be different, we also need to find out which one is later or earlier than the other.

# Postconditions: Output to the user the comparison of the two inputted dates. Show them that the dates
# are the same, earlier, or later in terms on date1 and date2.


def main():

    same_date_flag = False
    first_earlier_flag = False


#   input the first date
    first_month = int(input('Enter first month: '))
    first_day = int(input('Enter first day: '))
    first_year = int(input('Enter first year: '))
    print()

#   input the second date
    second_month = int(input('Enter second month: '))
    second_day = int(input('Enter second day: '))
    second_year = int(input('Enter second year: '))
    print()


#   print the comparison of the two dates with their dates included
    if same_date_flag == False:

        if first_earlier_flag == True:
            print('Date1: is earlier than Date2:')
        else:
            print('Date1: is later than Date2:')
    else:
        print('Date1: is the same as Date2:')


main()
