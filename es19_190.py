comuni=["lallio","treviolo","curno","lallio","treviolo","lallio","albegno","curnasco"]
nome_comune=input("inserisci un comune: ")
cont=0
for nome in comuni:
    if nome==nome_comune:
        cont=cont+1
if cont==0:
    print("non ci sono corrispondenze per", nome_comune)
else:
    print("ci sono", cont , "corrispondenze")
