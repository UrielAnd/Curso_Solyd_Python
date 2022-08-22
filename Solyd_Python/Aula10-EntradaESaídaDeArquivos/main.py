#open("teste.txt")  #Método para criar arquivos  #Desse modo vai so se abrir o arquivo que está no mesmo diretorio do programa
#open("C:/root/teste.txt")  #Desse modo se abre o arquivo no caminho desejado
#No linux é nessesário usar o \\, pois \ é um caracter especial da linguagem python

#open("teste.txt", "w")      #Com o parametro w é possivel se criar o arquivo ao invés de so abri-lo
#  NomeArquivo  ModoAbertura
#O w como parametro cria um arquivo, se ele ja existir ele sobrepõe

#open("teste.txt", "r+") #r+ lê e escreve e sobrepõe. Más não cria arquivos

#open("teste.txt", "a") #a ele não apaga o arquivo so adiciona mais no arquivo. Más não cria arquivos

#open("teste.txt", "b") #O b é para arquivos binários como imagens etc

arquivo = open("ContaAté.txt", "w") 

arquivo.write("Teste no aquivo.txt criado")    #Escreve dentro do arquivo

for i in range(0, 1000001):
    arquivo.write(str(i) + "\n")        #Escreve dentro do arquivo

arquivo = open("ContaAté.txt", "r")     #r lê do arquivo
print(arquivo.read())   #Função para Lê do arquivo, ela so funciona se o arquivo estiver aberto para leitura

arquivo = open("Python.jpg", "rb")     #rb leitura de arquivos binários como imagens

print(arquivo.read())   #lê o arquivo binarios