#!/bin/python3

import sys

def lonely_integer(a):
    count = []
    for i in range(101):
        count.append(0)
    for i in a:
        count[i] += 1
    val = 0
    for i in range(101):
        if(count[i] == 1):
            val = i
    return val

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
