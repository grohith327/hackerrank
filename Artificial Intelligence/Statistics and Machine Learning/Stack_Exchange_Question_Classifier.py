import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

train_data = []
with open('training.json') as f:
    for file in f:
        train_data.append(json.loads(file))

train_data.remove(train_data[0])

topics = set()
for entry in train_data:
    topics.add(entry['topic'])

y_train = []
    
topics = list(topics)
for entry in train_data:
    for i in range(len(topics)):
        if(entry['topic'] == topics[i]):
            y_train.append(i+1)

y_train = np.array(y_train)

x_train = []

for entry in train_data:
    t = entry['question'] + ' ' + entry['excerpt']
    x_train.append(t)

count_vect = CountVectorizer()
x_train_count = count_vect.fit_transform(x_train)

tfidf_transform = TfidfTransformer()
x_train_tfidf = tfidf_transform.fit_transform(x_train_count)

clf = MultinomialNB()
clf.fit(x_train_tfidf,y_train)
                
test_data = []
n = int(input())
for _ in range(n):
    val = input()
    test_data.append(json.loads(val))

x_test = []    
for entry in test_data:
    t = entry['question'] + ' ' + entry['excerpt']
    x_test.append(t)

x_test_count = count_vect.transform(x_test)
x_test_tfidf = tfidf_transform.transform(x_test_count)

result = clf.predict(x_test_tfidf)
for val in result:
    print(topics[val-1])
    

