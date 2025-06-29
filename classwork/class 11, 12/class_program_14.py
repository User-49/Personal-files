x = int(input("enter value: "))
sum = 0
while x:
    r=x%10
    x=x//10
    sum = sum +r
print("sum = ",sum)
