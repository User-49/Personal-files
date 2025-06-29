L = [12,5,20,30,3]
for i in range(len(L)):
    if L[i]%2==1:
        L[i] = L[i]*5
    else:
        L[i] = L[i]*10
print(L)
