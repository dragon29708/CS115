# Prolog
# Author:  Andrew Cassidy, John DeMoor, Nahaba Hamada
# Email:   andrew.cassidy@uky.edu
# Section: 003

# CS 115 Lab 4 Group

# Purpose:

# Preconditions:

# Postconditions:


def main():

    print('Adventure!\n')

    print('You enter a room with 3 doors.')
# 1. set silver flag to False
    silver_flag = False
# 2. set ring flag to False
    ring = False
# 3. set lived flag to False
    lived_flag = False
# 4. display first prompt Door #1/#2/#3 - get user's first choice
    prompt1 = int(input('Do you take Door #1, Door #2, Door #3?\n> '))

# 6. if user chooses 1
    if prompt1 == 1:

        # a. display wolf prompt Run away/Attack
        print('You see a wolf! What do you do?')
        print('1. Run away')
        print('2. Attack the wolf')

    # b. get user's second choice
        ans_wolf = int(input('> '))

    # c. if user chooses 2
        if ans_wolf == 2:
            print('You got eaten!')


main()
