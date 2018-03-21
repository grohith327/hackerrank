#!/bin/python3

import sys

def getMinimumCost(n, k, c):
    # Complete this function
    c.sort()
    c.reverse()
    cost = 0
    if(n == k):
        for i in range(k):
            cost += c[i]
        return cost
    elif(n < k):
        for i in range(n):
            cost += c[i]
        return cost
    else:
        for i in range(k):
            cost += c[i]
        pos = k
        num = 1
        count = 0
        while(pos < n):
            cost += (num + 1)*c[pos]
            pos += 1
            count += 1
            if(count == k):
                num += 1
                count = 0
        return cost
    
    

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
