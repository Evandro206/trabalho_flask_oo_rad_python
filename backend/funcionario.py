from abc import ABC, abstractmethod


class Funcionario(ABC):
    """
        Atr:
        nome: str
        setor: str
        salario: float
        bonus: float
    """

    def __init__(self, nome, setor, salario):
        self.nome = nome
        self.setor = setor
        self.salario = salario
        self.bonus = self.retorna_bonus()

    @abstractmethod
    def retorna_bonus(self):
        pass


    @abstractmethod
    def retorna_salario(self):
        pass


class Analista(Funcionario):


class Supervisor(Funcionario):
    pass


class Gerente(Funcionario):
    pass
