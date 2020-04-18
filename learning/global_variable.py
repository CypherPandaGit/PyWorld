a = 10


def something():
    global a

    a = 15

    print('this is inside ', a)


something()
print('and outside ', a)
