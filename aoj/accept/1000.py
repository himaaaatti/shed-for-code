#!/usr/bin/env python3


while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError as e:
        break

