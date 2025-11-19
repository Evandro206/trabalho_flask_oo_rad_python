from src.orientacao_objetos.conta import Conta


class ContaCorrente(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor + 10.00
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")


class ContaCorrenteGerentes(ContaCorrente):

    def depositar(self, valor):
        confirmacao = input("Será cobrada uma taxa de um real, Gostaria de continuar? (s/n)")
        if confirmacao.lower().strip() == 's':
            super().depositar(valor)
            self.saldo -= 1.00
        else:
            print('Depósito não realizado!!!')


conta_corrente_gerente = ContaCorrenteGerentes(
    cliente="Anderson Cruz",
    agencia=123456,
    banco="Banco do Brasil",
    conta=123456,
    saldo=100.00
)

print(conta_corrente_gerente.saldo)

conta_corrente_gerente.sacar(50.00)
print(conta_corrente_gerente)
conta_corrente_gerente.depositar(100.00)
print(conta_corrente_gerente)
