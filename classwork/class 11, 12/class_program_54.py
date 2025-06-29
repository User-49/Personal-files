x = input('enter the value: ')
l = []
while x !='no':
    l.append(int(x))
    x = input('enter the value: ')
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            temp = l[j]
            l[j]=l[j+1]
            l[j+1] =temp
    print(l)
