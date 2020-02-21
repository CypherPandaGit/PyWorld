# START Old code
#
# day = "Friday"
# temperature = 30
# raining = False
#
# if (day == "Saturday" and temperature > 27) and not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

# if 0:
#     print("True")
# else:
#     print("False")
#
# END Old code

name = input("Please enter your name: ")
# if name:
if name != "" and name != " ":
    print("Hello, {0}".format(name))
else:
    print("You are the man with no name?")