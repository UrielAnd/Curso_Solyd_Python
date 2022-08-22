#TRY e EXCEPT
#Muito semelhante com o try catch do java
from logging import exception


try:    #significa tentar  /    Tudo que está dentro de try ele tenta fazer se não dê ele lança uma esseção EXCEPT
    a = 1200/0      #isso não acontece se der erro
    #sjafkkasfk()
except ZeroDivisionError:     #Sempre que usar o try tem que usar o except  #ZeroDivisionError é uma forma de especificar o erro, entrando nesse except somente se o erro for desse tipo
    print("Divisão por 0 não existe")
except NameError:   #NameError é uma forma de especificar o erro, entrando nesse except somente se o erro for desse tipo    (erro de nome sintexe)
    print("Você digitou algo de errado")
#except: ou except Exception é para tratar qualquer tipo de erro no codigo não se sabe qual erro aconteceu
#except Exception as erro:  Joga o Exception dentro da variável erro, podendo assim identificar o tipo do erro
    #print(erro)