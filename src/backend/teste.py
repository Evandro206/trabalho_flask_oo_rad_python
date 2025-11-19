def criar_conta(
        nome,
        nome_banco,
        numero,
        agencia,
        saldo_inicial=10.00
):
    return {
        "nome": nome,
        "nome_banco": nome_banco,
        "numero": numero,
        "agencia": agencia,
        "saldo": saldo_inicial
    }


def imprimir_conta(conta):
    print(
        f"""Olá {conta['nome']}, 
    obrigado por criar uma conta em nosso banco {conta['nome_banco']}. 
    Sua agência é {conta['agencia']}, 
    conta {conta['numero']} e 
    seu saldo {conta['saldo']} já está disponível para saque."""
    )


def sacar(conta, valor):
    if conta['saldo'] < valor:
        print("Saldo insuficiente")
    else:
        conta['saldo'] -= valor
        print(f"Saque de {valor} realizado com sucesso. Novo saldo: {conta['saldo']}")


def depositar(conta, valor):
    conta['saldo'] += valor
    print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {conta['saldo']}")


conta_01 = criar_conta(
    "Anderson Cruz",
    "Banco do Brasil",
    "12345-6",
    "0001",
    10.00
)

sacar(conta_01, 500.00)
depositar(conta_01, 1000.00)

imprimir_conta(conta_01)

print(conta_01)
conta_01['saldo'] += 1000.00
conta_01['saldo'] -= 500.00

print(conta_01)

int()
str()