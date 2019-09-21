'''
Prologue -
Name: Andrew Cassidy
Email: andrew.cassidy@uky.edu
Title: Program 3
Preconditions:
Postconditions:
'''

def get_choice():

def display(dlist):

def sort_list(dlist):

def load():
	    openOk = False
    # The flag starts out false, so the loop runs at least once.
    while not openOk:
        try:
            # Get a filename and try to open it
            fn = input("Enter a file name: ")
            infile = open(fn, "r")
            # If we got here, open succeeded.
            openOk = True
        except IOError:
            print("Could not open", fn)
    # If we got here, we know it successfully opened.
    # Now fn is the filename and infile the file object.
    # Create a 2D list that stores the values of the lines.
    lst = []
    lineno = 1
    for line in infile:
        # Remove newline (and other trailing whitespace)
        line = line.rstrip()
        lst.append([line])
        lineno += 1
    # Free the resources associated with the file object.
    infile.close()
def save(dlist):

def newrecord():

def remove_record():

def search_menu():

def search():

def main():
	'''
	Function that runs the program
	'''
	# Initialize the database list
	dlist = []
	# Program start!
	get_choice()
main()
