# spam = "Hello"
# spam = [10, 20 , 30]
#
# spam[1] = "Hello"
#
# print(spam)
#
# spam[1:3] = ['cat', 'dog', 'mouse']
#
# print(spam)

#------------------------------------

# spam = [10, 20, 30]
# print(spam)
# spam[1:3] = ["CAT", "MOUSE", "DOG"]
# print(spam)

#------------------------------------

# for i in range(4):
#     print(i)
#
# my_list = list(range(5))
# print(my_list)

#------------------------------------

# supplies = ['Apfel', 'Birne', 'Erdbeere', 'Himbeere']
# for i in range(len(supplies)):
#     print('Position {0} in supplies is: {1}'.format(str(i + 1), supplies[i]))
# 
# 
# size, color, disposition = 'skinny', 'brown', 'quiet'
# print(size, disposition, color)

#------------------------------------

# spam = ['Apfel', 'Birne', 'Erdbeere', 'Himbeere']
# print(spam.index('Erdbeere'))
# spam.append('Zimt')
# print(spam)
# spam.insert(0, 'Brombeere')
# print(spam)
# spam.remove('Birne')
# print(spam)
# del spam[3]
# print(spam)
# spam.sort()
# print(spam)

# ------------------------------------


# def eggs(someParameter):
#     someParameter.append('Hello')
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)


# ------------------------------------

# # LEGB RULE
#
# # LOCAL
# def report():
#     # LOCAL ASSIGNMENT!!!
#     x = 'local'
#     print(x)
#
# # ENCLOSING
# x = 'THIS IS GLOBAL LEVEL'
#
# def enclosing():
#     x = 'Enclosing level'
#
#     def inside():
#         print(x)
#
#     inside()
#
# # GLOBAL
# # BUILT IN

# -------------------------------------

# phone_ext = {'david':1456, 'brad':1145}
# print(phone_ext)
# print(list(phone_ext.keys()))
# print(phone_ext.values())
# print(list(phone_ext.values()))
# print('Hello Pikachu', end=' :)')

# counter = 1
# while counter <= 5:
#     print('Hi')
#     counter = counter + 1

# for item in [1, 2, 3, 4, 5]:
#     print(item**3)
#

# list=[]
#
# for i in range(1,11):
#     list.append(i * i)
#
# print(list)
#
# list_2=[i * i for i in range(1,11)]
# print(list_2)
# -------------------------------------

# import random

# nums = [23, 43, 56, 87,24, 45, 93]
# print(nums)

# i = 0
# while i < 10:
#     ran = random.randint(1, 40)
#     nums.append(ran)
#     i += 1

# print(nums)

# h = '#'
# i = 0
#
# for i in range(10):
#     print(h * (10 - i))
#     i += 1
# ------------------------------------------
# i = 1
#
# while i <= 5:
#     print('Ice cream ', end='')
#     j = 1
#     while j <= 5:
#         print('is good ', end='')
#         j += 1
#     i += 1
#     print()
# -------------------------------------------

# i = 0
#
# for i in range(1, 101):
#     if i%3 == 0:
#         continue
#     print(i)

# -------------------------------------------

# from array import *
#
# values = array('i', [5, 3, 7, -2, 9])
#
# new_values = array(values.typecode, (a for a in values))
#
# print(values)
# print(values.buffer_info())
# print(values.typecode)
#
# values.reverse()
# print(values)
#
# for i in range(len(values)):
#     print(values[i])

# -------------------------------------------

# from array import *
#
# # creating array
# arr = array('i', [])
#
# n = input('Please insert number of inputs: ')
#
# # inserting numbers to array
# for i in range(int(n)):
#     x = int(input('please insert value: '))
#     arr.append(x)
#
# print(arr)
#
#
# search = int(input('Search your number: '))
# k = 0
#
# # searching number through array
# for value in arr:
#     if value == search:
#         print(k)
#         break
#     k += 1
#
# print(arr.index(search))

# --------------------------------------------

# def person(name, **data):
#
#     print(name)
#
#     for i, j in data.items():
#         print(i, j)
#
#
# person('Roman', age=99, city='Wien', tel=438234567,)

# ---------------------------------------------

# def fib(f):
#
#     x = 0
#     y = 1
#
#     print(x)
#     print(y)
#
#     for i in range(2, f):
#         z = x + y
#         x = y
#         y = z
#         print(z)
#
#
# fib(10)

# ----------------------------------------------


# def div(a, b):
#     print(a / b)
#
#
# def smart_div(func):
#
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#
#     return inner
#
#
# div1 = smart_div(div)
#
# div1(2, 4)

# ------------------------------------------------

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 9
c1.com = "AUDI"
c2.mil = 23
c2.com = "JAGUAR"

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
