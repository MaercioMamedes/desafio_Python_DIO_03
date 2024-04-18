from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta) -> dict:
        # Obter a data e hora atual
        agora = datetime.now()

        # Formatar a data e hora
        data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M")
        registro = {
            'transacao': "Depósito",
            'valor': self._valor,
            'data_hora': data_hora_formatada,
        }

        return registro


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta):
        # Obter a data e hora atual
        agora = datetime.now()

        # Formatar a data e hora
        data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M")
        registro = {
            'transacao': "Saque",
            'valor': self._valor,
            'data_hora': data_hora_formatada,
        }
        return registro
