dizionario_voti={1001: 8 , 1002 : 6 , 1003 : 8 , 1004: 10, 1005 : 4}
lista_voti=[]
voti_unici=[]
for i in dizionario_voti.values():
    lista_voti.append(i)

lista_voti.sort()
print(lista_voti)

for i in lista_voti:
    if  i not in voti_unici:
        voti_unici.append(i)

print(voti_unici)

