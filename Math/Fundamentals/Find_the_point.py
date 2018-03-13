n = int(input())
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().strip().split(' '))
    print(2*x2-x1,2*y2-y1)
