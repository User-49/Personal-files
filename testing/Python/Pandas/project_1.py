import pandas
import numpy

# pandas series an hold any arbitrary python object

label = ['a', 'b', 'c']
l = [10,20,30]
arr = numpy.array(l)
d = {'a':10, 'b':20, 'c':30}

print(pandas.Series(data=l))
print(pandas.Series(data=label, index=l))
print(pandas.Series(data=arr))
print(pandas.Series(data=d))
print(pandas.Series(data=d, index=l))
