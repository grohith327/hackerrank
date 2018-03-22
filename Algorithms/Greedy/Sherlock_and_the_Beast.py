#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = n
    count = 0
    while(i>=0):
        if(i%3 == 0 and (n-i)%5 == 0):
            count = 1
            break
        i -= 1
    if(count == 0):
        print("-1")
    else:
        l = []
        for j in range(i):
            l.append(5)
        for j in range(n-i):
            l.append(3)
        print(*l, sep='')
