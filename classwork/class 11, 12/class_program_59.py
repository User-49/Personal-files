l = [1,23,43,54]
i=0
Len=len(l)
while i<Len:
    if l[i]<0 or l[i]%2==1:
        del l[i]
        i=i-1
        Len-=1
    i+=1
print(l)
