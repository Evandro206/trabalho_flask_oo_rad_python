from dataclasses import dataclass


@dataclass
class ContaDataClass:
    cliente: str
    banco: str
    agencia: str
    conta: str
    saldo: float = 10.00

    def sacar(self, valor: float) -> None:
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            print("Valor de depósito inválido")
            return
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def transferir(self, valor: float, conta_destino: 'Conta') -> None:
        if self.saldo < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.cliente} realizada com sucesso. Novo saldo: {self.saldo}")

