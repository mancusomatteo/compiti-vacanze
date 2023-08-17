dizionario_voti={1001: 8 , 1002 : 6 , 1003 : 8 , 1004: 10, 1005 : 4}
somma=0
for i in dizionario_voti:
    somma=somma+dizionario_voti[i]
media=somma/len(dizionario_voti)

for i in dizionario_voti:
    if dizionario_voti[i]>media:
        print(i)

