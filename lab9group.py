'''
Name: John DeMoor, Andrew Cassidy, Nahaba Hamada
Section: 003
Email: john.demoor@uky.edu, andrew.cassidy@uky.edu, nkha229@uky.edu
Purpose: Calculate the average of three grades for a list of students.
Preconditions: The name of each student and three of their grades.
Postconditions: List of student names and their average grades.
'''

def main():
    # Define list
    studentgrades = []
    # Initialize flag
    teststudent = False
    # Get first input
    student = input('Enter a student name (STOP to stop) ')
    # Define main loop
    while student != 'stop' and student != 'STOP':
        # Get grades/find average
        grade1 = float(input('Enter a grade '))
        grade2 = float(input('Enter a grade '))
        grade3 = float(input('Enter a grade '))
        avg = (grade1 + grade2 + grade3) / 3
        # Add name/average to lists
        studentgrades.append([student,avg])
        # Test for student name
        if student == 'Test' or  student == 'test' or student == 'TEST':
            teststudent = True
        # Get next input
        print('')
        student = input('Enter a student name (STOP to stop) ')
    # Evaluate student name test
    print('')
    if teststudent == True:
        print('test student seen')
    else:
        print('test student not seen')
    # Sort list of students
    studentgrades.sort()
    # Print list
    print()
    for i in range(len(studentgrades)):
        print(studentgrades[i][0] , '\t', round(studentgrades[i][1] , 2))
main()