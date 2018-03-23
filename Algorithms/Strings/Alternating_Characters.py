#!/bin/python3

import sys

def alternatingCharacters(s):
    # Complete this function
    no_of_del = 0
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            no_of_del += 1
    return no_of_del
            

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
