import numpy

l = [[[1,2], [3,4]], [[5,6],[7,8]], [[9,10], [11,12]]]
print(l)

l = numpy.array(l)
print(l)
print("numpy.size: ", numpy.size(l, axis=None))
print("numpy.shape: ", numpy.shape(l))
print("numpy.shape dimention 3: ", numpy.size(l, axis=2))


print("l[2]: ", l[2])
print("l[2][1]: ", l[2][1])
print("l[2][1][0]: ", l[2][1][0])
