age = 24
year = 1988
print("My age is " + str(age) + " years")
print("My age is {0} years, born in {1}".format(age, year))

"""
print("How old are you?")
age2 = input()
print("And born in year?")
year2 = input()

print("You are {0} year old and born in year {1}.".format(age2, year2))
print()
"""

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print()

print("Honza ma {0} let, Barca {1}, Kaca {2}, Roman {0}, Vika {1}"
      .format(32, 28, 21))
print()

print("""Honza ma {0} let
Barca {1}
Kaca {2}
Roman {0}
Vika {1}""".format(32, 28, 21))