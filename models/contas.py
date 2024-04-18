from .transacoes import Deposito, Saque

class Conta:
    def __init__(self, agencia: str, cliente: Cliente):
        self._saldo = 0
        self._numero: int
        self._agencia: str = agencia
        self._cliente: Cliente = cliente
        self._historico: Historico

        self._gerar_numero_conta()

    def _gerar_numero_conta(self):
        pass

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> Conta:
        pass

    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:

        """Criar transacao """
        deposito = Deposito(valor)
        self._cliente.realizar_transacao(self, deposito)

        return True


class ContaCorrete(Conta):
    def __init__(self, agencia: str, cliente: Cliente):
        super().__init__(agencia, cliente)
        self._limite: float
        self._limite_saques: int
