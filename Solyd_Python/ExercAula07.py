def maior(tupla):
    aux=tupla[0]
    for i in tupla:
        if int(aux) < i:
            aux = i
    return aux

def menor(tupla):
    aux=tupla[0]
    for i in tupla:
        if int(aux) > i:
            aux = i
    return aux
        

tupla = (91,24,51,56,102,12,2,90,96,1040,12,1.4)

print("O maior número dessa coleção é:", maior(tupla))
print("O maior número dessa coleção é:", menor(tupla))