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

from math import sqrt


def main():

    # 1. display the title and author
    print('\tResistor Calculations')
    print('\t  by Andrew Cassidy\n')

# 2. asks user to input 3 resistor values in ohms
    r1 = float(input('Enter the resistance of the first resistor (ohms): '))
    r2 = float(input('Enter the resistance of the second resistor (ohms): '))
    r3 = float(input('Enter the resistance of the third resistor (ohms): '))

# 3. ask user for the power for the three resistors
    power = float(input('How much power (in watts)? '))
    print()

# 4. calculate equivalent resistance for a series combo of the 3 resistors
    req_series = r1 + r2 + r3

# 5. a process that checks for division by zero when calculating parallel resistance
    if r1 == 0 or r2 == 0 or r3 == 0:
        print('One of the resistors is zero. Parallel resistance set to 1e300')
        req_parallel = 1e+300

    else:  # 6. calculate equivalent resistance for a parallel combo of the 3 resistors
        req_parallel = (1 / r1 + 1 / r2 + 1 / r3) ** -1

# 7. output the equivalent resistance for both series and parallel combos
    print('The resistance of these three resistors in series is:', round(req_series, 3), 'ohms')
    print('The resistance of these three resistors in parallel is:', round(req_parallel, 3), 'ohms\n')

# 8. calculate the current for both combos of resistors
    curr_series = sqrt(power / req_series)

    if req_parallel == 0:
        curr_parallel = 0
    else:
        curr_parallel = sqrt(power / req_parallel)

# 9. output current values

    print('The current in the circuit with the resistors in series is', round(curr_series, 3), 'amps when the power is', power, 'watts.')
    print('The current in the circuit with the resistors in parallel is', round(curr_parallel, 3), 'amps when the power is', power, 'watts.')


main()
