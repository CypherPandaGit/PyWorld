import random
# This is a guessing game

print("Welcome in the guessing game")
print("----------------------------")
name = input("Please enter your name: \n")
print("Welcome {}.".format(name))

random_number = random.randint(1, 20)
print(random_number)
print("Please enter a number in range 1 - 20.")
user_number = int(input())

while user_number != random_number:
    print("That's not the number.")
    user_number = int(input())

else:
    print("YES that's the number.")