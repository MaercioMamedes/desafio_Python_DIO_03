from unittest import TestCase


from models.transacoes import Saque


class SaqueTestCase(TestCase):

    def test_criacao_saque(self):
        valor_saque = 50.0
        saque = Saque(valor_saque)

        self.assertIsInstance(saque, Saque)
