arr = [i for i in range(101) if i > 1]
for x in range(2,101):
    for y in range(2,x):
        if x % y == 0:
            arr.remove(x)
            break

print(arr)