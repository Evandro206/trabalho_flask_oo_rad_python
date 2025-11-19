from src.orientacao_objetos.cliente_conta import ClienteConta


class TestaClienteNovo:
    cliente = ClienteConta("Anderson Cruz",
                           "123.456.789-00",
                           18,
                           "Desenvolvedor")

    print(cliente)
    print(cliente.nome)
    print(cliente.cpf)
    print(cliente.idade)
    print(cliente.profissao)
