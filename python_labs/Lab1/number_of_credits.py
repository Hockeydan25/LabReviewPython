"""Write two programs for this lab. Dan Smestad prep for Cap Stone 11/19/2021.

1. Number of Credits Write a program that asks for your name, and the number of credits you are taking 
this semester. Print a message with this information, for example, 'Sam is taking 7 credits this 
semester' or 'Miriam is taking 9 credits this semester' """

#asking for data from the user. Users input will be the data for student_name and student_credits.
student_name = input('What is your name: ')
student_credits = input('tell me how many credits are you enrolled in this semester? ')
#print with f formatting variable name between mustash sybols will diplay input data from user 
print(f'Your name is {student_name} and your taking {student_credits} credits this semester.')

my_name = 'Mo'
my_name_twice = my_name + my_name
print(my_name)
print(my_name_twice)
my_name ='Dan'

print('One \nTwo \nThree')
print("She said, \"I'm learning Python,\" to me.")
print("Here is a tab \t Do you see it?")

number_of_cds = 45
number_of_lps = 23
number_of_albums = number_of_cds + number_of_lps
print(number_of_albums)

# here are two variables, of different types
college = 'MC'  # string data entered
number_of_cds = 3   # integer data entered

# nested functions 
print(type(college)) # adapt to see the type of the other variable

# Python IDs these as a float variables, even if it’s .0
temp_today = 35.0
coffee_price = 3.45
print(type(temp_today))
print(temp_today)
print(type(coffee_price))
print(coffee_price)

total = 999.99
print('Total wages = $' + str(total)) # OR
print('Total wages = $', total)

# Use rounding or formatting to control the look. Compare:
float_number = 12345.6789
float_number_rounded = round(12345.6789, 2)
print('Your number is', float_number_rounded) # easy! But no thousands separator
print(f'Your number is {float_number:,.2f}') # format code adds thousands separator & makes it look like it's rounded



