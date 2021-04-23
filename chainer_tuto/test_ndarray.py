import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(np.array([a[0,1],a[2,1],a[1,0]]))
print(a[[0,2,1],[1,1,0]])

x = np.array([1,2,3])
print(x.dtype)
x = np.array([1.,2.,3.])
print(x.dtype)
x = np.array([1,2,3],dtype=np.float32)
print(x.dtype)
x = np.array([1,2,3],dtype='f')
print(x.dtype)
x = x.astype(np.float64)
print(x.dtype)
a = np.array([[0,1,2],[3,4,5],[6,7,8]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = a+b
c = a-b
c = a*b
c = a/b
c = np.sqrt(b)
n = 2
c = np.power(b,n)
print(c)
print(c**n)
a = np.array([[0,1,2],[3,4,5],[6,7,8]])
b = np.array([1,2,3])
c = a+b
print(c)