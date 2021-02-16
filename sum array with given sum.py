n, s = map(int, input().split())
arr = list(map(int, input().split()))
conc = 0
m = {}
c = 0
for i in range(n):
    conc += arr[i]
    if conc == s:
        print(1, i+1)
        c = 1
        break
    if conc - s in m:
        print(m.get(conc - s) + 2, i+1)
        c = 1
        break
    m[conc] = i
if c == 0:
    print(-1)
