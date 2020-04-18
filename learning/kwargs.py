# KEYWORDED VARIABLE LENGTH ARGUMENTS *KWARGS


def person(name, **data):

    print(name)

    for i, j in data.items():
        print(i, j)


person('Roman', age=99, city='Wien', tel=438234567,)
