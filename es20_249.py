fatture={}
file=open('fatture.txt',"r")
s="a"
while s!="":
    s=file.readline()
    if s!="":
        a=s.split()
        fatture[a[1]]=a[0]
file.close()
print(fatture)


codice_cliente=input("inserisci un codice cliente: ")
if codice_cliente in fatture.values():
    count=0
    for cd_fattura,cliente in fatture.items():
        if cliente==codice_cliente:
            count=count+1
    print("il cliente ha pagato ", count , " volte")
else:
    print("nessun cliente trovato")