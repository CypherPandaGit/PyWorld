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

#------------------------------------


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
#-------------------------------------

import random

nums = [23, 43, 56, 87,24, 45, 93]
print(nums)

i = 0
while i < 10:
    ran = random.randint(1, 40)
    nums.append(ran)
    i += 1

print(nums)
