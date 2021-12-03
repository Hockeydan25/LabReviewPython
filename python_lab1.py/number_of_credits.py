"""Write two programs for this lab. Dan Smestad prep for Cap Stone 11/19/2021.

1. Number of Credits Write a program that asks for your name, and the number of credits you are taking 
this semester. Print a message with this information, for example, 'Sam is taking 7 credits this 
semester' or 'Miriam is taking 9 credits this semester' """

#asking for data from the user. Users input will be the data for student_name and student_credits.
student_name = input('What is your name: ')
student_credits = input('tell me how many credits are you enrolled in this semester? ')
#print with f formatting variable name between mustash sybols will diplay input data from user 
print(f'Your name is {student_name} and your taking {student_credits} credits this semester.') 