comuni=["lallio","treviolo","curno","lallio","treviolo","lallio","albegno","curnasco"]
comuni_unici=[]
cont=0
for nome in comuni:
    if nome not in comuni_unici:
        comuni_unici.append(nome)
        cont+=1
print("il numero di paesi univoci è", cont)




    