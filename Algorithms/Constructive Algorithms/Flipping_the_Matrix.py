#!/bin/python3

import sys

def flippingMatrix(matrix):
    # Complete this function
    sums = 0
    length = len(matrix)
    n = int(length/2)
    for i in range(n):
        for j in range(n):
            sums += max([matrix[length-1-i][j],matrix[i][length-1-j],matrix[length-1-i][length-1-j],matrix[i][j]])
    return sums

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        matrix = []
        for matrix_i in range(2*n):
            matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
            matrix.append(matrix_t)
        result = flippingMatrix(matrix)
        print(result)
