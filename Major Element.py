t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = {}
    c = 0
    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
            if m[arr[i]] > n//2:
                print(arr[i])
                c = 1
                break
        else:
            m[arr[i]] = 1
    if c == 0:
        print(-1)
