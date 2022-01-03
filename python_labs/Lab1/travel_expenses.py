"""  Dan Smestad prep for Cap Stone 11/19/2021.
Travel Expenses Write a program that calculates the amount of money spent on bus fares last month.

Ask the user for the number of times they rode the bus last month
Ask the user for the cost of one bus ride 
Multiply these numbers to calculate the total cost of riding the bus. 
Print the number of rides, the cost of one bus ride, and the total cost for the user. 
For this problem, you can ignore transfers, and rush-hour fares, and just assume every bus ride 
costs the same. 

Example output would look like this:'You rode the bus 8 times last month. One bus ride costs $2. 
Your total cost was $16' or 'You rode the bus 3 times last month. One bus ride costs $1.75. 
Your total cost was $5.25. """

#asking for data from the user. Users input will be the data for ride_count and ride_cost.
ride_count= int(input('How many times did you ride the bus last month? '))
ride_cost = float(input('How much did you pay for each ride? '))
#calculating the cost of the mnthly expense to ride the bus
mntly_bus_cost = ride_count * ride_cost
#print message for users travel expenses. not sue how far this line can extend out. 
print(f'You rode the bus {ride_count} times and each time you rode the buys it cost you ${ride_cost}, your monthly expense = ${mntly_bus_cost}.')

