


t = int(input())
for _ in range(t):
    n = int(input())
    gpa = list(map(float,input().strip().split(' ')))
    apt = []
    temp = list(map(float,input().strip().split(' ')))
    apt.append(temp)
    temp = list(map(float,input().strip().split(' ')))
    apt.append(temp)
    temp = list(map(float,input().strip().split(' ')))
    apt.append(temp)
    temp = list(map(float,input().strip().split(' ')))
    apt.append(temp)
    temp = list(map(float,input().strip().split(' ')))
    apt.append(temp)
    max_val = 0
    pos = 0
    for i in range(5):
        x = apt[i]
        y = gpa
        x_prod_y = []
        x_sq = []
        y_sq = []
        if(sum(x) == 0):
            continue
        for j in range(len(apt[i])):
            x_prod_y.append(x[j]*y[j])
            x_sq.append(x[j]**2)
            y_sq.append(y[j]**2)
        if(n*sum(x_sq)-(sum(x)**2) == 0):
            continue
        gamma = (n*sum(x_prod_y)-sum(x)*sum(y))/((n*sum(x_sq)-(sum(x)**2))*(n*sum(y_sq)-(sum(y)**2)))**(0.5)
        if(i == 0):
            max_val = gamma
            pos = i+1
        else:
            if(max_val < gamma):
                max_val = gamma
                pos = i+1
    print(pos)
        
