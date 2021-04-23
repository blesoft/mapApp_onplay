import numpy as np
import random
a = np.array([1,2,3])
b = np.array([2,2,3])
c = a * b
print(c)
c = a * 2
print(c)

a = np.random.randint(0,10,(2,1,3))
b = np.random.randint(0,10,(3,1))
print('a:',a)
print('\na.shape:',a.shape)
print('b:',b)
print('\nb.shape:',b.shape)
c = a + b
print('a+b:',c)
print('(a+b).shape:',c.shape)
print('Original shape:',b.shape)
b_expanded = b[np.newaxis,:,:]
print('Added new axis to the top:',b_expanded.shape)
b_expanded2 = b[:,np.newaxis,:]
print('Added new axis to the middle:',b_expanded2.shape)
print(b)
print(b_expanded)
print(b_expanded2)

a = np.array([[0,1,2,1,0],
              [3,4,5,4,3],
              [6,7,8,7,6],
              [3,4,5,4,3],
              [0,1,2,1,0]])
b = np.array([1,2,3,4,5])
c = np.empty((5,5))

for i in range(a.shape[0]):
    c[i,:] = a[i,:] + b
print(c)

c = a + b
print(c)

A = np.array([[0,1,2],[3,4,5],[6,7,8]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
C = np.dot(A,B)
print(C)
C = A.dot(B)
print(C)
print(a.dtype)

x = np.random.randint(0,10,(8,10))
print(x)
print(x.mean())
print(x.var())
print(x.std())
print(x.max())
print(x.min())
print(x.mean(axis=1))
y = np.array([
    x[0,:].mean(),
    x[1,:].mean(),
    x[2,:].mean(),
    x[3,:].mean(),
    x[4,:].mean(),
    x[5,:].mean(),
    x[6,:].mean(),
    x[7,:].mean(),
])
print(y)

X = np.array([[2,3],[2,5],[3,4],[5,9]])
ones = np.ones((X.shape[0],1))

X = np.concatenate((ones,X),axis=1)
print(X)

t = np.array([1,5,6,8])

xx = np.dot(X.T,X)
print(xx)

xx_inv = np.linalg.inv(xx)
print(xx_inv)

xt = np.dot(X.T,t)
print(xt)

w = np.dot(xx_inv,xt)
print(w)

w_ = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(t)
print(w_)

w_ = np.linalg.solve(X.T.dot(X),X.T.dot(t))
print(w_)
