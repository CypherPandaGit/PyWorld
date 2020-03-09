# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 100, 2))
# odd = list(range(1, 100, 2))
#
# print(even)
# print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)

print(small_decimals.index(3))

odd = range(1, 10000, 2)
print(odd)

print(odd[985])

sevens = range(7, 100000, 7)
x = int(input("Please enter a positive number less than a one million: "))
if x in sevens:
    print("{} is divisible by 7".format(x))