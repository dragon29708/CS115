# Prolog
# Author:  Andrew Cassidy
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Program 1

# Purpose: To create a resistor / current calculator for 2 separate arangements
# of resistors.

# Preconditions: Given 3 resistor values and a power value, determine the
# equivalent resistances for a series and parallel combination of the resistors.
# Also, calculate the current through both combiniations of resistors.

# Postconditions: Output to the user the equivalent resistance for a series and
# parallel combinations of the inputted resistors and also output their currents.
# Also, if they in a resistance of zero, output they have done so and set the
# parallel resistance to a very large number.

#from math library import square root function


# define main function:

# 1. display the title and author
#   print Resistor Calculations
#   print by Andrew Cassidy

# 2. asks user to input 3 resistor values in ohms
# r1 = float of input Enter the resistance of the first resistor (ohms)
# r2 = float of input Enter the resistance of the second resistor (ohms)
# r3 = float of input Enter the resistance of the third resistor (ohms)

# 3. ask user for the power for the three resistors
# power = float of input How much power (in watts)?
# print blank line

# 4. calculate equivalent resistance for a series combo of the 3 resistors
# req_series = sum the resistor values

# 5. a process that checks for division by zero when calculating parallel resistance
# if r1 = 0 or r2 = 0 or r3 = 0:
# print One of the resistors is zero. Parallel resistance set to 1e300
# req_parallel = 1e+300

# otherwise:  # 6. calculate equivalent resistance for a parallel combo of the 3 resistors
# req_parallel = (1 / r1 + 1 / r2 + 1 / r3) ** -1

# 7. output the equivalent resistance for both series and parallel combos
# print The resistance of these three resistors in series is: (rounded req_series to 3 decimals) ohms
# print The resistance of these three resistors in parallel is: (rounded req_parallel to 3 decimals) ohms
# print new line

# 8. calculate the current for both combos of resistors
# curr_series = square root of power divided by req_series

    # if req_parallel = 0:
        # then curr_parallel = 0
    # otherwise:
        # curr_parallel = square root of power divided by req_parallel

# 9. output current values

    # print The current in the circuit with the resistors in series is (rounded curr_series to 3 decimals) amps when the power is (output power) watts.
    # print The current in the circuit with the resistors in parallel is (rounded curr_parallel to 3 decimals) amps when the power is (ouput power) watts.


# main function call

# A-L Test Cases:

# A = 42.0
# B = 3.093
# C = 1.543
# D = 5.686
# E = 7.0
# F = 0.455
# G = 0.378
# H = 1.483
# I = 37.0
# J = 1e+300
# K = 1.644
# L = 0.0
