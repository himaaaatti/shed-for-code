#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# Filename: 1003.py
# Author:   himaaaatti
# Created:  2014-05-15

keys = [[' '],
       ['\'', ',','.', '!', '?'],
       ['a', 'b', 'c', 'A', 'B', 'C'],
       ['d', 'e', 'f', 'D', 'E', 'F'],
       ['g', 'h', 'i', 'G', 'H', 'I'],
       ['j', 'k', 'l', 'J', 'K', 'L'],
       ['m', 'n', 'o', 'M', 'N', 'O'],
       ['p', 'q', 'r', 'P', 'Q', 'R'],
       ['t', 'u', 'v', 'T', 'U', 'V'],
       ['x', 'y', 'z', 'X', 'Y', 'Z']]


def main():

    count = -1
    data = input()
    before_number = data[0]
    output = []
    for n in data:
        if before_number == n:
            count += 1

        else:
            if before_number == '0':
                for zero in range(count):
                    output.append(' ')
            else:
                output.append(keys[int(before_number)][count])

            before_number = n
            count = 0

    else:
        if before_number == '0':
            for zero in range(count):
                output.append(' ')
        else:
            output.append(keys[int(before_number)][count])

    print(''.join(output))


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
