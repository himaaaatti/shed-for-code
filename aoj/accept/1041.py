#!/usr/bin/env python3


while True:
    a = input()
    n = int(a)
    if n == 0:
        break
    ans = 0
    for i in range(n//4):
        ans += int(input())
    print(ans)

