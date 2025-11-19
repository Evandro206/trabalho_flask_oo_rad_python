class Conta:

    def __init__(self,
                 cliente: str,
                 banco: str,
                 agencia: int,
                 conta: int,
                 saldo: float = 10.00):
        self.cliente = cliente
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"Conta(cliente={self.cliente}, banco={self.banco}, agencia={self.agencia}, conta={self.conta}, saldo={self.saldo})"


    def __repr__(self):
        return f"Conta(cliente={self.cliente}, banco={self.banco}, agencia={self.agencia}, conta={self.conta}, saldo={self.saldo})"

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.cliente} realizada com sucesso. Novo saldo: {self.saldo}")


