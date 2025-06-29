l = list()
choice = 'y'
i = 0

while choice=='y':
	l.append(input("Enter the string: "))
	choice = input("Do you wish to continue(y/n): ")

l.sort(key=len)
prefix = l[0]


while i<len(l):
	if l[i].startswith(prefix) == False:
		prefix = prefix[:-1]
		continue
	i += 1

print("longest common prefix: ", prefix)
