import requests     #Biblioteca do python importada pelo pip que permite fazer requisições web
import json     #Biblioteca para trabalhar com json
import sys      #importa biblioteca em python. SYS permite ultilizar algumas coisas do sistema operacional
import time     #Biblioteca time para algumas funções de tempo
import datetime #Biblioteca que permite o programa saber a hora e o dia exato que o usuário está está

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,COP-BRL,CAD-BRL,JPY-BRL,PEN-BRL,DKK-BRL,RUB-BRL,CNY-BRL,ETH-BRL,BTC-BRL"     #Variável que contem a url da api
try:    
    while True:     #sempre acontece a cada 30 segundos
        req = requests.get(url)     #Faz a requisição à api e quarda em req
        valor = json.loads(req.text)        #Pega o get da url e adapta para um arquivo json
        print ("-------------MOEDAS PARA O REAL-------------")
        print (valor["USDBRL"]["name"],valor["USDBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["EURBRL"]["name"],valor["EURBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["GBPBRL"]["name"],valor["GBPBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["COPBRL"]["name"],valor["COPBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["CADBRL"]["name"],valor["CADBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["CNYBRL"]["name"],valor["CNYBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["JPYBRL"]["name"],valor["JPYBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["PENBRL"]["name"],valor["PENBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["DKKBRL"]["name"],valor["DKKBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["RUBBRL"]["name"],valor["RUBBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario

        print (valor["BTCBRL"]["name"],valor["BTCBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print (valor["ETHBRL"]["name"],valor["ETHBRL"]["bid"])      #printa a cotação de alguma moeda para o real, O json tem um dicionario dentro de outro dicionario, por isso se chama um dicionario primeiro e depois o atributo desejado dentro do outro dicionario
        print(datetime.datetime.now())      #Permite o programa saber a hora e o dia exato que o usuário está está
        print ("--------------------------------------------")      
        time.sleep(10)
except:
    print("Erro na conexão")    #erro caso a conexão não seja feita com sucesso