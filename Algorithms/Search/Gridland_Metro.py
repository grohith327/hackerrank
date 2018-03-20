#!/bin/python3

import sys

def gridlandMetro(n, m, k, track):
    # Complete this function
    total = n*m
    vals = []
    for i in range(k):
        c = 0
        for j in range(len(vals)):
            if(vals[j][0] == track[i][0]):
                if(vals[j][1]>track[i][1] and vals[j][1]>track[i][2]):
                    continue
                if(vals[j][2]<track[i][1] and vals[j][2]<track[i][2]):
                    continue
                if(vals[j][1] >= track[i][1]):
                    c = 1
                    vals[j][1] = track[i][1]
                if(vals[j][2] <= track[i][2]):
                    c = 1
                    vals[j][2] = track[i][2]
                if(vals[j][1] < track[i][1] and vals[j][2] > track[i][2]):
                    c = 1
                    
        if(c == 0):
            vals.append(track[i])
    for i in range(len(vals)):
        total -= vals[i][2]-vals[i][1]+1
    return total
        

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
        track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
        track.append(track_t)
    result = gridlandMetro(n, m, k, track)
    print(result)
