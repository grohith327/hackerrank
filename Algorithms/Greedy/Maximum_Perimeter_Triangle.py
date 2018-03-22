#!/bin/python3

import sys

def maximumPerimeterTriangle(l):
    # Complete this function
    l.sort()
    l.reverse()
    ans = []
    for i in range(len(l)-2):
        if(l[i]+l[i+1]>l[i+2] and l[i]+l[i+2]>l[i+1] and l[i+1]+l[i+2]>l[i]):
            temp = []
            temp.append(l[i+2])
            temp.append(l[i+1])
            temp.append(l[i])
            ans.append(temp)
    if(ans):
        return ans[0]
    else:
        return [-1]
        

if __name__ == "__main__":
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    result = maximumPerimeterTriangle(l)
    print (" ".join(map(str, result)))


