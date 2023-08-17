numeri=[10,20,30,40,50,60,70,80,90,100]
numeri1=[]
numeri2=[]
file=open('numeri.txt','w')
for i in numeri:
    file.write(str(i)+"\n")
file.close()

file=open('numeri.txt','r')
s="a"
while s!="":
    s=file.readline()
    if s!="":
        s=s.rstrip()
        numeri1.append(s)
        numeri2.append(int(s)+0.2*int(s))
file.close()


file=open('numeri.txt','w')
for i in range(len(numeri)):
    file.write(numeri1[i]+ " --> " + str(numeri2[i]) + "\n")
file.close()