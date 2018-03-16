#!/bin/python3

import sys

def fibonacciModified(t1, t2, n):
    # Complete this function
    bottom_up = []
    for i in range(n+1):
        bottom_up.append(None)
    bottom_up[1] = t1
    bottom_up[2] = t2
    for j in range(3,n+1):
        bottom_up[j] = bottom_up[j-2] + bottom_up[j-1]**2
    return bottom_up[n]

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
