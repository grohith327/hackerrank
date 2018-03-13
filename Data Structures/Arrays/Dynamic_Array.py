n,q = map(int,input().strip().split(' '))
seqlist = []
for _ in range(n):
    temp = []
    seqlist.append(temp)

last_ans = 0    
for _ in range(q):
    opt,x,y = map(int,input().strip().split(' '))
    if(opt == 1):
        seq_num = (x^last_ans)%n
        seqlist[seq_num].append(y)
    else:
        seq_num = (x^last_ans)%n
        last_ans = seqlist[seq_num][y%(len(seqlist[seq_num]))]
        print(last_ans)
