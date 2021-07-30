#Import random and mean from statistics
from statistics import mean
from random import randint

# Set the number of throws
throws = 1000

# Create empty list to hold the values
throwsList = []

# Create loop to throw the dice
for i in range(throws):
    throwsList.append(randint(1,6))

# Print the mean of the list
print(mean(throwsList))
