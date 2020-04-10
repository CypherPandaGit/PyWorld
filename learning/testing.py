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


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)


# ------------------------------------

# LEGB RULE

# LOCAL
def report():
    # LOCAL ASSIGNMENT!!!
    x = 'local'
    print(x)

# ENCLOSING
x = 'THIS IS GLOBAL LEVEL'

def enclosing():
    x = 'Enclosing level'

    def inside():
        print(x)

    inside()

# GLOBAL
# BUILT IN
