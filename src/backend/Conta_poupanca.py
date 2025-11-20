from src.backend.Conta_abs import Conta


class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo = 0):
        super().__init__(numero, titular, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            return None
        else:
            self.saldo -= valor 
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor * 1.05
        return self.saldo

    def exibir_saldo(self):
        return super().exibir_saldo()