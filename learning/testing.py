print("How many cats do you have?")
cats = input()

try:
    if int(cats) >= 4:
        print("That's a lot of cats.")
    else:
        print("That is not that many cats.")
except ValueError:
    print("You did not enter a number.")