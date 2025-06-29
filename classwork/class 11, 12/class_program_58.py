l=[]
x= input("enter the element: ")
while x!="no":
    l.append(int(x))
    x = input("enter the element: ")
print(l)
print("the position of element : ",end=",")
flag = 0
y = int(input("the element you wish to search: ")
for i in range(len(l)-1):
    if l[i]==y:
        print(i+1,end=",")
        flag = 1
if flag = 0:
        print("is not found in the given list")
        
    
