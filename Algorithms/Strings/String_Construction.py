#!/bin/python3

import sys

def stringConstruction(s):
    # Complete this function
    s = list(s)
    p = ""
    cost = 0
    for i in range(len(s)):
        if(not p):
            p += s[i]
            cost += 1
            continue
        if(s[i] in p):
            p += s[i]
        else:
            p += s[i]
            cost += 1
    return cost

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
