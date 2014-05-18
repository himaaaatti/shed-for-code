#!/usr/bin/env python3



def main():

    joi = 0
    ioi = 0

    text = input()

    for i in range(len(text)-2):

        if text[i+1] == 'O' and text[i+2] == 'I':
            if text[i] == 'J':
                joi += 1

            elif text[i] == 'I':
                ioi += 1


    print(joi)
    print(ioi)

if __name__ == '__main__':
    main()
