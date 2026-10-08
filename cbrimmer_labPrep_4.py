# Carter Brimmer
# 9/16/26
# "Lab-prep assignment - week 4"


# 1. For loop

total = 0

for i in range(5):
    number = float(input("Enter a positive number: "))
    total += number

average = total / 5

print("Total: {:.2f}".format(total))
print("Average: {:.2f}".format(average))


# 2. While loop

import random

random_number = random.randint(1, 5)
guess = 0
attempts = 0

while guess != random_number:
    guess = int(input("Guess a number between 1 and 5: "))
    attempts += 1

print("Correct!")
print("Number of attempts:", attempts)
