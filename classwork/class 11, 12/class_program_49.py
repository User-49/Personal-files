a = input("enter the string: ")
l = a.split()
print("words having vowels are: ",end='')
for i in range(len(l)):
    x = 0
    for j in l[i]:
        if j  in "AEIOUaeiou":
            x +=1
    if x > 0:
        print(l[i],end=" ")

