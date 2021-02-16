

def max_sum(a,n):
    #code here
    it = list(range(n))
    s = 0
    p = sum(a)
    for i in range(n):
        s += i*a[i]
    # print(s)
    # print(a)
    m = s
    for i in range(n-1):
        x = a[0]
        a.remove(x)
        a.append(x)
        # print(a)
        s += a[n-1]*(n-1)
        s -= p - a[n-1]
        # print(s)
        m = max(m, s)
    # print("m = " + str(m))
    return m


print(max_sum([8,3,1,2], 4))

