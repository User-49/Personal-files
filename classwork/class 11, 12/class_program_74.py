'''x = input('enter string: ')
wrd = len(x.split(' '))
lin = len(x.split('.'))
print('no. of words: ',wrd)
print('no. of lines: ', lin)
'''
'''
d = dict()
while True:
  print('welcome to the program, what do you wish to do?')
  print('1)input values\n2)search value\n3)delete value')
  print('4)exit')
  choice = int(input('enter choice: '))
  if choice == 1:
    k = input('enter key: ')
    v = input('value: ')
    d[k] = v 
  elif choice == 2:
    k = input('enter key to search: ')
    print('value: ',d[k])
  elif choice == 3:
    k = input('enter key to delete: ')
    del def[k]
    print('the given item was deleted.')
  elif choice == 4:
    print('you have exited the program')
    break
  else:
    print('invalid choice, try again.')
    print('-'*64)
'''
l = list()
for i in 'asdfg':
  l.append(int(input('enter element: ')))
x = l[0]
for i in l:
  if x < i:
    x = i
print('highest value is : ',x)
