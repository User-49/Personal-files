#wap a dynamic list create 2 different list the no. which are odd and which are even
x = input('enter the value: ')
l = []
odd = []
even = []
while x != 'no':
    l.append(int(x))
    x = input('enter value: ')
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('list of odd values: ',odd)
print('list of even elements:',even)
