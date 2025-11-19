from src.orientacao_objetos.conta_dataclass import ContaDataClass


class TestaContaDataClass:
    def testa_conta(self):
        conta = ContaDataClass("Anderson Cruz",
                               "Banco do Brasil",
                               "0001", "12345-6",
                               1000.00)

        conta_02 = ContaDataClass("Maria Silva",
                                  "Caixa Econômica",
                                  "0001",
                                  "98765-4",
                                  500.00)

        print(conta)
        print(conta_02)

        conta.transferir(200.00, conta_02)
        print(conta)
        print(conta_02)


if __name__ == "__main__":
    test = TestaContaDataClass()
    test.testa_conta()
