#!/bin/python3

import sys

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    if(N<2):
        print("0")
    else:
        print(int((N*(N-1))/2))
