from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = []
Y = []

with open('apple-computers.txt','r') as f1:
    data = f1.readlines()
    
for i in range(len(data)):
    data[i] = data[i].replace('\n','')
    data[i] = data[i].replace('\t','')
    
X = list(data)
for _ in range(len(X)):
    Y.append(0)

with open('apple-fruit.txt','r') as f1:
    data = f1.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\n','')
    data[i] = data[i].replace('\t','')

X = X + data
for _ in range(len(data)):
    Y.append(1)

X = np.array(X)
Y = np.array(Y)

X, Y = shuffle(X,Y)

count_vect = CountVectorizer()
x_train_count = count_vect.fit_transform(X)

tfidf = TfidfTransformer()
x_train_tfidf = tfidf.fit_transform(x_train_count)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(x_train_tfidf,Y)

n = int(input())
x_test = []
for _ in range(n):
    line = input()
    x_test.append(line)

x_test = np.array(x_test)

x_test_count = count_vect.transform(x_test)
x_test_tfidf = tfidf.transform(x_test_count)

y_pred = clf.predict(x_test_tfidf)

for value in y_pred:
    if(value == 0):
        print('computer-company')
    else:
        print('fruit')
