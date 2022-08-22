listaNomes = ["Guilherme", "Marcelo", "Ricardo", "João"]
print(listaNomes)

for nome in listaNomes:     #(ISSO ACONTECE ENQUANTO A LISTA NÃO CHEGA AO FIM)Para cada nome dentro de listaNomes print(nome) (Ou seja pecorre todo a lista / array para printar cada posição da mesma).
    print (nome)

listaNumeros = range(5)     #função range cria uma lista / array de números de 0 a 5

for num in listaNumeros:
    print(num)

listaNumeros = range(5,10) #Cria uma lista de números entre 5(INCLUSO) e 10
print("\n")
for num in listaNumeros:
    print(num)

#O 2 na função de baixo é o passo (steep)
listaNumeros = range(0,100,2) #Cria uma lista de números entre 0(INCLUSO) e 100 de 2 em 2
print("\n")
for num in listaNumeros:
    print(num)

for i in range(4):      #Dessa forma é nessesário se saber o tamanho da lista / array
    print(listaNomes[i])    

for i in range(len(listaNomes)):      #Dessa forma não é nessesário se saber o tamanho da lista / array
    print(listaNomes[i])    

i = 0
while i < 10:
    print(".")
    i += 1    

while i < 10:
    print(".")
    i += 1
    break  #Sai do laço de repetição       
     