from unittest import TestCase
from datetime import datetime

from models.clientes import PessoaFisica


class PessoaFisicaTestCase(TestCase):
    def test_criacao_de_pessoa_fisica(self):
        # String da data
        data_string = '1991-05-23'

        # Converter a string para um objeto datetime
        objeto_date = datetime.strptime(data_string, '%Y-%m-%d')

        pessoa_fisica = PessoaFisica(endereco="Rua A", cpf='10101001011', data_nascimento=objeto_date)

        self.assertIsInstance(pessoa_fisica, PessoaFisica)

