fatturati={"nord" : [] , "centro" : [] , "sud" : [] , "isole": []}
lista_fatturato=[]
i=0
for regione in fatturati:
    temp=int(input("inserisci il fatturato della regione " + regione + ": "))   
    lista_fatturato.append(temp)
    while  lista_fatturato[i]<0:
        lista_fatturato[i]=input("rinserisci il fatturato: ")
    fatturati[regione]=lista_fatturato[i]
    i=i+1

totale_fatturato=sum(lista_fatturato)
print("il totale del fatturato è: " , totale_fatturato)

for regione in fatturati:
    print("la percentuale di vendite nella regione" + regione + " è: " , fatturati[regione]/totale_fatturato*100 , "%")
