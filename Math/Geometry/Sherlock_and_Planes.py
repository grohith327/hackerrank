n = int(input())
for _ in range(n):
    points = []
    for __ in range(4):
        l = list(map(int,input().strip().split(' ')))
        points.append(l)
    pq = []
    pr = []
    
    pq.append(points[0][0] - points[1][0])
    pq.append(points[0][1] - points[1][1])
    pq.append(points[0][2] - points[1][2])
    
    pr.append(points[0][0] - points[2][0])
    pr.append(points[0][1] - points[2][1])
    pr.append(points[0][2] - points[2][2])
    
    norm_vec = []
    
    norm_vec.append(((pq[1]*pr[2])-(pq[2]*pr[1])))
    norm_vec.append((pq[2]*pr[0])-(pq[0]*pr[2]))
    norm_vec.append((pq[0]*pr[1])-(pq[1]*pr[0]))
    
    if(norm_vec[0]*(points[3][0]-points[1][0])+norm_vec[1]*(points[3][1]-points[1][1])+norm_vec[2]*(points[3][2]-points[1][2]) == 0):
        print("YES")
    else:
        print("NO")
    
