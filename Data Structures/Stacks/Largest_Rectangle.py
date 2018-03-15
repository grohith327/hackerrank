#!/bin/python3

import sys

def largestRectangle(h):
    # Complete this function
    max_area = 0
    for i in range(len(h)):
        if(i == 0):
            k = i+1
            length = 1
            while(k<len(h)):
                if(h[k] >= h[i]):
                    length += 1
                else:
                    break
                k += 1
            k = i-1
            while(k>=0):
                if(h[k] >= h[i]):
                    length += 1
                else:
                    break
                k -= 1
            max_area = length*h[i]
        else:
            k = i+1
            length = 1
            while(k<len(h)):
                if(h[k] >= h[i]):
                    length += 1
                else:
                    break
                k += 1
            k = i-1
            while(k>=0):
                if(h[k] >= h[i]):
                    length += 1
                else:
                    break
                k -= 1
            if(length*h[i] > max_area):
                max_area = length*h[i]
    return max_area

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
