 # ugly number ==> number with only 2,3 or 5 as its prime factors
 # eg - 1,2,3,5,6,8...

def nth_ugly_num(n):
    arr = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    next_num_multiple_of_two = 2*arr[i2]
    next_num_multiple_of_three = 3*arr[i3]
    next_num_multiple_of_five = 5*arr[i5]

    for i in range(n-1):
        # print(next_num_multiple_of_two, next_num_multiple_of_three, next_num_multiple_of_five)
        next_num = min(next_num_multiple_of_five, next_num_multiple_of_three, next_num_multiple_of_two)
        arr.append(next_num)
        if next_num == next_num_multiple_of_two:
            i2 += 1
            next_num_multiple_of_two = 2*arr[i2]
        if next_num == next_num_multiple_of_three:
            i3 += 1
            next_num_multiple_of_three = 3*arr[i3]
        if next_num == next_num_multiple_of_five:
            i5 += 1
            next_num_multiple_of_five = 5*arr[i5]

    print(arr)


nth_ugly_num(7)

