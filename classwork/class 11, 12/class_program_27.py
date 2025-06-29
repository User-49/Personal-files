n = 65
m = 10
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(n),"@",m**2,end='  ')
        n =n+1
        m =m-1
    print()
