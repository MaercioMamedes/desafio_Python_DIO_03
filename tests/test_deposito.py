from unittest import TestCase


from models.transacoes import Deposito


class DepositoTestCase(TestCase):

    def test_criacao_deposito(self):
        valor_deposito = 50.0
        deposito = Deposito(valor_deposito)

        self.assertIsInstance(deposito, Deposito)