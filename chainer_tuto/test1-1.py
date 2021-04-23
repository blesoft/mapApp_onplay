import numpy as np
a = [4,8,3,4,1]
def FANC(arr):
    len_arr = len(arr)
    na = np.array(arr)
    for i in range(len_arr):
        swap = i + np.argmin(na[i:])
        (na[i],na[swap]) = (na[swap],na[i])
    return na
res = FANC(a)
print(res)
