from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import preprocessing 
import numpy as np

n,m = map(int,input().strip().split(' '))
x_train = []
y_train = []
for _ in range(n):
    entry = list(input().strip().split(' '))
    entry.remove(entry[0])
    if(entry[0] == '+1'):
        y_train.append(int(entry[0]))
    else:
        y_train.append(0)
    entry.remove(entry[0])
    x_val = []
    for i in range(m):
        temp = list(entry[i].strip().split(':'))
        x_val.append(float(temp[-1]))
    x_train.append(x_val)



x_train = np.array(x_train)
y_train = np.array(y_train)



x_train = preprocessing.scale(x_train)

clf = RandomForestClassifier()
clf.fit(x_train,y_train)

q = int(input())
x_test = []
out = []
for _ in range(q):
    test = list(input().strip().split(' '))
    out.append(test[0])
    test.remove(test[0])
    x_val = []
    for i in range(m):
        temp = list(test[i].strip().split(':'))
        x_val.append(float(temp[-1]))
    x_test.append(x_val)

x_test = np.array(x_test)
x_test = preprocessing.scale(x_test)
y_test = clf.predict(x_test)


clf = GradientBoostingClassifier()
clf.fit(x_train,y_train)
y_test_gb = clf.predict(x_test)

clf = AdaBoostClassifier()
clf.fit(x_train,y_train)
y_test_abc = clf.predict(x_test)

for i in range(len(out)):
    t = [0,0]
    t[y_test[i]] += 1
    t[y_test_gb[i]] += 1
    t[y_test_abc[i]] += 1
    big = max(t)
    pos = t.index(big)
    if(pos == 0):
        print(out[i],'-1')
    else:
        print(out[i],'+1')

