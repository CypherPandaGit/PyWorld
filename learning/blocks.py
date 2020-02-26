"""
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 50)
"""

name = input("Whats your name? ")
age = int(input("How old are you? "))
print(age)

if age >= 18:
    print("You are old enough")
else:
    print("Please come back in {0} years {1}".format((18 - age), name))
