t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    num=0
    for i in range(n-1):
        if(a[i]>=m):
            continue
        for j in range(i+1,n):
            if(a[j]>=m):
                continue
            if(a[i]+a[j]==m):
                x=i+1
                y=j+1
                num=1
                break
        if(num==1):
            break
    print(x,y)
    
