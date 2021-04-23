import math
import random
arr_i = [1,2,3,4,5,6]
arr_θ = [0.5,0.1,0.1,0.1,0.1,0.1]
def log_likehood(arr_i,arr_θ):
    sum_likehood = 0
    for x in range(6):
        # print(arr_i[x]*arr_θ[x])
        # print(math.log(arr_i[x]*arr_θ[x]))
        sum_likehood += math.log(arr_i[x]*arr_θ[x])
    return sum_likehood

# print(log_likehood(arr_i,arr_θ))
for j in range(100):
    total = 0
    count = [random.randint(1,100) for i in range(6)]
    for i in range(6):
        total += count[i]
    for i in range(6):
        arr_θ[i] = count[i] / total
    print(arr_θ)
    print(log_likehood(arr_i,arr_θ))