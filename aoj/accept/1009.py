#!/usr/bin/env python3


def main():

    while True:
        try:

            a, b = map(int, input().split())
            print(euclid_algorithm(a, b))

        except EOFError as e:
            break

def euclid_algorithm(a, b):

    while a and b:

        if a > b:
            a = a - b
        else:
            b = b - a

    return a if a else b

if __name__ == '__main__':
    main()
