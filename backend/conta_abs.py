from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, numero: int,
                 titular: str,
                 saldo: float = 0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def transferir(self, valor: float, conta_destino):
        pass


class ContaCorrente(Conta):

    def __init__(self,
                 numero,
                 titular,
                 saldo=1000.0,
                 limite_cheque_especial=500.0):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if self.saldo + self.limite_cheque_especial < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor + 20.00  # Taxa de 10 reais para saque
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor - 10.00  # Taxa de 10 reais para depósito
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def transferir(self, valor, conta_destino):
        if self.saldo + self.limite_cheque_especial < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.titular} realizada com sucesso. Novo saldo: {self.saldo}")


class ContaCorrentePrime(ContaCorrente):

    def __init__(self,
                 numero,
                 titular,
                 saldo=1000.0,
                 limite_cheque_especial=500.0,
                 gerente: str = "Gerente Padrão"):
        super().__init__(numero, titular, saldo, limite_cheque_especial)
        self.gerente = gerente

    def solicitar_cartao_credito(self):
        print(f"Cartão de crédito solicitado para {self.titular}. Entraremos em contato.")


class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo=0.0, aniversario=1, rendimento=0.005):
        super().__init__(numero, titular, saldo)
        self.aniversario = aniversario
        self.rendimento = rendimento

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor + 1.99  # Taxa de 1.99 reais para saque
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor - 1.99  # Taxa de 1.99 reais para depósito
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.titular} realizada com sucesso. Novo saldo: {self.saldo}")

    def render_juros(self):
        juros = self.saldo * self.rendimento
        self.saldo += juros
        print(f"Juros de {juros} aplicados. Novo saldo: {self.saldo}")


class Banco:

    def __init__(self):
        self.contas = []
        self._criar_contas_iniciais()

    def _criar_contas_iniciais(self):
        conta1 = ContaCorrentePrime(numero=1, titular="Anderson Cruz", saldo=5000.0, gerente="Carlos Silva")
        conta2 = ContaPoupanca(numero=2, titular="Maria Souza", saldo=3000.0, aniversario=15)
        conta3 = ContaCorrente(numero=3, titular="João Pereira", saldo=2000.0)

        self.contas.append(conta1)
        self.contas.append(conta2)
        self.contas.append(conta3)

    def listar_contas(self):
        for conta in self.contas:
            print(f"Conta: {conta.numero}, Titular: {conta.titular}, Saldo: {conta.saldo}")

    def executar_operacoes(self):
        print("\n--- Operações Bancárias ---\n")

        # Exemplo de operações
        self.contas[0].sacar(600.0)
        self.contas[1].depositar(400.0)
        self.contas[2].transferir(150.0, self.contas[0])

        if isinstance(self.contas[0], ContaCorrentePrime):
            self.contas[0].solicitar_cartao_credito()

        if isinstance(self.contas[1], ContaPoupanca):
            self.contas[1].render_juros()


if __name__ == "__main__":
    banco = Banco()
    banco.listar_contas()
    banco.executar_operacoes()
    banco.listar_contas()
