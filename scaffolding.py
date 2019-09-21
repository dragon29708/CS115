#---------------------------------------------------------------------------
# To use this:  comment out the call to main and put this code (all of it)
#  at the bottom of your .py file.
#  choose which test or tests are run by setting that boolean to True
#   just uncomment it and comment out the line setting it to False
# NOTE: your function names MUST match what the assignment gives!
#---------------------------------------------------------------------------

#### TESTING
            
#test_display = True
test_display = False 
#test_sort_list = True
test_sort_list = False
#test_load = True
test_load = False
#test_save = True
test_save = False
#test_search_menu = True
test_search_menu = False
#test_search = True
test_search = False
#test_newrecord = True
test_newrecord = False
#test_remove_record = True
test_remove_record = False


if test_display:
    print("***********************************************display")
    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['1112', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['1113', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1120', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("testing display, with 4 employees")
    display(dblist)
    
    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("testing display, with 1 employee")
    display(dblist)
    
    dblist = []
    print("testing display, with 0 employees")
    display(dblist)


if test_sort_list:
    print("***********************************************sort_list")
    dblist = []
    print("Sorting with 0 employees\n")
    print("Give Ascending as input")
    print("Before sort",dblist)
    sort_list(dblist)
    print("After sort",dblist)

    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("\nSorting with one employee\n")
    print("Give Ascending as input")
    print("Before sort",dblist)
    sort_list(dblist)
    print("After sort",dblist)
   
    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("\nSorting with one employee\n")
    print("Give Descending as input")
    print("Before sort",dblist)
    sort_list(dblist)
    print("After sort",dblist)


    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]

    print("\nSorting with 4 employees\n")
    print("Give Descending as input")
    print("Before sort",dblist)
    sort_list(dblist)
    print("After sort",dblist)


    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]

    print("\nSorting with 4 employees\n")
    print("Give Ascending as input")
    print("Before sort",dblist)
    sort_list(dblist)
    print("After sort",dblist)

if test_load:
    print("***********************************************load")
    print("\nGive filename that exists")
    table = load()
    print("After load, table is", table)

    print("\nGive filename that does not exist, then one that exists")
    table = load()
    print("After load, table is", table)

    print("\nGive filename that exists but is empty")
    table = load()
    print("After load, table should be empty, table is", table)


if test_save:
    print("***********************************************save")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Saving with 4 employees")
    print("Before save, list is", dblist)
    save(lst)
    print("After save, list is", dblist)
    print("Check your output file, should have 4 lines")

    dblist = []
    print("Saving with 0 employees")
    print("Before save, list is empty", dblist)
    save(lst)
    print("After save, list is", dblist)
    print("Check your output file, should be empty")


    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Saving with 1 employee")
    print("Before save, list is", dblist)
    save(lst)
    print("After save, list is", dblist)
    print("Check your output file, should have 1 line")


if search_menu:
    print("***********************************************search_menu")
    print("Choose 0 and 2222 and N")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for 2222 as ID", result)
    print("result should be ['2222','John','Smith','Purchasing','Ron Sloan']\n")

    print("Choose 0 and 5555")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for 5555 as ID", result)
    print("result should be []\n")

    print("Choose 1 and Mary and n")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Mary as First Name", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']]\n")

    print("Choose 1 and Sue")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Sue as First Name", result)
    print("result should be []\n")
     
    print("Choose 2 and Brown and N")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Brown as Last Name", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'] ]\n")

    print("Choose 2 and Black")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Black as Last Name", result)
    print("result should be []\n")

    print("Choose 3 and Purchasing and Y and a filename")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Purchasing as Department", result)
    print("result should be [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']]\n")

    print("Choose 3 and Administration")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Administration as Department", result)
    print("result should be []\n")

    print("Choose 4 and Bob Wallen and y and a filename")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Bob Wallen as Supervisor", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']] \n")

    print("Choose 4 and Brian Kramer")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Brian Kramer as Supervisor", result)
    print("result should be []\n")

    print("Choose 9 and 4 and Ron Sloan and n")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Ron Sloan as Supervisor", result)
    print("result should be [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']]\n")

if test_search:
    print("***********************************************search")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Searching for 4444 as ID")
    result = search ("4444", dblist, 0)
    print("result is", result)
    print("result should be ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']\n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Searching for 6666 as ID")
    result = search ("6666", dblist, 0)
    print("result is", result)
    print("result should be []\n")

    dblist = []
    print("Searching for 6666 as ID in empty list")
    result = search ("6666", dblist, 0)
    print("result is", result)
    print("result should be []\n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search("Bob Wallen", dblist, 4)
    print("Result of search for Bob Wallen as Supervisor", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']] \n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search("Brian Kramer", dblist, 4)
    print("Result of search for Brian Kramer as Supervisor", result)
    print("result should be []\n")

    dblist = []
    result = search("Bob Wallen", dblist, 4)
    print("Result of search for Bob Wallen as Supervisor in an empty list", result)
    print("result should be []\n")


if test_newrecord:
    print("***********************************************newrecord")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(lst)
    print("After new record added", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 4444 then 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(lst)
    print("After new record added", dblist)

    dblist = []
    print("Adding to an empty list")
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(lst)
    print("After new record added", dblist)

    print("Adding to a list with 1 employee")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(lst)
    print("After new record added", dblist)


if test_remove_record:
    print("***********************************************remove_record")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 1111")
    print("Before record removed", dblist)
    remove_record (dblist)
    print("After record removed", dblist)
    
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record at the end of the list")
    print("Enter 1111")
    print("Before record removed", dblist)
    remove_record (dblist)
    print("After record removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record not in list")
    print("Enter 5555")
    print("Before record removed", dblist)
    remove_record (dblist)
    print("After record not removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
        ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
        ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
        ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record at the front of the list")
    print("Enter 2222")
    print("Before record removed", dblist)
    remove_record (dblist)
    print("After record removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Removing a record from list with 1 employee")
    print("Enter 2222")
    print("Before record removed", dblist)
    remove_record (dblist)
    print("After record removed", dblist)
