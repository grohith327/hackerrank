inp = input().split(" ")
img = []
for i in range(len(inp)):
    temp = inp[i].split(",")
    img.append(temp)
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j] = int(img[i][j])
sums = 0
for i in range(len(img)):
    for j in range(len(img[i])):
        sums += img[i][j]

avg_val = sums/(len(img)*3)

if(avg_val<90):
    print("night")
else:
    print("day")

    
