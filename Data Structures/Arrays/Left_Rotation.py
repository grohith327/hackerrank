#!/bin/python3

import os
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    d = d%n
    for _ in range(d):
        temp = a[0]
        a.remove(temp)
        a.append(temp)
    print(*a,sep=' ')
