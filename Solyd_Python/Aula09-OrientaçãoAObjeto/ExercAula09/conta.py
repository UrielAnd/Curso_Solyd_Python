from cliente import Cliente
class Conta(Cliente):
    def __init__(self, nome, idade, cpf, saldo, limite) -> None:
        super().__init__(nome, idade, cpf)
        self.saldo = saldo
        self.limite = limite
        
    
    def getSaldo (self):
        return print(self.saldo)
    
    def setSaque (self, valor):
        self.saldo -= valor
        return print("O valor de",valor,"foi sacado com sucesso")

    def setDeposit (self, valor):
        self.saldo += valor
        return print("O valor de",valor,"foi depositado com sucesso")






