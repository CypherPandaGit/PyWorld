a = 10
print(id(a))


def something():
    a = 15

    x = globals()['a']
    print(id(x))
    print('this is inside ', a)

    globals()['a'] = 15


something()
print('and outside ', a)
