import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

data = []
with open('trainingdata.txt','r') as f:
    data = f.readlines()
#print(data)
to_list = []
for i in data:
    to_list.append(i.split(','))
for i in range(len(to_list)):
    to_list[i][-1] = to_list[i][-1].strip('\n')

x_train = []
y_train = []
s = set()
for i in range(len(to_list)):
    y_train.append(int(to_list[i][-1]))
    to_list[i].remove(to_list[i][-1])
    for j in to_list[i]:
        s.add(j)

types = list(s)

for i in to_list:
    temp = []
    for j in i:
        for k in range(len(types)):
            if(types[k] == j):
                temp.append(k+1)
                break
    x_train.append(temp)

x_train = np.array(x_train)
y_train = np.array(y_train)


clf = RandomForestClassifier(n_estimators=150)
clf.fit(x_train,y_train)

clf_1 = GradientBoostingClassifier(n_estimators=150)
clf_1.fit(x_train,y_train)

clf_2 = AdaBoostClassifier(n_estimators=150)
clf_2.fit(x_train,y_train)

x_test = []
q = int(input())
for _ in range(q):
    test = input().strip().split(',')
    temp = []
    for i in test:
        for j in range(len(types)):
            if(types[j] == i):
                temp.append(j+1)
                break
    x_test.append(temp)

x_test = np.array(x_test)

y_test = clf.predict(x_test)
y_test_1 = clf_1.predict(x_test)
y_test_2 = clf_2.predict(x_test)

for i in range(len(y_test)):
    t = [0,0]
    t[y_test[i]-1] += 1
    t[y_test_1[i]-1] += 1
    t[y_test_2[i]-1] += 1
    big = max(t)
    pos = t.index(big)
    print(pos+1)
