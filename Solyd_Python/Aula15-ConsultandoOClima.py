import requests      #Biblioteca do python importada pelo pip que permite fazer requisições web
import time         #Biblioteca time para algumas funções de tempo
import json         #Biblioteca para trabalhar com json
import datetime     #Biblioteca que permite o programa saber a hora e o dia exato que o usuário está está

try:
    cidade = input ("Digite o nome da sua cidade: ")        #Input para o usuário colcar a cidade que deseja pesquisar
    req = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ cidade+ "&appid=73da14e371271df8a32c693e90b67ec8")     #Faz a requisição à api e quarda em req
    tempo = json.loads(req.text)        #Pega o get da url e adapta para um arquivo json
    if tempo["cod"] == 200:     #If para verificar a condição da conexão e vê se a cidade pequisada existe
        grausC = (tempo["main"]["temp"] - 273)      #Convete a temperatura em kelvim para Celcius
        print ("--------------------------Tempo em",cidade,"--------------------------")
        print ("Temperatura:",int(grausC),"°C")         #Printa informações resgatada pela api para o usuário
        print ("Condição:",tempo["weather"][0]["main"]) #Printa informações resgatada pela api para o usuário
        print ("Descrição:",tempo["weather"][0]["description"]) #Printa informações resgatada pela api para o usuário
        print (datetime.datetime.now()) #Mostra a data atul e a hora
        print ("-----------------------------------------------------------------------------")
    else:
        print ("Cidade não encontrada")     #Para printar se a cidade não existir
except:
    print ("Erro na conexão")       #erro caso a conexão não seja feita com sucesso