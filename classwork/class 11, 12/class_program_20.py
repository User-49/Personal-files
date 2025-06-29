x = int(input("enter value: "))
y = 1
z = 5
for i in range(1,x):
    if y<=i:
        print(y)
        y,z=y+z,z*2
        
