class Cliente:
    def __init__(self, endereco, conta: Conta):
        self._endereco: str = endereco
        self._conta: list[Conta] = conta

    def realizar_trasacao(self, conta: Conta, transacao: Transacao):
        pass

    def adicionar_conta(self, conta: Conta):
        pass


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf: str = cpf
        self._data_nascimento: date = data_nascimento


