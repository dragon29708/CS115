# Prolog
# Author:  Andrew Cassidy, John DeMoor, Nahaba Hamada
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 3 (Team)

# Purpose - Given the diameter of a wafer and a pre-decided area for each chip
# that is cut out of the wafer, compute the area of the wafer and how many chips
# can be cut from the wafer.

# Preconditions - Both the diameter of the wafer and the area of each chip are
# converted into floats, which we will use to compute the area of the wafer and
# the amount of chips that can be made from the wafer with specific area per chip.

# Postconditions - The outputs sent to the screen are the amount of chips that
# are made from a wafer and the area of the wafer.

# Import math library to use sqrt and pi
from math import pi, sqrt

# Main function


def main():

    # 1. Display introductory message
    print('            000 Slicing Wafers 000\n')

    # 2. Ask user for diameter of wafer
    wafer_diameter = float(input('What is the diameter of the wafer? (in mm) '))

    # 3. Ask user for desired area of a chip
    desired_chip_area = float(input('What is the area of a single chip? (in mm^2) '))

    # 4. Calculate the area of the wafer using the formula for area of a circle
    wafer_area = pi * (wafer_diameter / 2) ** 2

    # 5. Calculate the number of chips that can be cut from  a wafer using formula given
    chips_per_wafer = int((wafer_diameter * pi) * ((wafer_diameter / (4 * desired_chip_area)) - (1 / sqrt(2 * desired_chip_area))))

    # 6. Output a blank line
    print()

    # 7. Output the area of the wafer
    print('From a circular wafer with area', round(wafer_area, 2), 'square millimeters')

    # 8. Output the (integer) number of chips cut from the wafer
    print('you can cut', chips_per_wafer, 'chips, each with area', desired_chip_area, 'square millimeters')

main()
