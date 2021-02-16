def func(arr, n):
    cm = arr[0]
    m = arr[0]
    for i in range(1, n):
        cm = max(cm+arr[i], arr[i])
        m = max(m, cm)
    return m



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # print(n, k)
    arr = list(map(int, input().split()))
    # print(arr)
    if k == 1:
        print(func(arr, n))
    else:
        ans = func(arr*2, 2*n)
        # print("pre ans = " + str(ans))
        if sum(arr) > 0:
            ans += (k-2)*sum(arr)
        print(ans)
