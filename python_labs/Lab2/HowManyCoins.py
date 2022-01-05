"""  Question 1: 

Do you have a dollar?

Write a program that asks the user how many cents (penny coins) they have.

If they have less than 100 cents, print the message 'you have less than a dollar'. 
If they have exactly 100 cents, print the message 'you have exactly one dollar'
If they have more than 100 cents, print the message 'you have more than one dollar'
(Bonus question, +3 points: extend your program to check if the user has an exact 
number of dollars in cents (penny coins), for example 100 or 300 or 700 pennies. 
Print a message if so. Hint: look up the modulo % operator. It's covered in 
Chapter 1 of the textbook.)

"""
'Hello and welcome to my penny counter program.'
total = 1
pennies = 1
pennies = float(input('How many Pennies do you have?: '))
if pennies <= 99:
    print('you have less than one dollar.)
elif pennies == 100:
    print('you have exactly one dollar.)
elif pennies == 200:
    print('you have exactly two dollars.)
elif pennies == 700:
    print('you have exactly seven dollars.)    
else:     
    print('you have more than one dollar.)




