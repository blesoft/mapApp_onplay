import math

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

def g(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

x = [-3,-2,-1,-0,1,2,3]
y = [0.25,0.5,1,2,4,8]

for i in x:
    print(f(i))
    print(dfdx_approx(i))

for i in y:
    print(1/i)
    print(dgdx_approx(i))