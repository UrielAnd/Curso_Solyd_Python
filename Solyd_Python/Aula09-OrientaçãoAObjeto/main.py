#import veiculo
from veiculo import Veiculo #Para uma classe funcionar no main é necesário a sua importação
from caminhão import Caminhão   #Para uma classe funcionar no main é necesário a sua importação

carroRosa = Veiculo("rosa", 4, "ford", 40)      #Modo em que se instancia um objeto

print(carroRosa)
print(type(carroRosa))
print(carroRosa.cor,carroRosa.marca,carroRosa.rodas,carroRosa.tanque)

carroAzul = Veiculo("Azul", 4, "Fiat", 25)  #Modo em que se instancia um objeto

print(carroAzul)
print(type(carroAzul))
print(carroAzul.cor,carroAzul.marca,carroAzul.rodas,carroAzul.tanque)

print(carroAzul.abastecer(8))

print(carroAzul.cor,carroAzul.marca,carroAzul.rodas,carroAzul.tanque)

print(carroAzul.abastecer(8))

print(carroAzul.cor,carroAzul.marca,carroAzul.rodas,carroAzul.tanque)

caminhão_Roxo = Caminhão("roxo", 6, "Volvo", 49, 50000) #Modo em que se instancia um objeto

print(caminhão_Roxo.cor,caminhão_Roxo.marca,caminhão_Roxo.rodas,caminhão_Roxo.tanque,caminhão_Roxo.peso)

caminhão_Roxo.abastecer(7)
print(caminhão_Roxo.tanque)