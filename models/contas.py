from abc import ABC, abstractmethod
import time

from .transacoes import Deposito, Saque
from .historico import Historico


class Conta(ABC):
    _contas_criadas = {}

    def __init__(self, cliente, numero: int = 0):
        self._saldo = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: Cliente = cliente
        self._historico: Historico = Historico()

        if self._numero in self._contas_criadas.keys():
            raise Exception("Número de conta ja cadastrada")

        elif self._numero == 0:

            numero_conta = len(self._contas_criadas.keys())
            self._numero = numero_conta

        self._cliente.adicionar_conta(self)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass


class ContaCorrete(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)
        self._limite: float
        self._limite_saques: int

    def sacar(self, valor: float) -> bool:
        try:
            saque = Saque(valor)
            transacao = self._cliente.realizar_transacao(self, saque)
            self._historico.adicionar_transacao(transacao)

            self._saldo -= valor

        except Exception:
            return False

    def depositar(self, valor: float) -> bool:

        try:
            """VERIFICAR CONDIÇÕES DE LIMITES"""
            deposito = Deposito(valor)
            transacao = self._cliente.realizar_transacao(self, deposito)
            self._historico.adicionar_transacao(transacao)

            self._saldo += valor

            return True

        except Exception:
            return False
