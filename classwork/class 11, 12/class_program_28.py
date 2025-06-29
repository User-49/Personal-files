n = input("enter the value: ")
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=' ')
    print()
