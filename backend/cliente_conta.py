class ClienteConta:
    nome: str
    cpf: str
    idade: int
    profissao: str

    # método construtor: todos os atributos são obrigatórios e estão privados;
    def __init__(self,
                 nome: str,
                 cpf: str,
                 idade: int,
                 profissao: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = self.__valida_idade(idade)
        self.__profissao = profissao


    def __valida_idade(self, idade):
        if idade < 18:
            raise ValueError("Idade deve ser maior ou igual a 18 anos")
        return idade

    def __str__(self):
        return f"ClienteConta(nome={self.__nome}, cpf={self.__cpf}, idade={self.__idade}, profissao={self.__profissao})"

    # getters da classe
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    @property
    def profissao(self):
        return self.__profissao



