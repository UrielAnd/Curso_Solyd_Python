import requests #Biblioteca do python importada pelo pip que permite fazer requisições web
import json     #Biblioteca para trabalhar com json

#Função para fazer a requisição à api
def requisicao(titulo):
    req = None  #Quando se que inicializar uma variável sem valor
    try:
        req = requests.get("https://www.omdbapi.com/?t=" + titulo + "&type=movie&apikey=e667d3b5")     #Nesse caso a concatenação é feita dessa forma, com o +. Pois se não é considerado com um parametro amais na função
        dicionario = json.loads(req.text)   #json.loads, pega um texto estruturado em json e tranforma em dicinario do python
        return dicionario       #Retorna o dicionario
    except:
        print("Erro na conexão")
        exit()  #exit(), é uma função que termina a execução do programa
    #print (req.text)

def printa_filme(filme):
    print("Título:",filme["Title"])     #Atraves do dicionario filme ele procura os seu atributo de Title
    print("Ano:",filme["Year"])     #Atraves do dicionario filme ele procura os seu atributo de Year
    print("Atores:",filme["Actors"])    #Atraves do dicionario filme ele procura os seu atributo de Actors
    print("Diretor:",filme["Director"])     #Atraves do dicionario filme ele procura os seu atributo de Director
    print("Nota:",filme["imdbRating"])      #Atraves do dicionario filme ele procura os seu atributo de imbRating
    print("Premios:",filme["Awards"])   #Atraves do dicionario filme ele procura os seu atributo de Awards
    print("Poster:",filme["Poster"])    #Atraves do dicionario filme ele procura os seu atributo de Poster


esc = input("Digite aqui o nome do filme: ")
filme = requisicao(esc)
if filme["Response"] == "False":        #Se a resposta do contida no dicionario for False, o programa fala que não o encontrou o filme 
    print("Filme não encontrado")
else:
    printa_filme(filme)     #Função para printar o filme