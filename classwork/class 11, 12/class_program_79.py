f=open("e:\\python.txt")
print(len(f.read()))
f.seek(0)
print(f.read())
print(f.tell())
f.close()



f=open("e:\p.txt",'w+')
str="This is democ country.\n I live in India.\n This is my country."

#writelines to upload list into the file
f.writelines(["this is me\n", "Hi\n","How r\n"])

#write to enter lines as a string
f.write(str)
f.seek(0)
print("Current position of cursor is= ",f.tell())
print(f.read())

#reading a file from the beginning by storing into a variable
f.seek(0)
lines=f.readlines()
#print(lines)
for line in lines: 
  print(f.readline())

f.close()


