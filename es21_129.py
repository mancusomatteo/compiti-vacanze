numeri1=[120,10,100,99,101,0,-50,10.250]
numeri2=[]
for i in range(len(numeri1)):
    if numeri1[i]<100:
        numeri2.append(numeri1[i]*2)
    elif numeri1[i]>=100:
        numeri2.append(numeri1[i]*3)
print(numeri2)
