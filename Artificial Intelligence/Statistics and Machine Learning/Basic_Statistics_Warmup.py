n = int(input())
val = list(map(int,input().strip().split(' ')))
mean = sum(val)/n
t = val
t.sort()
if(n%2 != 0):
    median = t[int(n/2)+1]
else:
    median = float((t[int(n/2)]+t[int(n/2)-1])/2)
count = []
for i in range(100001):
    count.append(0)
for j in val:
    count[j] += 1
max_val = max(count)
mode = 0
for i in range(len(count)):
    if(max_val == count[i]):
        mode = i
        break
sum_of_sq = 0
for i in val:
    temp = i - mean
    sum_of_sq += temp**2
std_dev = (sum_of_sq/n)**(0.5)
a = (std_dev * 1.96)/(n)**(0.5)
lower_lvl = mean - a
upper_lvl = mean + a
mean = round(mean,1)
median = round(median,1)
mode = round(mode,1)
std_dev = round(std_dev,1)
lower_lvl = round(lower_lvl,1)
upper_lvl = round(upper_lvl,1)
print(mean)
print(median)
print(mode)
print(std_dev)
print(lower_lvl,upper_lvl)
