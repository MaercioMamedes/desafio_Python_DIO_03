class Cliente:
    def __init__(self, endereco):
        self._endereco: str = endereco
        self._lista_contas: list[Conta] = []

    def realizar_transacao(self, conta, transacao) -> dict:
        if conta in self._lista_contas:
            registro = transacao.registrar(conta)
            return registro

        else:
            raise Exception("erro de transação")

    def adicionar_conta(self, conta) -> None:

        if conta.cliente == self:
            self._lista_contas.append(conta)

        else:
            raise Exception("Conta nao pertence ao usuário cadastrado")


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, data_nascimento):
        super().__init__(endereco)
        self._cpf: str = cpf
        self._data_nascimento: date = data_nascimento


