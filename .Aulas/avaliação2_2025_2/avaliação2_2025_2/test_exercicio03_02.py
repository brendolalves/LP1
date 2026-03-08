import unittest
from exercicio03 import search_low_values

import unittest

class TestSearchLowValues(unittest.TestCase):

    def test_um_elemento(self):
        dados = [{'low': '5.30'}]
        esperado = ['5.30']
        self.assertEqual(search_low_values(dados), esperado)

    def test_dois_elementos(self):
        dados = [{'low': '5.30'}, {'low': '5.25'}]
        esperado = ['5.30', '5.25']
        self.assertEqual(search_low_values(dados), esperado)

    def test_lista_vazia(self):
        dados = []
        esperado = []
        self.assertEqual(search_low_values(dados), esperado)

    def test_valores_como_float(self):
        dados = [{'low': 5.30}, {'low': 5.25}]
        esperado = [5.30, 5.25]
        self.assertEqual(search_low_values(dados), esperado)

    def test_low_repetido(self):
        dados = [{'low': '5.25'}, {'low': '5.25'}]
        esperado = ['5.25', '5.25']
        self.assertEqual(search_low_values(dados), esperado)

    def test_low_zero(self):
        dados = [{'low': '0.00'}]
        esperado = ['0.00']
        self.assertEqual(search_low_values(dados), esperado)

    def test_low_negativo(self):
        dados = [{'low': '-5.00'}, {'low': '-4.90'}]
        esperado = ['-5.00', '-4.90']
        self.assertEqual(search_low_values(dados), esperado)

    def test_low_ausente(self):
        dados = [{'low': '5.30'}, {}]
        with self.assertRaises(KeyError):
            search_low_values(dados)

    def test_tipo_de_entrada_incorreto(self):
        dados = "isso não é uma lista"
        with self.assertRaises(TypeError):
            search_low_values(dados)

    def test_valores_low_invalidos(self):
        dados = [{'low': 'abc'}, {'low': '5.20'}]
        esperado = ['abc', '5.20']
        self.assertEqual(search_low_values(dados), esperado)

# Executar os testes
if __name__ == '__main__':
    unittest.main()
