a = []
x = int(input('enter the no. of elements you want to add: '))
for i in range(x):
    a.append(int(input('enter the element: ')))
for i in a:
    j = a.index(i)
    while j>0:
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
        else:
            break
        j -=1
    print(a)
