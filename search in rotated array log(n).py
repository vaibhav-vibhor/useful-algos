#code

def findpivot(arr, low, high):

    if low > high:
        return -1

    mid = (low + high)//2

    if arr[mid] > arr[mid+1]:
        return mid
    elif arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[high] < arr[mid]:
        return findpivot(arr, mid + 1, high)
    elif arr[mid] < arr[low]:
        return findpivot(arr, low, mid - 1)
    else:
        return 0


def binsearch(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high)//2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binsearch(arr, low, mid - 1, key)
    elif arr[mid] < key:
        return binsearch(arr, mid+1, high, key)

# print(binsearch([1, 2, 3], 0, 2, 10))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    m = findpivot(arr, 0, n-1)
    # print("pivot = " + str(m))
    a = arr[0:m+1]
    b = arr[m+1:]
    # print("a, b = " + str(a) + ", " + str(b))
    p = binsearch(a, 0, m, k)
    # print("p = " + str(p))
    # print("m+1, n-1 = " + str(m+1) + ", " + str(n-1))
    q = binsearch(b, 0, n - m - 2, k)
    # print("q = " + str(q))
    if p != -1:
        print(p)
    elif q != -1:
        print(len(a) + q)
    else:
        print(-1)

