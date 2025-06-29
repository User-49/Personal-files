x = input("enter string: ")
vow = 0
for i in 'aeiou':
    for j in range(len(x)):
        if i == x[j]:
            vow += 1
print(vow)
