'''d = dict()
for i in range(int(input('enter no. of values to add:'))):
  k = int(input('enter admin no.'))
  x = input('name:')
  y = input('class:')
  z = input('roll. no.:') 
  d[k] = [x,y,z]
print('/nto print and delete the record')
x = int(input('enter admin no.:'))
print('name:/t',d[x][0],'/nclass:/t',d[x][1],'/nroll. no.:\n',d[x][2])
del d[x]
'''
#write a menu driven program to do the following  in a dictionary
#1)entry 2)search 3)del 4)shoe dict 5)exit
d = dict()
while True:
  print('what do you wish to do-')
  print('1)entry\n2)search\n3)del\n4)show dict\n5)exit')
  choice = int(input('\nenter choice: '))
  if choice == 1:
    key = input('enter key :')
    val = eval(input('enter value :'))
    d[key] = val
  elif choice == 2:
    k = input('enter key to search: ')
    if k in d:
      print(k, '=>', d[k])
    else:
      print('key not in list: ')
  elif choice == 3:
    x = input('enter key to delete :')
    if x in d:
      del d[x]
    else:
      print('key not in dict')
  elif choice == 4:
    for i in d:
      print(i, ':', d[i])
  elif choice == 5:
    print('you have exited the program')
    break
  else:
    print('invalid option, try again')
  print('-'*65)
print('*'*79)
