n = int(input())
for _ in range(n):
    x1,y1,x2,y2,xm,ym = map(int,input().strip().split(' '))
    if(x1*y2 - x2*y1 > 0 and ym*(x2-x1) - xm*(y2-y1) + x1*y2 - x2*y1 > 0):
        print("YES")
    elif(x1*y2 - x2*y1 < 0 and ym*(x2-x1) - xm*(y2-y1) + x1*y2 - x2*y1 < 0):
        print("YES")
    else:
        if(ym*(x2-x1) - xm*(y2-y1) + x1*y2 - x2*y1 == 0):
            if((y1 > ym and y2 > ym and y1 > 0 and y2 > 0) or (y1 < ym and y2 < ym and y1 < 0 and y2 < 0)):
                print("YES")
            else:
                print("NO")
            continue
        y_cord = (x2*y1-x1*y2)/(x2-x1-(xm/ym)*(y2-y1))
        if((y_cord > y1 and y_cord > y2) or (y_cord < y1 and y_cord < y2)):
            print("YES")
        else:
            print("NO")
            
