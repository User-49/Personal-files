#tuples are immutable
'''wap to create a static tuple if a%10:*5
if a%3:*10'''
a=eval(input("enter the tuple: "))
a = list(a)
for i in range(len(a)-1):
    if a[i]%10==0:
        a[i]*=5
    elif a[i]%3==0:
        a[i]*=10
print(tuple(a))

