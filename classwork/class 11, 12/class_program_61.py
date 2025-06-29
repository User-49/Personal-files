l = eval(input("enter the list: "))
for i in l:
    a=l.count(i)
    for j in range(a-1):
        if a>1:
            l.remove(i)
print(l)
