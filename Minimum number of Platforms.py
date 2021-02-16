t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    dep = list(map(str, input().split()))
    m = []
    for i in range(n):
        m.append([arr[i], 1])
        m.append([dep[i], -1])

    m.sort()
    # print(m)
    c = 0
    ans = 0
    for i in range(2*n):
        # print("c = " + str(c))
        if m[i][1] == 1:
            c+=1
        else:
            c-=1
        ans = max(ans, c)
    print(ans)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    dep = list(map(str, input().split()))
    arr.sort()
    dep.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1

        elif arr[i] > dep[j]:
            plat_needed -= 1
            j += 1

        if plat_needed > result:
            result = plat_needed

    print(result)


