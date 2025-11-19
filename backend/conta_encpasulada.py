from src.orientacao_objetos.cliente_conta import ClienteConta

class ContaEncapsulada:

    def __init__(self,
                 cliente: ClienteConta,
                 banco: str,
                 agencia: str,
                 conta: str,
                 saldo: float =10.00):
        self.__cliente = cliente
        self.__banco = banco
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    def __str__(self):
        return (f"Conta(cliente={self.__cliente}, "
                f"banco={self.__banco}, agencia={self.__agencia}, "
                f"conta={self.__conta}, saldo={self.__saldo})")

    def __repr__(self):
        return (f"Conta(cliente={self.__cliente}, "
                f"banco={self.__banco}, agencia={self.__agencia}, "
                f"conta={self.__conta}, saldo={self.__saldo})")


    def __eq__(self, other):
        if not isinstance(other, ContaEncapsulada):
            return NotImplemented
        return (self.__cliente == other.__cliente and
                self.__banco == other.__banco and
                self.__agencia == other.__agencia and
                self.__conta == other.__conta and
                self.__saldo == other.__saldo)



    def sacar(self, valor):
        if self.__saldo < valor:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.__saldo}")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.__saldo}")

    def transferir(self, valor, conta_destino):
        if self.__saldo < valor:
            print("Saldo insuficiente para transferência")
        else:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            print(
                f"Transferência de {valor} para {conta_destino.cliente} realizada com sucesso. Novo saldo: {self.__saldo}")

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo



cliente = ClienteConta("Anderson Cruz",
                       cpf="123.456.789-00",
                       idade=18,
                       profissao="Desenvolvedor")



conta_01 = ContaEncapsulada(cliente=cliente,
                            banco="Banco do Brasil",
                            agencia="0001",
                            conta="12345-6",
                            saldo=1000.00)

#print(conta_01)
print(conta_01.cliente.idade)
print(conta_01.saldo)
print(conta_01.cliente.nome)