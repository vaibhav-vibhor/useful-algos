def maxsubarray(n, arr):
    sum = 0
    maxi = 0

    for i in range(n):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0

    return maxi

print(maxsubarray(7, [-2,3,4,-1,0,5,-1]))
