import calc as cc


def user_input():

    a = int(input())
    b = int(input())
    print('Use these functions: add, sub, multi, div\nor q for quit')
    fcn = str(input())

    if a or b or fcn != 'q':
        return a, b, fcn


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