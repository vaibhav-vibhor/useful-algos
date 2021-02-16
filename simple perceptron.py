import numpy

x = [[1,3,3], [1,3,8], [1,9,7], [1,5,7], [1,2,6], [1,4,5], [1,6,5], [1,2,3], [1,8,5], [1,2,5], [1,2,1], [1,8,3], [1,11,3], [1,11,1], [1,8,1], [1,3,1], [1,-1,-1], [1,3,-1], [1,7,0], [1,5,2]]

y = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1]

# print(len(x), len(y))

w = [0, 1, 1]

# print(w)

p = 0

# k = numpy.sign(sum(a*b for a,b in zip(w,x[p])))
# print(k)


while p != 19:
    if y[p] == numpy.sign( sum(a*b for a,b in zip(w,x[p])) ):
        p += 1
    else:
        w = w + numpy.multiply(y[p], x[p])
        p = 0

print(w)

# for i in range(len(x)):
#     print(numpy.sign( sum(a*b for a,b in zip(w,x[i])) ))
