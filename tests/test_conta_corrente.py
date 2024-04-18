from unittest import TestCase
from datetime import datetime

from models.contas import ContaCorrete
from models.clientes import PessoaFisica


class ContaCorrenteTestCase(TestCase):

    def setUp(self):
        data_string = '1991-05-23'
        objeto_date = datetime.strptime(data_string, '%Y-%m-%d')
        self.cliente_PF = PessoaFisica(endereco="Rua A", cpf='10101001011', data_nascimento=objeto_date)

    def test_criacao_conta_corrente(self):
        conta_corrente = ContaCorrete(cliente=self.cliente_PF)

        self.assertIsInstance(conta_corrente, ContaCorrete)
