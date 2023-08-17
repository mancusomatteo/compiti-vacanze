videoteca={}
chiave=""
file=open('videoteca.txt',"r")
s="a"
while s!="":
    s=file.readline()
    if s!="":
        a=s.split()
        chiave=""
        for i in range(len(a)-1):
            if i==0:
                chiave=a[i]
            else:
                chiave=chiave + " " + a[i]
        videoteca[chiave]=a[-1]
file.close()
print(videoteca)


film=input("inserisci un film: ")
if film in videoteca.keys():
    print("il regista è " + videoteca[film])
else:
    print("nessun regista trovato")

