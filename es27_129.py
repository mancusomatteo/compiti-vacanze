rubrica={"marco" : 333 , "mattia" : 222, "fabrizio" : 111}
nome=input("inserisci il nome: ")
a=False
for i in rubrica:
    if i==nome:
        print(rubrica[nome])
        a=True
if a==False:
    print("nome non presente nel dizionario")
