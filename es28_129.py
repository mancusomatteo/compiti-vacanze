codifica_comuni={}

for i in range(3):
    cap=int(input("inserisci il cap del comune : "))
    citta=input("inserisci il nome della città corrispondente al cap: ")
    codifica_comuni[cap]=citta
print(codifica_comuni)

cap_in=int(input("inserisci un cap da cercare: "))

if cap_in in codifica_comuni:
    print(codifica_comuni[cap_in])
else:
    print("cap non presente all'interno del dizionario")

citta_in=input("inserisci una  città da cercare: ")

a=False
for cap, citta in codifica_comuni.items():
    if citta==citta_in:
        print(cap)
        a=True
if a==False:
    print("la città inserita non è presente nel dizionario")



