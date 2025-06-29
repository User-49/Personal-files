'''for i in range(4):
    cn = 65
    for j in range(i+1):
        print(chr(cn+j),end='')
    print()
'''
'''
n = int(input("enter the number: "))
print("divisor of given no. are: ",end="")
for i in range(1,n//2+1):
    if n%i == 0:
        print(i,end=",")
'''
'''
x = input("enter the str: ")
y = ""
for i in range(len(x)-1,-1,-1):
    y = y+x[i]
print(y)
print(x+y)
'''

n = int(input("enter value of n: "))
x = 0
for i in range(1,n+1):
    for j in range(i,i+1):
        x += j
        print(x,)
"""
x = input("enter the string: ")
up = []
low = []
digi = []
spac = []
for i in range(len(x)-1):
    if x[i].islower:
        low.append(x[i])
    elif x[i].isupper:
        up.append(x[i])
    elif x[i].isdigit:
        didi.append(x[i])
"""