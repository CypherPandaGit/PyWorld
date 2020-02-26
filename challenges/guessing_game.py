import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Game over. You ended the game.")
        break
    if guess == answer:
        print("WOW, good job!")
        break
    else:
         if guess < answer:
             print("Please guess higher")
         else:
             print("Please guess lower.")