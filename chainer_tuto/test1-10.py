def vector_sum(x,y):
    if len(x) == len(y):
        len_i = len(x)
        for i in range(len_i):
            x[i] += y[i]
    return x

x = [1,2,3]
y = [8,1,2]

answer1 = vector_sum(x,y)
print(answer1)

def matrix_sum(X,Y):
    if len(X) == len(Y):
        if [len(v) for v in X] == [len(w) for w in Y]:
            len_x = len(X)
            len_y = len(X[0])
            for x in range(len_x):
                for y in range(len_y):
                    X[x][y] += Y[x][y]
    return X

X = [[1,2,3],[4,5,6]]
Y = [[8,1,2],[-1,0,-2]]

answer2 = matrix_sum(X,Y)
print(answer2)

def matrix_product(X,Y):
    if len(X[0]) == len(Y):
        len_x = len(X)
        len_y = len(X[0]) #len(Y)
        len_z = len(Y[0])
        Z = [[0 for i in range(len_z)] for j in range(len_x)]
        for l in range(len_x):
            for m in range(len_z):
                for n in range(len_y):
                    Z[l][m] += X[l][n] * Y[n][m]
        return Z

X = [[1,2,3],[4,5,6]]
Y = [[8,1],[-1,0],[0,1]]
answer3 = matrix_product(X,Y)
print(answer3)

def matrix_transpose(X):
    len_x = len(X)
    len_y = len(X[0])
    Y = [[0 for i in range(len_x)] for j in range(len_y)]
    for i in range(len_x):
        for j in range(len_y):
            Y[j][i] = X[i][j]
    return Y

X = [[1,2,3],[4,5,6]]
answer4 = matrix_transpose(X)
print(answer4)