#wpc to enter ten names into the text file named a.txt
f = open('e:\\a.txt', 'w+')
for i in range(2):
  f.write(input('\nenter name: '))
f.seek(0)
print(f.read())
f.close()

