from unittest import TestCase
from datetime import datetime

from models.contas import ContaCorrete
from models.clientes import PessoaFisica


class ContaCorrenteTestCase(TestCase):

    def setUp(self):
        data_string = '1991-05-23'
        objeto_date = datetime.strptime(data_string, '%Y-%m-%d')
        self.cliente_PF = PessoaFisica(endereco="Rua A", cpf='10101001011', data_nascimento=objeto_date)
        self.conta_corrente = ContaCorrete(cliente=self.cliente_PF)
        self.conta_corrente.depositar(100)

    def test_criacao_conta_corrente(self):
        conta_corrente = ContaCorrete(cliente=self.cliente_PF)

        self.assertIsInstance(conta_corrente, ContaCorrete)

    def test_realizar_deposito_em_conta_corrente(self):
        valor_deposito = 100
        deposito = self.conta_corrente.depositar(valor_deposito)
        self.assertTrue(deposito)

    def test_realizar_saque_em_conta_corrente(self):
        valor_saque = 50
        saque = self.conta_corrente.sacar(valor_saque)
        self.assertTrue(True)

    def test_criando_nova_conta_corrente(self):
        nova_conta = self.conta_corrente.nova_conta(self.cliente_PF)
        self.assertIsInstance(nova_conta, ContaCorrete)
        self.assertNotEquals(nova_conta, self.conta_corrente)


    def test_gerando_extrato(self):
        extrato = self.conta_corrente.gerar_extrato()
        print(extrato)

