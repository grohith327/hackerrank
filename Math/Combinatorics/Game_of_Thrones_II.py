import math
import sys

s = input().strip()
l = []
s = list(s)
for i in range(26):
    l.append(0)
for i in range(len(s)):
    l[ord(s[i])-97] += 1
sums = 0
for i in range(26):
    if(l[i] != 0 and l[i]%2 != 0):
        l[i] -= 1
    if(l[i] != 0):
        l[i] /= 2
sums = sum(l)
numr = math.factorial(sums)
for i in range(26):
    if(l[i] == 0):
        continue
    val = math.factorial(l[i])
    numr = int(numr//val)
print(int(numr%(10**9+7)))

