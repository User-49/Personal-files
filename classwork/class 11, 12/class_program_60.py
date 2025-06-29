l = eval(input("enter he list: "))
for i in l:
    if type(i)==str:
        l.swapcase(i)
    else:
        l[l.index(i)]=i**2
print(l)
