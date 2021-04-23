import math
def p(r,k):
    return pow(r,k) * math.e**(-r) / math.factorial(k)

def log_likehood(r,k,i):
    sum_likehood = 0
    for n in range(i):
        sum_likehood += math.log(pow(k*p(r,k)))

