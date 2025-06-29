#open a file named a.txt in writting mode. Write few lines into it
'''
f = open('E:\\python.txt', 'w')
f.write('nyampasu-\nyabure kabure no yabu ishaga')
f.close()
'''
#open a txt in reading mode display data
f = open('E:\\python.txt','r')
x = f.readlines(63)
f.close
print(x)
