# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# Purpose: calculate the area of a trapezoid, given measures from the user
#           and provided formula
# Preconditions (inputs): two bases and height of a trapezoid (as floats)
# Postconditions (output): prompts for inputs and output of area of trapezoid (as float)
#           area rounded to 2 places

def main():
    
#Design: (Pseudocode)
   
   #1. Display title
    print("Trapeziod Area Calculator")
   
   #2. Display blank line
    print()
   
   #3. Input the two bases
    base1 = float(input("Input Base 1 = "))
    base2 = float(input("Input Base 2 = "))
   
   #4. Input the height
    height = float(input("Input Height = "))
   
   #5. Display blank line
    print()
   
   #6. Calculate the area of the trapezoid
    total_area = ((base1 + base2) / 2) * height 
   
   #7. Display the area with a label "The area of the trapezoid is", rounded to 2 places
    print("Total Area is", total_area)

main()

# A = 43.75 
# B = 43.75
# C = 62.5
# D = .5
# E = 1
