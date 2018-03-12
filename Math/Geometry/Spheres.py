import math 

n = int(input())
for _ in range(n):
    r1,r2 = map(int,input().strip().split(' '))
    c1 = list(map(int,input().strip().split(' ')))
    a1 = list(map(int,input().strip().split(' ')))
    c2 = list(map(int,input().strip().split(' ')))
    a2 = list(map(int,input().strip().split(' ')))
    for i in range(3):
        a1[i] /= 2
        a2[i] /= 2
    count = 0
    k_1 = (r1+r2)**2
    c_x = c2[0] - c1[0]
    c_y = c2[1] - c1[1]
    c_z = c2[2] - c1[2]
    a_x = a2[0] - a1[0]
    a_y = a2[1] - a1[1]
    a_z = a2[2] - a1[2]
    const_sum_sq = c_x**2 + c_y**2 + c_z**2
    a = a_x**2 + a_y**2 + a_z**2
    b = 2*(a_x*c_x + a_y*c_y + a_z*c_z)
    c = const_sum_sq - k_1
    discr = b**2-4*a*c
    if(discr < 0):
        print("NO")
    else:
        discr = math.sqrt(discr)
        root_1 = (-1*b + discr)/(2*a)
        root_2 = (-1*b - discr)/(2*a)
        if(root_1 >= 0 or root_2 >=0):
            print("YES")
        else:
            print("NO")
    
