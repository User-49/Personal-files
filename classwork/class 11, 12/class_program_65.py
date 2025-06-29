dict={}
n= int(input("no. of values you wish to put: "))
for i in range(0,n):
    a=(input("\n enter the key(employee code): "))
    x=(input("enter the value (name): "))
    y=(input("enter the value (designation): "))
    z=(input("enter the value (basic): "))
    dict[a]=(x,y,z)
print(dict)

