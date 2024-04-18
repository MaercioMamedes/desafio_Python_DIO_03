from unittest import TestCase

from models.clientes import Cliente


class ClienteTestCase(TestCase):
    def test_criacao_de_cliente(self):

        cliente = Cliente("Rua A")

        self.assertIsInstance(cliente, Cliente)

