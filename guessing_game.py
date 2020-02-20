answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
     if guess < answer:
         print("Please guess higher")
     else:
         print("Please guess lower.")
     guess = int(input())
     if guess == answer:
         print("Well done!")
     else:
         print("Sorry, wrong. :(")
else:
    print("WOW, good job!")
       

# OLD CODE
# if guess < answer:
#     print("You need more.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Sorry, wrong.")
# elif guess > answer :
#     print("You need less")
#     guess = int(input())
#     if guess == answer:
#         print("Well done!")
#     else:
#         print("Sorry, wrong.")
# else:
#     print("Good job!")

