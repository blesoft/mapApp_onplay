squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares2 = [x ** 2 for x in range(10)]
print(squares2)

a = [4,8,3,4,1]
a2 = []
for i in a:
    # if i % 2 == 0:
    #     a2.append(0)
    # else:
    #     a2.append(1)
    a2.append(i % 2)
print(a2)
init = sum(a2)
print("奇数の個数は" + str(init))
b = [x for x in a if x % 2 == 1]
print(b)