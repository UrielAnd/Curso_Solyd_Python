quant = input("Digite a quantidade de pessoas que serão convidadas para a festa: ")
listaConvidados = []
aux = 1
quant = int(quant)
print(type(quant))
while quant > 0:
    print("Digite o nome do ", aux, "° convidado: ")
    listaConvidados.append(input(""))
    aux += 1
    quant -= 1

print(listaConvidados)

######Duas outras maneiras de printar######

#for list in listaConvidados:
    #print(list)

#for list in range(len(listaConvidados)):
    #print(listaConvidados[list])
