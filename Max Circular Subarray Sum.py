def func(arr, n):
    cm = msf = arr[0]
    for i in range(1, n):
        cm = max(arr[i], arr[i]+cm)
        msf = max(msf, cm)
    return msf


def func2(arr, n):
    cm = msf = arr[0]
    for i in range(1, n):
        cm = min(arr[i], arr[i]+cm)
        msf = min(msf, cm)
    return msf


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = func(arr, n)
    s = sum(arr)
    b = s - func2(arr, n)
    if b == 0:
        print(a)
    else:
        print(max(a, b))




arr = [-1, -4, -5, -2, -1]
n = 5
a = func(arr, n)
print("a = " + str(a))
s = sum(arr)
b = s - func2(arr, n)
print(max(a, b))
