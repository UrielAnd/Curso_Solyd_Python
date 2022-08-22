from typing import overload
from veiculo import Veiculo
class Caminhão(Veiculo):    #Jeito em que a herança é feita em python
    def __init__(self, cor, rodas, marca, tanque, peso) -> None:    #Self semelhante ao .this do java e do c    #__Init__ Significa o construtor daquele objeto
        super().__init__(cor, rodas, marca, tanque)     #modo em que se cria o a classe para o uso em sua subclasse, bem parecida com java, pois usa super e seu construtor    
        self.peso = peso
    
    def abastecer(self, litros):    #Override
        if self.tanque < 50:
            return super().abastecer(litros)    #Retorna oque está dentro da função abastecer do veiculo, mas não o seu valor de retorno em si
        else:
            print("Tanque Cheio")
