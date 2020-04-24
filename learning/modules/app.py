import calc as cc


def user_input():

    print('Enter your first number: ')
    a = float(input())
    print('And your second number: ')
    b = float(input())
    print('Now you can use these functions: add, sub, multi, div\nor q for quit')
    fcn = str(input())

    if fcn != 'q':
        return a, b, fcn

    else:
        print('Bye')
        quit()


def main_function():

    up = user_input()

    if up[2] == 'add':
        print(cc.add(up[0], up[1]))

    elif up[2] == 'sub':
        print(cc.sub(up[0], up[1]))

    elif up[2] == 'multi':
        print(cc.multi(up[0], up[1]))

    elif up[2] == 'div':
        print(cc.div(up[0], up[1]))

    else:
        print('Something went wrong!')


main_function()
