from src.backend.Conta_abs import Conta


class ContaSalario(Conta):


    def sacar(self, valor):
        if self.saldo < valor:
            return None
        else:
            self.saldo -= valor 
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def exibir_saldo(self):
        return super().exibir_saldo()