n = int(input("value of n: "))
x = 0
sum = 0
for i in range(1,n+1):
    x+=i
    print("term",i,": ",x)
    sum = sum+x
print("sum of all terms is :",sum)
