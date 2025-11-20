from abc import ABC, abstractmethod
from src.backend.Cliente import Cliente
import random


class Conta(ABC):

    def __init__(self,
                 titular: Cliente,
                 saldo: float = 0.0):
        self.numero = random.randint(1, 10000000)
        self.agencia = random.randint(1, 20)
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass

    def exibir_saldo(self):
        return self.saldo