#!/bin/python3

import os
import sys


def gamingArray(arr):
    count = 0
    max_val = 0
    for i in range(len(arr)):
        if(i == 0):
            count += 1
            max_val = arr[i]
        else:
            if(arr[i] > max_val):
                max_val = arr[i]
                count += 1
    if(count%2 == 0):
        return "ANDY"
    return "BOB"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
