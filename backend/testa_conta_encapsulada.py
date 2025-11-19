from src.orientacao_objetos.conta_encpasulada import ContaEncapsulada as Conta


class TestaContaEncapsulada:
    def testa_conta(self):

        conta = Conta("Anderson Barboza da Cruz",
                      "Banco do Brasil",
                      "0001",
                      "12345-6",
                      1000.0)

        conta_02 = Conta("Anderson Barboza da Cruz",
                         "Banco do Brasil",
                         "0001",
                         "12345-6",
                         1000.0)
        conta_03 = conta

        print(f"Saldo inicial: {conta.saldo}")

        conta.depositar(500.0)
        print(f"Saldo após depósito: {conta.saldo}")

        conta.sacar(200.0)
        print(f"Saldo após saque: {conta.saldo}")

        try:
            conta.sacar(2000.0)
        except ValueError as e:
            print(e)

        conta.depositar(-100.0)  # Teste de depósito inválido
        print(f"Saldo final: {conta.saldo}")

        if conta == conta_02:
            print("As contas são iguais.")
        else:
            print("As contas são diferentes.")

        if conta == conta_03:
            print("As contas são iguais.")
        else:
            print("As contas são diferentes.")


if __name__ == "__main__":
    test = TestaContaEncapsulada()
    test.testa_conta()
