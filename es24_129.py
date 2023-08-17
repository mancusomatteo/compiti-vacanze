listino_prezzi={"marmellata":1.50  , "nutella" : 2.10 , "insalata" : 1.20 , "acqua": 0.90, "coca cola" : 1.49}
cond=True
while cond:
    percentuale=int(input("inserisci una percentuale: "))
    if percentuale <0 or percentuale>100:
        print("inserire una percentuale valida")
    else:
        cond=False
    percentuale_ridotta=percentuale/100
    for prodotto in listino_prezzi:
        listino_prezzi[prodotto]=listino_prezzi[prodotto]+percentuale_ridotta*listino_prezzi[prodotto]
        print(prodotto,":",listino_prezzi[prodotto])