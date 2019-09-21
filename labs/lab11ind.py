'''
Author: Andrew Cassidy
Email: andrew.cassidy@uky.edu
Section: 003
Title: Lab 11 Individual
Purpose: Create a program that calculates payroll of n employees.
Preconditions: User n employee names, hours worked, and their hourly rats in
a comma separated list.
Postconditions: Output the total payroll of all the user entered employees.
'''


def main():
    # Initial messages for program.
    print('Payroll for ACME\n')
    print('Press Enter to stop')
    # Initialize payroll list and total.
    payroll = []
    total = 0
    user_input = input('Enter name, comma, hours worked, comma, hourly rate: ')
    # While loop to alter the payroll list.
    while user_input != '':
        temp_list = user_input.split(',')
        ind_payroll = float(temp_list[1]) * float(temp_list[2])
        total += ind_payroll
        payroll.append([temp_list[0], ind_payroll])
        user_input = input('Enter name, comma, hours worked, comma, hourly rate: ')
    # Print the total payroll.
    print('Total payroll', round(total, 2), sep = ' $')
    print()
    # Print all individual payrolls.
    for i in range(len(payroll)):
        print(payroll[i][0], payroll[i][1], sep='   $')
main()
