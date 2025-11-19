from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, titular, saldo=0.0):
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

    def __str__(self):
        return f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0.0, limite=500.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada para {conta_destino.titular}.")
        else:
            print("Saldo insuficiente para transferência.")


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0, rendimento=0.005):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento  # 0.5% ao mês

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada para {conta_destino.titular}.")
        else:
            print("Saldo insuficiente para transferência.")

    def render_juros(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        print(f"Rendimento aplicado: R${ganho:.2f}")


class ContaSalario(Conta):
    def __init__(self, numero, titular, saldo=0.0, empresa=""):
        super().__init__(numero, titular, saldo)
        self.empresa = empresa

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        print("Depósito não permitido diretamente. Apenas a empresa pode depositar.")

    def deposito_empresa(self, valor):
        self.saldo += valor
        print(f"Depósito de salário R${valor:.2f} realizado pela empresa {self.empresa}.")

    def transferir(self, valor, conta_destino):
        print("Transferências não são permitidas em conta salário.")


class Banco:
    def __init__(self):
        self.contas = []
        self._criar_contas()

    def _criar_contas(self):
        """Cria 6 contas diferentes"""
        self.contas.append(ContaCorrente("001", "Anderson", 1000))
        self.contas.append(ContaCorrente("002", "João", 200))
        self.contas.append(ContaPoupanca("003", "Maria", 500))
        self.contas.append(ContaPoupanca("004", "Ana", 1500))
        self.contas.append(ContaSalario("005", "Carlos", 0, "TechCorp"))
        self.contas.append(ContaSalario("006", "Fernanda", 0, "DataFlow"))

    def executar_operacoes(self):
        """Executa métodos de forma polimórfica"""
        print("\n--- Executando operações polimórficas ---\n")

        for conta in self.contas:
            print(f"Operando com {conta.titular} ({conta.__class__.__name__})")

            # As operações abaixo são chamadas polimórficas:
            conta.depositar(200)
            conta.sacar(100)

            # Tenta transferir para a primeira conta (pode ou não ser permitido)
            conta.transferir(50, self.contas[0])

            print(conta)
            print("-" * 50)


# ===================== TESTE =====================
if __name__ == "__main__":
    banco = Banco()
    banco.executar_operacoes()
