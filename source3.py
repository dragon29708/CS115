'''
Name: Andrew Cassidy
Email: andrew.cassidy@uky.edu
Title: Program 3
Preconditions: User chooses what they would like to do to the data
base. User keeps doing so until they enter Q to quit editing the data base.
Postconditions: Use the get_choice function to output the main menu along with any
operation the user would like to perform on the database. These options are
loading files, saving files, editing the files and searching for records in files.
'''


def get_choice():
    '''
    Purpose: Display the menu, get the users choice, validate the choice, then return a string
    of what the user's choice was.
    Preconditions: No parameters. User will input a number 1-7 or 'Q'.
    Postconditions: Validate if the user's choice is acceptible. If not, ask the user again.
    If it is good, return a string of the user's answer.
    '''
    # Display the main menu.
    print('\nMain Menu\n')
    print('1. Load database')
    print('2. Save database')
    print('3. Enter new record')
    print('4. Delete existing record')
    print('5. Search database')
    print('6. Sort by key (ID) field')
    print('7. Display database')
    print('Q. Quit')
    # Get the users choice based off the main menu.
    choice = input('\n> ')
    if choice == 'q':
        choice = 'Q'
    num = False
    # Validate that the choice is legal.
    while choice != 'Q' and num == False:
        # Change choice to an integer if its not the sentinal variable.
        choice = int(choice)
        if choice < 1 or choice > 7:
            print('Invalid Entry. Choose a number in range 1-7 or type Q to quit.')
            choice = input('> ')
        else:
            num = True
        if choice == 'q':
            choice = 'Q'
    # Return a string that is the uppercase letter of the user's choice.
    return choice


def display(dlist):
    '''
    Purpose: Display the current database list in the format given in the project rubric.
    Preconditions: Only parameter is the database list.
    Postconditions: Displays the current database list. Does not return anything.
    '''
    # Display the database list in column form
    print('-' * 55)
    colname = ['ID', 'Employee Name', 'Department', 'Supervisor']
    print(colname[0], colname[1], colname[2], colname[3], sep='\t')
    print()
    for i in range(len(dlist)):
        print(dlist[i][0], dlist[i][1] + ' ' + dlist[i][2], dlist[i][3], dlist[i][4], sep='\t')
    print('-' * 55)


def sort_list(dlist):
    '''
    Purpose: Sorts the database list in either ascending or descending order.
    Preconditions: Only parameter is the database list. Asks user whether they
    want the list sorted in ascending or descending order.
    Postconditions: Sorts the list how the user asks. Does not return anything.
    '''
    # Ask the user if they want the list in ascending or descending order.
    user_input = input('Ascending or Descending? (a/d) ')
    # Sort the list in order given.
    dlist.sort()
    if user_input == 'd':
        dlist.reverse()


def load():
    '''
    Purpose: Load in the file that the user would like to be loaded in.
    Preconditions: No parameters. User inputs the filename.txt that they would like to be loaded in.
    Postconditions: Build a list from the file that was uploaded. Afterwards, return this list to the user.
    '''
    # Ask the user for a filename.txt.
    fn = input("Enter a filename ")
    IOok = False
    # Validate file name until a proper file name is chosen.
    while not IOok:
        try:
            infile = open(fn, 'r')
            IOok = True
        except IOError:
            print('Error, file would not open.')
            fn = input('Enter a filename ')
    # Build the database list from the file name.
    lst = []
    lineno = 1
    for line in infile:
        # Remove newline (and other trailing whitespace)
        line = line.rstrip()
        row_i = line.split(',')
        lst.append(row_i)
        lineno += 1
    # Free the resources associated with the file object.
    infile.close()
    # Report list is loaded.
    print('File loaded.')
    # Return the list
    return lst


def save(dlist):
    '''
    Purpose: Save the current database list to a file provided by the user.
    Preconditions: Only parameter is the database list. User inputs the file location of where
    they want the database saved to.
    Postconditions: Validate if file can be saved. Then, save database list to file and report
    when done.
    '''
    # Ask the user for a filename to save the database list to.
    fn = input("Enter a filename ")
    # Check if the inputted file name will open to write.
    IOok = False
    while not IOok:
        try:
            infile = open(fn, 'w')
            IOok = True
        except IOError:
            print('Error, file does not exist.')
            fn = input('Enter a filename ')
    # Save dlist to the file.
    for i in range(len(dlist)):
        line_string = ','.join(dlist[i])
        line_string += '\n'
        infile.write(line_string)
    # Free the resources associated with the file object.
    infile.close()
    # Report list is saved.
    print('File saved.')


