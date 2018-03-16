t = int(input())
for _ in range(t):
    n = int(input())
    if(n==1 or n==2):
        print("-1")
    else:
        if(n%2!=0):
            print("2")
        else:
            if(n%4 == 0):
                print("3")
            else:
                print("4")
