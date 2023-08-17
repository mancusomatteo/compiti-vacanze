limiti_sup=[15000,28000,55000,75000,10**12]
limiti_inf=[0,15000,28000,55000,75000]
aliquota=[23,27,38,41,43]
imp_fasce_prec=[0,3450,6960,17220,25420]
importi_dovuti={}
for i in range(5):
    importi_dovuti[limiti_sup[i]] = [limiti_inf[i],imp_fasce_prec[i],aliquota[i]]

reddito=float(input("inserisci il reddito: "))

while reddito<0:
    reddito=float(input("valore negativo, rinserisci il valore: "))


for i in range(5):
    if reddito>limiti_inf[i] and reddito<limiti_sup[i]:
        imposta=importi_dovuti[limiti_sup[i]][1] + (reddito - importi_dovuti[limiti_sup[i]][0])*importi_dovuti[limiti_sup[i]][2]/100
print("l'imposta dovuta è: "  , imposta)

media_imposta=imposta/reddito*100
print("la media di imposta è: "  , media_imposta ,"%")
