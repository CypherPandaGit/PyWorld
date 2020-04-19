def fib(f):

    x = 0
    y = 1

    print(x)
    print(y)

    for i in range(2, f):
        z = x + y
        x = y
        y = z
        print(z)


fib(10)
