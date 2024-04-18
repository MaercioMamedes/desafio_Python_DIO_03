class Historico:
    def __init__(self):
        self._transacoes: list[Transacao] = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

