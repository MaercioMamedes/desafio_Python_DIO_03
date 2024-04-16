from abc import ABC, abstractmethod


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta):
        pass


class Saquer(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta):
        pass
