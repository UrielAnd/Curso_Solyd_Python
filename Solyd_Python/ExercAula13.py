import requests
import json
from time import sleep

def lista_filmes(titulo):
    lista = []
    print("Pesquisando...")
    for i in range(1, 101):
        try:
            #sleep(2)
            req = requests.get("https://www.omdbapi.com/?s=" + titulo + "&type=movie&page=" + str(i) + "&apikey=e667d3b5")
            dicionario = json.loads(req.text)
            if dicionario["Response"] == "False":
                break
            else:
                for filme in dicionario["Search"]:
                    lista.append(filme["Title"])
                    lista.append("(" + filme["Year"] +")")
        except Exception as erro:
            print("Falha na conexão", erro)
            exit()
    return lista
titulo = input("Digite o nome do filme: ") 

filmes = lista_filmes(titulo)
print("Filmes encontrados: ", len(filmes))
for i in filmes:
    print(i)

