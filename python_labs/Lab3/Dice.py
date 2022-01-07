"""Question 1: Dice (5 points)

Modify the while loop dice rolling program (this one:https://git.io/fh7qn) so it rolls two dice 
at the same time, and prints both dice values. The program should let the user roll the dice as 
many times as they want, until they want to quit. 

In some games, it matters if both dice roll the same value. In your loop, check if both dice 
were the same value. Print a message if so. (for example: "Both dice are the same!" or "you rolled 
doubles!")

Hint: for this one, you don't need to add any new loops to this program.

Extra credit question: ask the user for the number of dice to roll. Roll that many dice and 
print each dice value. Figure out if they all have the same value. For example, the user may 
wish to to roll 3 dice. If the dice values are 4, 5, 2, they are not all the same. If the dice 
values are 4, 4, 4, the are all the same, print a message saying they are all the same. 
You can do this using the things you've learned so far.  Another way is to use a list to store 
all the dice values but we haven't covered these yet, although we will soon.   +4 points.   """

import random

want_to_quit = ''
# while not want_to_quit:
#     dice_value1 = random.randint(1, 6) #creates random dice number range 1 to 6.
#     print(f'You rolled a {dice_value1}') #prints to user the dice roll random created.
#     want_to_quit = input('Press enter to roll again, any other key to quit ') #ask user for input.

# adds two dice without user prompt
# while not want_to_quit:
#     dice_value1 = random.randint(1, 6) #creates random dice number range 1 to 6.
#     dice_value2 = random.randint(1, 6) #creates random dice number range 1 to 6.
#     print(f'You rolled a {dice_value1}, {dice_value2}') #prints to user the dice roll random created.
#     if dice_value1 == dice_value2:  # special roll condition.
#         print(f'You rolled doubles, nice!')
#     else:
#         want_to_quit = input('Press enter to roll again, any other key to quit ') #ask user for input.

#ask the user for the number of dice to roll.
while not want_to_quit:
    dice_value1 = random.randint(1, 6) #creates random dice number range 1 to 6.
    dice_value2 = random.randint(1, 6) #creates random dice number range 1 to 6.
    print(f'You rolled a {dice_value1}, {dice_value2}') #prints to user the dice roll random created.
    if dice_value1 == dice_value2:  # special roll condition.
        print(f'You rolled doubles, nice!')
    else:
        want_to_quit = input('Press enter to roll again, any other key to quit ') #ask user for input.


    
    