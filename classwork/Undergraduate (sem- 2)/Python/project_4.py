from functools import reduce
def add(x,y):
	return x+y
num_list = [1,2,3,4,5]
print("sum of values in list =", reduce(add,num_list))
