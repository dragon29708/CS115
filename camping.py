# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 4 Individual

# Purpose: Create a camping supply store program that uses the total_bill variable
# to accrue the total bill for the transaction.

# Preconditions: Given a 'y' or 'n' answer to asking if the user wants certain items,
# determine the total bill w and w/o sales sax.

# Postconditions: Both the total bill w and w/o sales tax should be outputted to the
# user. They should also be thanked for their business afterwards.


def main():

    # 1. display title
    print('Camping Supply Store\n')

# 2. display instructions
    print('Enter y or n to answer the questions')

# 3. initialize total bill
    total_bill = 0

# 4. ask if they want 4 different items:

#   a. ask about walking stick, if yes, add cost to bill
    stick = input('Do you want a walking stick? ($15) ')

    if stick == 'y':
        total_bill += 15

#   b. ask about canteen, if yes, add cost to bill
    canteen = input('Do you want a canteen? ($10) ')

    if canteen == 'y':
        total_bill += 10

#   c. ask about water filter, if yes, add cost to bill
    water_filter = input('Do you want a water filter? ($25) ')

    if water_filter == 'y':
        total_bill += 25

#   d. ask about tent, if yes, add cost to bill
    tent_first_ask = input('Do you want a tent? (100-150) ')

#   if statement to print a blank line depending on your answer to tent question
    if tent_first_ask == 'n':
        print()

#   check whether they want a normal or a large tent
    if tent_first_ask == 'y':
        large_tent_ask = input('Do you want a large tent? (150) ')

#       they want a tent, now add 100 or 150 to the total bill depending on their prefered size of tent
        if large_tent_ask == 'y':
            total_bill += 150
            print()
        else:
            total_bill += 100
            print()

# 5. calculate sales tax of 6%
    sales_tax = .06 * total_bill

# 6. calculate total bill with tax and round the bill
    total_bill_w_tax = total_bill + sales_tax
    total_bill_w_tax = round(total_bill_w_tax,2)

# 7. display total bill with $ in front
    print('Your total bill is ', total_bill, sep='$')

# 8. display total bill plus tax with $ in front
    print('Your total bill plus tax is ', total_bill_w_tax, sep='$')

# 9. thank them for their business
    print('Thank you for your business! ')


main()
