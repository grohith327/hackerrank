#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

block = []
block.append(list(reversed(h1)))
block.append(list(reversed(h2)))
block.append(list(reversed(h3)))

sum1 = sum(block[0])
sum2 = sum(block[1])
sum3 = sum(block[2])

count = 1
finding_min = []
finding_min.append(sum1)
finding_min.append(sum2)
finding_min.append(sum3)
min_height = min(finding_min)




while(sum1 != sum2 or sum2 != sum3):
    
    if(sum1 > min_height):
        val = block[0].pop()
        sum1 -= val
        if(sum1 < min_height):
            min_height = sum1
    if(sum2 > min_height):
        val = block[1].pop()
        sum2 -= val
        if(sum2 < min_height):
            min_height = sum2
    if(sum3 > min_height):
        val = block[2].pop()
        sum3 -= val
        if(sum3 < min_height):
            min_height = sum3
            
    if(sum1 == 0 or sum2 == 0 or sum3 == 0):
        count = 0
        break

if(count == 0):
    print(count)
else:
    print(sum1)
    
    
