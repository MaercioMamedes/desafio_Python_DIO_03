from abc import ABC, abstractmethod


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta) -> dict:
        registro = {'dado': "dicionário com dados da operação"}
        return registro


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta):
        registro = {'dado': "dicionário com dados da operação"}
        return registro
