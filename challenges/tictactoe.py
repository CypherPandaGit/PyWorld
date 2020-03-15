import pprint

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-' * 5)
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-' * 5)
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print(print_board(board))