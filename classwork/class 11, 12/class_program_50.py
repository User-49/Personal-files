l = [-10,20,-5,24,-90,22]
i =0
len = len(l)
while i<len:
    if l[i]<0:
        del l[i]
        len = len-1
        i = i-1
    i = i+1
print(l)
'''
l = [-10,20,-5,24,-90,22]
i =0
len = len(l)
while i<len:
    if l[i]%2!=0:
        del l[i]
        len = len-1
        i = i-1
    i = i+1
print(l)
