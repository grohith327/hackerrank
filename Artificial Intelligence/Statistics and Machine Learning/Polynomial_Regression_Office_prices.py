import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

F, N = map(int,input().strip().split(' '))
train_data = []
test_data = []
for _ in range(N):
    temp = list(map(float,input().strip().split(' ')))
    train_data.append(temp)
M = int(input())
for _ in range(M):
    temp = list(map(float,input().strip().split(' ')))
    test_data.append(temp)

train_data = np.array(train_data)
test_data = np.array(test_data)



X_train = train_data[:,0:F]
Y_train = train_data[:,-1]

X_test = test_data

poly = PolynomialFeatures(degree=2)
X_train = poly.fit_transform(X_train)
X_test = poly.fit_transform(X_test)

model = linear_model.LinearRegression()
model.fit(X_train,Y_train)
Y_test = model.predict(X_test)
result = '\n'.join(list(map(str,Y_test)))
print(result)
