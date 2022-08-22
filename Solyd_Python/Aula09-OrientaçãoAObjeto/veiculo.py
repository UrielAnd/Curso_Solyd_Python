class Veiculo:      #Forma que a classe é criada

    def __init__(self, cor, rodas, marca, tanque) -> None:  #É necesário o self sempre nos métodos do objeto menos em casos de super().__init__()*Herança
        self.cor = cor  #Self semelhante ao .this do java e do c
        self.rodas = rodas  #Self semelhante ao .this do java e do c
        self.marca = marca  #Self semelhante ao .this do java e do c
        self.tanque = tanque    #Self semelhante ao .this do java e do c

    def abastecer(self, litros):    #Abastace o veiculo método
        self.tanque += litros
        return "Carro Abastecido"