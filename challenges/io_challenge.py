with open('..\\learning\\ipsum.txt', 'a') as txt:
    for i in range(1, 13):
        print(f'{i:>2} times 2 is {i * 2}', file=txt)
    print(20 * '-', file=txt)
