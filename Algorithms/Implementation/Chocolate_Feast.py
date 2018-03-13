#!/bin/python3

import sys

def chocolateFeast(n, c, m):
    # Complete this function
    num_c = int(n/c)
    num_wr = num_c
    while(num_wr >= m):
        if(num_wr%m == 0):
            num_wr = int(num_wr/m)
            num_c = num_c + num_wr
        else:
            rem_wr = num_wr%m
            num_wr = int(num_wr/m)
            num_c += num_wr
            num_wr += rem_wr
    return num_c

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)
