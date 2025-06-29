n = int(input("enter n: "))
m = 1
s = 2
p = 1
for i in range(n):
    for j in range(p):
        print(m,end=' ')
        m+=s
        s = s+1
    p+=1
    print()

