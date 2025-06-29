def check(x):
	if x%2==0:
		return 1
even = list(filter(check,range(1,21)))
print(even)
