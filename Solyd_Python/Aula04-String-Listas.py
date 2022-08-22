frase = "testando Strings e Listas"

lista = ["uriel", "andrade", "Charles"] #vetor / lista em python

print(frase[0])
print(frase[0:20])  #emprime da lista 0 até 20


print(lista)

print(lista[0:2])
print(lista[2])
print(lista[-1])    #Emprime de traz para frente

print(frase[0:5])  #emprime da lista 0 até 5

lista.append("Geralda")  #Adiciona no final lista lista / array
lista.append("Ricardo")  #Adiciona no final da lista / array
print(lista[-2])    #Emprime de traz para frente

lista.insert(1, "Gesiane")  #Coloca o conteúdo na posição

print(lista[0])

lista.append("Gesiane")  #Adiciona no final lista lista / array

gesiane = lista.count("Gesiane") #Conta quantas vezes "Gesiane" aparece na lista / array

print(lista)
print(gesiane)

quant = len(lista)  #conta a quantidade de conteúdo da lista / array

print(quant)  

print(lista.pop())    #pega semrpre o conteúdo na ultima posição da lista / array e também a retira do mesmo

separada = frase.split(",") #Separa partes da frase e tranforma em lista /array

print(separada)

print(frase.lower())    #Passa a frase para minuculo

fraseNova = frase + (" TESTE FRASE JUNTA")  #Concatena frases (variáveis str)

print(fraseNova)    