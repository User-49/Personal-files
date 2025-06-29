a = open('e:\\binaryk.bin', 'rb+')
from pickle import *
dump("hell's paradise",a)
a.seek(0)
x = load(a)
print(x)
a.close()
