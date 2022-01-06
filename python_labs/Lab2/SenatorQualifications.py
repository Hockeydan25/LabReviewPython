""" Question 2:
Can you be a senator?

Article I, Section 3 of the Constitution sets out three qualifications for senators:

(1) they must be at least 30 years old,
(2) they must have been citizens of the United States for at least the past nine years, and
(3) they must live in the state they seek to represent at the time of their election.

Write a program that asks the user four questions:

the state they want to be a senator in,
their age, as an int number,
if they have been a citizen of the US for at least 9 years. If someone is not a US citizen, they will enter 0,
the state they currently live in.  (to be eligible, this needs to be the same as the state they want to be 
the senator of). """

print('Welcome, please answer the following Questions for your pursuit in becoming a US State Senator')
while True:
    age = int(input('Are you at least 30 years old. Please enter your cureent age, numbers only: '))
    if age < 30:
        print('Sorry you must be at least 30 years old')
        break     
    citizen = input('Have you been a US citizen for at least 9 years? please type only: "y" or "n" ')
    if citizen == 'n':
        print('Sorry you must be citizens of the United States for at least the past nine years.')
        break
    else:    
        print('Great, let\'s continue.')
    stateResident = input('Please type your current State residance, only the two letter state code, CAPITALIZED:  ')    
    if stateResident == 'MN': #not validating for the caps.
        print('great you\'re a Minneasota resident.') 
        print('Congratulations you meet all the requirements!')
        break
    else:   
        print('Sorry you must live in the state you are seeking to represent at the time of your election.')
        break
    
print('Questionire Done.')    