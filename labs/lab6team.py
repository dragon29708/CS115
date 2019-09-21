# Name: John DeMoor, Andrew Cassidy, Nahaba Hamada
# Section: 3
# Email: john.demoor@uky.edu

# Purpose: Dice game that compares two players' rolls.

# Preconditions: The names of the two players and how many rounds to play.

# Postconditions: Which player has the more even roles for each round, how many
# rounds each player won.


def main():

    # Import random function
    import random
    random.seed(25)

    # Input first player's name
    player1 = input('Player 1 name? ')

    # Input second player's name
    player2 = input('Player 2 name? ')

    # Input number of rounds
    rounds = int(input('How many rounds to play? '))

    # Define main loop
    for i in range(1, rounds + 1):

        # Define rolls
        roll11 = random.randrange(1, 13)
        roll12 = random.randrange(1, 13)
        roll13 = random.randrange(1, 13)
        roll21 = random.randrange(1, 13)
        roll22 = random.randrange(1, 13)
        roll23 = random.randrange(1, 13)

        # Print rounds/rolls
        print()
        print('Round', i)
        print(player1, 'rolls: ', end='')
        print(roll11, roll12, roll13)
        print(player2, 'rolls: ', end='')
        print(roll21, roll22, roll23)

        # Find even rolls
        if (roll11 % 2) == 0 and (roll12 % 2) == 0 and (roll13 % 2) == 0:
            evenrolls1 = 3
        elif (roll11 % 2) == 0 and (roll12 % 2) == 0 and (roll13 % 2) != 0:
            evenrolls1 = 2
        elif (roll11 % 2) == 0 and (roll13 % 2) == 0 and (roll12 % 2) != 0:
            evenrolls1 = 2
        elif (roll13 % 2) == 0 and (roll12 % 2) == 0 and (roll11 % 2) != 0:
            evenrolls1 = 2
        elif (roll11 % 2) == 0 and (roll12 % 2) != 0 and (roll13 % 2) != 0:
            evenrolls1 = 1
        elif (roll12 % 2) == 0 and (roll13 % 2) != 0 and (roll11 % 2) != 0:
            evenrolls1 = 1
        elif (roll13 % 2) == 0 and (roll12 % 2) != 0 and (roll11 % 2) != 0:
            evenrolls1 = 1
        elif (roll11 % 2) != 0 and (roll12 % 2) != 0 and (roll13 % 2) != 0:
            evenrolls1 = 0
        print(player1, 'has ', end='')
        print(evenrolls1, 'even rolls')

        if (roll21 % 2) == 0 and (roll22 % 2) == 0 and (roll23 % 2) == 0:
            evenrolls2 = 3
        elif (roll21 % 2) == 0 and (roll22 % 2) == 0 and (roll23 % 2) != 0:
            evenrolls2 = 2
        elif (roll21 % 2) == 0 and (roll23 % 2) == 0 and (roll22 % 2) != 0:
            evenrolls2 = 2
        elif (roll23 % 2) == 0 and (roll22 % 2) == 0 and (roll21 % 2) != 0:
            evenrolls2 = 2
        elif (roll21 % 2) == 0 and (roll22 % 2) != 0 and (roll23 % 2) != 0:
            evenrolls2 = 1
        elif (roll22 % 2) == 0 and (roll23 % 2) != 0 and (roll21 % 2) != 0:
            evenrolls2 = 1
        elif (roll23 % 2) == 0 and (roll22 % 2) != 0 and (roll21 % 2) != 0:
            evenrolls2 = 1
        elif (roll21 % 2) != 0 and (roll22 % 2) != 0 and (roll23 % 2) != 0:
            evenrolls2 = 0
        print(player2, 'has ', end='')
        print(evenrolls2, 'even rolls')

        # Determine winner
        if evenrolls1 > evenrolls2:
            print(player1, 'won!')
        elif evenrolls2 > evenrolls1:
            print(player2, 'won!')
        elif evenrolls1 == evenrolls2:
            print('It is a tie!')


main()
