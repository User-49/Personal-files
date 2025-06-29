sd={}
i=1
n = int(input("enter the no. of records you eant to put: "))
while i<=n:
    adm = int(input("enter admn: "))
    rno=int(input("enter roll no.: "))
    name= input("enter name: ")
    per=float(input("enter persentage: "))
    rec=(adm,name,per)
    sd[rno]=rec
    i+=1
a=sd.keys()
for i in a:
    print(i,"------",sd[i])
