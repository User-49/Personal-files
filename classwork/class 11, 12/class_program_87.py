import mysql.connector as connector
mydb = connector.connect(host='localhost',user = 'root',password='kapil2006@')
mycursor = mydb.cursor()
mycursor.execute('show databases')
for i in mycursor:
    print(i)