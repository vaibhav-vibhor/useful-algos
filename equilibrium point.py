t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    c = 0
    p = -1
    for i in range(n):
        if i != 0:
            c += arr[i-1]
        d = s - c - arr[i]
        # print(i, c, d)
        if c == d:
            p = i
            break
        if c > d:
            break
    if p != -1:
        print(p+1)
    else:
        print(-1)



