#insersion sort
'''
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in l:
    j = l.index(i)
    while j > 0:
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
        else:
            break
        j -= 1
    print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
for i in l:
    x = l.pop()
    l.insert(0,x)
    print(l)
'''
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
