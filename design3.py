'''
Name: Andrew Cassidy
Email: andrew.cassidy@uky.edu
Title: Program 3
Preconditions: User chooses what they would like to do to the data
base. User keeps doing so until they enter Q to quit editing the
data base.
Postconditions: Use the get_choice function to output the main menu along with any
operation the user would like to perform on the database. These options are
loading files, saving files, editing the files and searching for records in 
files.

def get_choice():
	'''
	# Purpose: Display the menu, get the users choice, validate the choice, then return a string of what the user's choice was. 
	# Preconditions: No parameters. User will input a number 1-7 or 'Q'.
	# Postconditions: Validate if the user's choice is acceptible. If not, ask the user again. If it is good, return a string of the user's answer.
	'''
	Display the main menu.
	Get the users choice based off the main menu.
	Validate that the choice is legal.
	Return a string that is the uppercase letter of the user's choice.

def display(databaselist):
	'''
	# Purpose: Display the current database list in the format given in the project rubric.
	# Preconditions: Only parameter is the database list.
	# Postconditions: Displays the current database list. Does not return anything. 
	'''
	Display the database list in column form

def sort_list(databaselist):
	'''
	# Purpose: Sorts the database list in either ascending or descending order.
	# Preconditions: Only parameter is the database list. Asks user whether they want the list sorted in ascending or descending order
	# Postconditions: Sorts the list how the user asks. Does not return anything.
	'''
	Ask the user if they want the list in ascending or descending order.
	Sort the list in order given.
	Return the edited list that was inputted. Note: This means the database list should be edited.

def load():
	'''
	# Purpose: Load in the file that the user would like to be loaded in.
	# Preconditions: No parameters. User inputs the filename.txt that they would like to be loaded in.
	# Postconditions: Build a list from the file that was uploaded. Afterwards, return this list to the user.
	'''
	Ask the user for a filename.txt. Make sure to ask the user until a proper file name is chosen.
	Build the database list from the file name.
	Report list is loaded.
	Return the list

def save(databaselist):
	'''
	# Purpose: Save the current database list to a file provided by the user.
	# Preconditions: Only parameter is the database list. User inputs the file location of where they want the database saved to.
	# Postconditions: 
	'''
	Ask the user for a filename to save the database list to.
	Load the list data into the file with a proper dilimitor.

def newrecord(databaselist):
	'''
	# Purpose:
	# Preconditions:
	# Postconditions:
	'''
	Ask user for new ID number.
	If ID number already exists:
		ask for ID again.
	Ask user for information in the form: (first name, last name, department, supervisor).
	Append this info to the the database list.

def remove_record(databaselist):
	'''
	# Purpose: Delete a record from the database list. The user decides what record is deleted.
	# Preconditions: Only parameter is the database list. User inputs the ID number of the record they would like to remove.
	# Postconditions: Output to the user whether the record was or wasn't removed. Change the inputted list if a record is removed.
	'''
	Ask for the ID number of the record the user wants to remove.
	Search for the ID number.
	if ID is found:
		remove the record that contains the ID number.
		report the record was successfully removed.
	else:
		report failure to find the record and do not change the list.

def search_menu(databaselist):
	'''
	# Purpose: Create a menu that lets the user search for certain criteria in the database list.
	# Preconditions: Only parameter is the database list. User will input a string to compare with every element in the database list.
	# Postconditions: Output a list of all elements in the database list that satisfy the search string criteria. We do this by calling the search() function that is later defined.
	'''
	Output a field list for the user.
	Ask user which field they would like to search in.
	Validate the choice.
	Ask for the string to search for and validate it. Call the search function.
	Display the result of the search function.
	if the length of the resulting search list is non-empty:
		ask the user if they want to save the list as a separate file.
		if they want to save the list as a separate file:
			call the save function.

def search(search_string, databaselist, field number to search for):
	'''
	# Purpose: Build the new list that contains all records, from the database list, that fits the parameters inputted.
	# Preconditions: 3 parameters: the criteria string, the database list, and the field number to search for. User inputs all 3 of these.
	# Postconditions: Return a list, only consisting of elements from the correct field, that satisfies the search criteria.
	'''
	Build the new list.
	if the new list is empty:
		Return an empty list
	Return the list

def main():
	'''
	# Purpose: Runs the database program.
	# Preconditions: User will be inputting 1-7 to get to where they want to be in the program until they input 'Q' to quit.
	# Postconditions: Program will run all individual function that accomplish what the user wants based of their numerical input.
	'''
	user_input = get_choice()
	initialize the database list
	while user_input does not equal 'Q':
		if user_input is 1:
			call the load() function
		elif user_input is 2:
			call the save() function with the database list.
		elif user_input is 3:
			call the new_record() function with the database list.
		elif user_input is 4:
			call the remove_record() function with the database list.
		elif user_input is 5:
			call the search() function with its required parameters.
		elif user_input is 6:
			call the sort_list() function.
		else: user_input is 7 if the else is triggered.
			call the display() function with the database list.
    	user_input = get_choice()
main()
'''