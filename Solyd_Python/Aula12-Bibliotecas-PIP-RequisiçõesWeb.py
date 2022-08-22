from shutil import ExecError
import sys  #Biblioteca padrão do python
import time
import requests     #Biblioteca do python importada pelo pip que permite fazer requisições web
#PIP -> É um gerenciador de pacotes do python, serve para intalar pacotes externos
#pip install requests|exemplo para exportar usando pip
texto = None  #Quando se que inicializar uma variável sem valor
try:    #É sempre bom usar o try nesse caso para tratar os erros, como a requisição não dê certo
    requisicao = requests.get("https://solyd.com.br")
    print(requisicao)   #Mostra o status code
    print(requisicao.status_code)   #Mostra o status code  (estado da conexão)
    print(type(requisicao))     #Mostra o tipo da variável
    print(requisicao.text)  #Mostra o codigo fonte HTML da pagina     #alguns sites tem proteção contra isso
except Exception as erro:       #Pega o exception(erro) e joga dentro da variável erro
    print("A requisição deu erro", erro)