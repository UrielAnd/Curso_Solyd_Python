import sys  #importa biblioteca em python. SYS permite ultilizar algumas coisas do sistema operacional

argumentos = sys.argv   #Faz com oque seja recebido argumentos de comando de linha
#arg1 metod // arg2 -n1 // arg3 -n2

def soma(n1, n2):   
    return float(n1) + float(n2)

def sub(n1, n2):
    return float(n1) - float(n2)

print(argumentos)   #O argumento n° zero é semrpe o caminnho do arquivo

if argumentos[1] == "soma":
    print("A soma desse números é", soma(argumentos[2], argumentos[3]))
elif argumentos[1] == "sub":
        print("A subtração desse números é", sub(argumentos[2], argumentos[3]))