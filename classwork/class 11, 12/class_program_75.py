'''#write a python code to print a list using function .sh()
a = [1,2,3,4,5,6,7,8,9,0]
def sh(z):
  print(z)
#write py code to enter two values, pass on those to function
#called swap(). print swapped values
a = int(input('enter a: '))
b = int(input('enter b: '))
def swap(a = int(input('enter a:')), b = int(input('enter b:'))):
  print('original values:',a,b )
  a,b = b,a
  print('new value: ', a,b)
  '''
#opening a file
f = open('E:\\class_program_47.py')
print(f.read)
