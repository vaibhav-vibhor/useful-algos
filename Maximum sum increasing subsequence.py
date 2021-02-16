
def maxSumIS(Arr, n):
    # code here
    sums = [Arr[0]]
    maxsum = Arr[0]
    m = {}
    m[0] = Arr[0]
    if n == 1:
        return Arr[0]
    for i in range(1,n):
        elem = Arr[i]
        j = i-1
        s = -1
        k = None
        # while(p > elem):
        #     j -= 1
        #     if j == -1:
        #         break
        #     p = Arr[j]
        while j > -1:
            p = m[j]
            if p > s and Arr[j] < Arr[i]:
                s = p
                k = j
            j -= 1
        if s == -1:
            thissum = Arr[i]
        else:
            thissum = Arr[i] + m[k]
        m[i] = thissum
        # print(thissum)
        if thissum > maxsum:
            maxsum = thissum
    # print(m)
    return maxsum


print(maxSumIS([23,1], 2))
