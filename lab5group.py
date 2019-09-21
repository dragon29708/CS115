# Prolog
# Author:  Andrew Cassidy, John DeMoor, Nahaba Hamada
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 5 (Team)

# Purpose: Create a gpa calculator

# Preconditions: Using a for loop, have the student input their amout of classes, grade and credit hour
# total per class.

# Postconditions: Print the students gpa, total quality points, total credit hours, and give them a
# message pertaining to whether or not they received deans list or they are on academic probation.


def main():

    # initialize total_credit_hours and quality_point_total to zero
    total_credit_hours = 0
    quality_point_total = 0
    quality_points = 0

    # ask user for the number of classes
    num_classes = int(input('How many classes did you take? '))

    # for each class (a loop!)
    for i in range(num_classes):

        # input grade and credit hours per class
        grade = input('Grade? ')
        credit_hours = int(input('Credit hours? '))

        # convert letter grade to quality points using an if/elif/elif/elif/elif/else control structure
        if grade == 'A' or 'a':
            quality_points = 4
        elif grade == 'B' or 'a':
            quality_points = 3
        elif grade == 'C' or 'c':
            quality_points = 2
        elif grade == 'D' or 'd':
            quality_points = 1
        elif grade == 'E' or 'e':
            quality_points = 0
        else:
            print('Invalid grade. Using zero for quality points')
            quality_point_total = 0

        # add quality points * credit hours to quality_point_total
        quality_point_total = quality_points * credit_hours

        # add credit hours to total_credit_hours
        total_credit_hours += credit_hours

    # if total_credit_hours is greater than zero
    print()
    if total_credit_hours > 0:
        # divide quality_point_total by total_credit_hours to get gpa
        gpa = quality_point_total / total_credit_hours

    # otherwise gpa is 0
    else:
        gpa = 0.0

    # output _______, ______ and gpa
    print('Total Quality Points', quality_point_total)
    print('Total Credit Hours', total_credit_hours)
    print()
    print(r'Grade Point Average =', round(gpa, 2))

    # check gpa for special classifications: Probation and Dean's List using ____ (what control structure?)
    if gpa > 3.50 and total_credit_hours >= 12:
        print('Dean\'s List')
    elif gpa < 2.0:
        print('Academic Probation')


main()
