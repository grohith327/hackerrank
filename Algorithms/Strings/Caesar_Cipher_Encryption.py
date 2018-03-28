#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
s = list(s)
for i in range(n):
    if(ord(s[i]) >= 65 and ord(s[i]) <= 90):
        s[i] = chr((ord(s[i])-65+k)%26+65)
    if(ord(s[i]) >= 97 and ord(s[i]) <= 122):
        s[i] = chr((ord(s[i])-97+k)%26+97)
print("".join(s))
