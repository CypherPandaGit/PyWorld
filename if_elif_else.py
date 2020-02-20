name = input("What's your name? ")
age = int(input("How old are you? "))
print("You are {0} years old and".format(age))

if age <18:
    print("you can't vote {0}. Come back in {1} years.".format(name, 18 - age))
elif age >=120:
    print("eeeh, something is wrong, {0}?".format(name))
elif age >= 18:
    print("you can vote. Great!")