def new_record(dlist):
    '''
    Purpose: Append a new employee record to the database list.
    Preconditions: User inputs a new ID number. After ID validation, user is asked
    for: (first name, last name, department, supervisor).
    Postconditions: Program appends the inputted record to the database list.
    '''
    # Ask user for new ID number.
    print('Enter new ID number:')
    id_num = input('> ')
    # Create a list of the ID numbers
    id_list = []
    for i in dlist:
        id_list.append(i[0])
    # If ID number already exists:
    while id_num in id_list:
        # Ask for ID again.
        print('ID number invalid. Enter new ID number:')
        id_num = input('> ')
    # Ask user for information in the form: (first name, last name, department, supervisor).
    print('Enter in information in form: (first name, comma, last name, comma, department, comma, supervisor)')
    lst = input('> ')
    lst = id_num + ',' + lst
    # Append this info to the the database list.
    dlist.append(lst.split(','))


def remove_record(dlist):
    '''
    Purpose: Delete a record from the database list. The user decides what record is deleted.
    Preconditions: Only parameter is the database list. User inputs the ID number of the record
    they would like to remove.
    Postconditions: Output to the user whether the record was or wasn't removed.
    Change the inputted list if a record is removed.
    '''
    # Ask for the ID number of the record the user wants to remove.
    print('Enter ID number to delete:')
    id_num = input('> ')
    # Search for the ID number.
    id_list = []
    for i in dlist:
        id_list.append(i[0])
    # If ID is found:
    if id_num in id_list:
        # Remove the record that contains the ID number.
        i = id_list.index(id_num)
        del dlist[i]
        # Report the record was successfully removed.
        print('Record successfully removed.')
    else:
        print('Failure to find ID number in records.')


def search(search_string, dlist, col_num):
    '''
    Purpose: Build a new list that contains all records, from the database list, that fits the parameters inputted.
    Preconditions: 3 parameters: the criteria string, the database list, and the field number
    to search for. User inputs all 3 of these.
    Postconditions: Return a list, only consisting of elements from the correct field,
    that satisfies the search criteria.
    '''
    # Build the new list.
    lst = []
    # Build a list of all elements from the column wanted.
    col_lst = []
    for i in dlist:
        col_lst.append(i[col_num])
    # Append the new list with all records that match the search string.
    for j in range(col_lst.count(search_string)):
        index = col_lst.index(search_string)
        lst.append(dlist[index])
        col_lst.insert(index, 'Empty')
        col_lst.remove(search_string)
    # Return the list
    return lst


def search_menu(dlist):
    '''
    Purpose: Create a menu that lets the user search for certain criteria in the database list.
    Preconditions: Only parameter is the database list. User will input a string to compare with
    every element in the database list.
    Postconditions: Output a list of all elements in the database list that satisfy the search
    string criteria. We do this by calling the search() function that is later defined.
    '''
    # Output a field list for the user.
    print('Search Menu\n')
    print('0. Key (ID)')
    print('1. First name')
    print('2. Last name')
    print('3. Department')
    print('4. Supervisor\n')
    # Ask user which field they would like to search in.
    col_num = int(input('> '))
    # Validate the choice.
    while col_num < 0 or col_num > 4:
        print('Invlad input. Enter a number 0-4: ')
        col_num = int(input('> '))
    # Ask for the string to search for and validate it. Call the search function.
    search_string = input('\nString to search for? ')
    lst = search(search_string, dlist, col_num)
    # Display the result of the search function.
    display(lst)
    # if the length of the resulting search list is non-empty:
    if lst != []:
        # ask the user if they want to save the list as a separate file.
        save_q = input('Do you want to save this as a separate file? (y/n) ')
        # if they want to save the list as a separate file:
        if save_q == 'y':
            # call the save function.
            save(lst)


def main():
    '''
    Purpose: Runs the database program.
    Preconditions: User will be inputting 1-7 to get to where they want to be in the program
    until they input 'Q' to quit.
    Postconditions: Program will run all individual function that accomplish what the user
    wants based of their numerical input.
    '''
    # Initialize the database and input history lists.
    dlist = []
    input_his = []
    # Start up program
    user_input = get_choice()
    # Initialize the database list.
    while user_input != 'Q':
        if user_input == 1:
            dlist = load()
        elif user_input == 2:
            save(dlist)
        elif user_input == 3:
            new_record(dlist)
        elif user_input == 4:
            remove_record(dlist)
        elif user_input == 5:
            search_menu(dlist)
        elif user_input == 6:
            sort_list(dlist)
        else:
            display(dlist)
        input_his.append(user_input)
        user_input = get_choice()
    # If the user has entered 'Q' and has not saved their file:
    if 2 not in input_his:
        save_q = input('File is not saved.  Save? (y/n) ')
        if save_q == 'y':
            save(dlist)
    # Prompt that the program is over.
    print('Database closed.')


main()
