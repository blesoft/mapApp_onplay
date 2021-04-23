#さいころを10連でふって直前にでた数より小さい、または同じになる確率を求める。
##１回目が１のとき、
## 111....
##１回目が２のとき、
## 2 1or2 とつづく。。
##同様に、１回目が３のとき、
## 3 1or2or3

import itertools
# arr = [1,2,3,4,5,6]

# for v in itertools.combinations_with_replacement(arr,10):
#     judge = 0
#     for i in range(0,9):
#         if v[i] < v[i+1]:
#             judge = 1
#     if judge == 0:
#         print(v)

arr = [1 for i in range(10)]
# count = 0
# all_count = 6**10
next_count = 0
next_all_count = 0
for i in range(6**10):
    if i > 0:
        arr[9] += 1
        for j in range(10):
            if arr[9-j] == 7:
                arr[9-j] = 1
                arr[9-j-1] += 1

    judge = 0
    for m in range(0,9):
        if arr[m] < arr[m+1]:
            judge = 1
    if judge == 0:
        # print(arr)
        # count += 1
        next_all_count += 6
        next_count += (6 - arr[9])
# per_Luck = count / all_count
per_11Luck = next_count / next_all_count
