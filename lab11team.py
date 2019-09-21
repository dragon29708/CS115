'''
Prologue
Title: Lists and Strings
Authors: Nahaba Hamada, Andrew Cassidy, John DeMoor
Emails: nkha229@uky.edu, arca248@uky.edu, john.demoor@uky.edu
Section: 3
Date: 4/15/19
Purpose: To write a program grading a multiple choice test (MCT) with 5 questions on it.
Preconditions: User first inputs the "KEY" (the answers, 5 in total) to the MCT being created; 
user types "END" to stop the entry of MCT data. Follwoing, user proceeds to typing the name(s)
of students and their 5 answers ranging from A-D, typing "END" again when he/she is finished.   
Postconditions: The data inputted by the user is processed and constructed into a list(s) 
containing the student's name and their selected multiple choice answers. First the key is posted,
followed by the aformentioned. The amount of correct answers is outputted to the screen in 
numerical and percentage form, followed by the the total amount of students and the 
computation of their average total answers correct.
'''
def main1():
	# Have user input a key. Afterwards, make a list for the key.
	key_input = input('Enter the KEY first, then 5 answers: ')
	key = key_input.split()
	print('Enter END to stop data entry')
	# Initialize the student list and sentinal value.
	student_list = []
	user_input = input('Enter Student Name first, then 5 answers: ')
	# While loop that appends the student list.
	while user_input != 'END':
		new_entry = user_input.split()
		student_list.append(new_entry)
		user_input = input('Enter Student Name first, then 5 answers: ')
	# Print the key and student list for the user.
	print('\nKey',key)
	print(student_list)
	print()
	# Initialize class total correct.
	class_total = 0
	# Grading contrl structure.
	for j in range(len(student_list)):
		total = 0
		for i in range(1,len(key)):
			if key[i] == student_list[j][i]:
				total += 1
		class_total += total
		print(student_list[j][0], 'got', total, 'right answers or', total * 100 / (len(key)-1), end=' %')
		print()
	print()
	# Average of the students
	if len(student_list) == 0:
		average = 0
	else:
		average = class_total / len(student_list)
	# Ending information.
	print('There were', len(student_list),'students')
	print('Average correct', round((average / (len(key)-1)) * 100,1), end=' %')
main1()