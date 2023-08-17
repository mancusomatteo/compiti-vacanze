nome=input("inserisci il nome desiderato: ")
cognome=input("inserisci il cognome desiderato: ")
citta=input("inserisci la citta desiderata: ")
nazione=input("inserisci la nazione desiderata: ")
anagrafica=nome + ";" + cognome + ";" + citta + ";" + nazione 
file = open('anagrafica.txt' , 'w')
file.write(anagrafica)
file.close()