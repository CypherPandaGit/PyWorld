answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("You need more.")
elif guess > answer :
    print("You need less")
else:
    print("Good job!")