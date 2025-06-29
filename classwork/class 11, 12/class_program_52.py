"""l = [12,5,89,23,44,90,45,13]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            temp = l[j]
            l[j]=l[j+1]
            l[j+1] =temp
    print(l)"""
#wap the max value from the given list
l = [12,5,89,23,44,1,45,13]
for i in range(1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            temp = l[j]
            l[j]=l[j+1]
            l[j+1] =temp
print(temp)

