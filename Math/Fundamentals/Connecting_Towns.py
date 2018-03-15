t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().strip().split(' ')))
    prod = 1
    for k in l:
        prod *= k
        prod %= 1234567
    print(prod)
