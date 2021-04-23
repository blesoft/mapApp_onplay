import numpy as np
a = [4,8,3,4,1]
na = np.array(a)
na2 = np.delete(na,0)
na3 = np.delete(na,len(na)-1)
na4 = np.append(na,100)
print(na2)
print(na3)
print(na4)