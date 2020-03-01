name = ""

while True:
    name = input("Please enter your name: ")

    if name == "Roman":
        break

    print("That's not your name, {}.".format(name))
print("That's your name.")