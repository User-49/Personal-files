n = input("enter the value: ")
l = len(n)
for i in range(l):
    for j in range(l-i):
        print(n[j],end=' ')
    print()
