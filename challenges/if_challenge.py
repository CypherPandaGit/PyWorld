name = input(("What's your name? "))
age = int(input("What's your age {}? ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the 18-30 holiday, {}".format(name))
else:
    print("Sorry you can't go with us, {}".format(name))