def rearrange(arr, n):
    # code here
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    s = min(len(pos), len(neg))
    # print(pos, neg)
    if arr[0] < 0:
        p = []
        for i in range(2*s):
            if i%2 == 0:
                p.append(neg.pop(0))
            else:
                p.append(pos.pop(0))
        if pos is None:
            p.extend(neg)
        else:
            p.extend(pos)
    else:
        p = []
        for i in range(2*s):
            if i%2 == 0:
                p.append(pos.pop(0))
            else:
                p.append(neg.pop(0))
        if pos is None:
            p.extend(neg)
        else:
            p.extend(pos)

    arr = p
    # print(arr)

rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8], 10)
