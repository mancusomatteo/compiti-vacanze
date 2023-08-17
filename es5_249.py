province=["Bergamo","Milano","Brescia","Cremona","Lecco","Lodi","Mantova","Monza e Brianza","Pavia","Como","Sondrio","Varese"]
province1=[]
file=open('province.txt','w')
for i in province:
    file.write(i+"\n")
file.close()

file=open('province.txt','r')
s="a"
while s!="":
    s=file.readline()
    province1.append(s)
file.close()
province1.sort()
for i in province1:
    print(i)


