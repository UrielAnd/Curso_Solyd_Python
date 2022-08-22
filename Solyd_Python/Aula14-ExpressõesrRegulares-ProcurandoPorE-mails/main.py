#Procurar padrões em textos
#EX:email@dominio.com.br
#   99 98742 8742
#   220.10.12.3
import requests
import re #Biblioteca para expressões regulares #Regular expression

string_teste = "O gato é bonito"

#.search() Procura pela primeiro padrão correspondente
padrao = re.search(r"gato", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
#--------------------------------
#Exemplo do r antes da string
print("TESTE\nTESTE")
print(r"TESTE\nTESTE")
#--------------------------------
#Se existir algo dentro do padrão
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao.group())   #.group(), é para imprimir o padrão
else:
    print("Padrão não encontrado")    

string_teste = "A gata é bonita gata gatinhos gatoes"

#O ponto dentro da condição do padrão siginifica qualquer caracter
padrao = re.search(r"gat.", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao.group())   #.group(), é para imprimir o padrão
else:
    print("Padrão não encontrado") 

#findall procura por todas as incidencias dos padrões em um texto
padrao = re.findall(r"gat\w", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
#O \w siginifica que qualquer caracter que esteja naquela posição precedido de gat ele identifica o padrão(\w não é especial da linguagem mais sim dessa biblioteca)
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao)   #Nesse caso não se usa o .group, pois findall retorna uma lista contendo todos os padrões localizados
else:
    print("Padrão não encontrado") 


#findall procura por todas as incidencias dos padrões em um texto
padrao = re.findall(r"gat\w+", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
#O \w+ siginifica que vai repetir o ultimo padrão especificado uma ou mais vezes, no caso o ultimo padrão é o \w(\w não é especial da linguagem mais sim dessa biblioteca)
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao)   #Nesse caso não se usa o .group, pois findall retorna uma lista contendo todos os padrões localizados
else:
    print("Padrão não encontrado") 

#findall procura por todas as incidencias dos padrões em um texto
padrao = re.findall(r"gat\.", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
#O \. é para identificar o proprio ponto como padrão uma vez que ele sem a barra significa qualquer caracter
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao)   #Nesse caso não se usa o .group, pois findall retorna uma lista contendo todos os padrões localizados
else:
    print("Padrão não encontrado") 

#findall procura por todas as incidencias dos padrões em um texto
padrao = re.findall(r"[gat]+", string_teste)   #O r antes de uma string faz com que os caracteres especiais não funcione, a transforma em uma RAW String. Se usa esse r nessa condição porque as expressões regulares tem muita desses caracteres especiáis da linguagem
#Quando se abre colchetes se pode especificar mais de um tipo de grupo para se identificar
if padrao:      #Esse if é para checar se ele achou ou não um determinado padrão
    print(padrao)   #Nesse caso não se usa o .group, pois findall retorna uma lista contendo todos os padrões localizados
else:
    print("Padrão não encontrado") 

##############################################################################################################################
#Com esse conhecimento é possivel fazer requeste de uma pagina e procurar um certo tipo de dado nela exemplo emails
req = requests.get("https://www.ecowebdesign.com.br/atendimento")
padrao = re.findall(r"[\w \. -]+@[\w \.]+\.[\w \.]+", req.text)
if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")
#site: regex101.com -> Site que permite treinar expressões regulares