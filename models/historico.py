class Historico:
    def __init__(self):
        self._transacoes: list[Transacao] = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
