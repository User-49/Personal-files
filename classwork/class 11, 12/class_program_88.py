import mysql.connector as c
try:
    mydb = c.connect(host='localhost', user='root', password='kapil2006@')
    c = mydb.cursor()
except Error as e:
    print(e)
