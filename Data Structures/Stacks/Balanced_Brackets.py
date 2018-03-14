#!/bin/python3

import sys

def isBalanced(s):
    # Complete this function
    stack = []
    for i in s:
        if(i == '(' or i == '{' or i == '['):
            stack.append(i)
        else:
            if(stack):
                if((i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[')):
                    val = stack.pop()
            else:
                if(i == '}' or i == ')' or i == ']'):
                    return "NO"
        
    if(len(stack) == 0):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
