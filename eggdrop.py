k = 3  # no of eggs
f = 100  # no of floors
a = [[0] * (f + 1) for i in range(k)]
for i in range(f + 1):
    a[0][i] = i
for i in range(k):
    a[i][0] = 0
    a[i][1] = 1

for i in range(k):
    print(a[i])
print("-------------xx------------")

for i in range(1, k):
    for j in range(2, f + 1):
        if i + 1 > j:
            # print("egg more than floor. i, j = " + str(i) + ", " + str(j) + " || elem = " + str(a[i-1][j]))
            a[i][j] = a[i - 1][j]
        else:
            p = 10 ** 6
            for l in range(1, j + 1):
                x = 1 + max(a[i - 1][l - 1], a[i][j - l])
                # print("x = " + str(x))
                if x < p:
                    p = x
            a[i][j] = p
            # print("egg NOT more than floor. i, j = " + str(i) + ", " + str(j) + " || p = " + str(p))

for i in range(k):
    print(a[i])

print("final answer = " + str(a[k-1][f]))
