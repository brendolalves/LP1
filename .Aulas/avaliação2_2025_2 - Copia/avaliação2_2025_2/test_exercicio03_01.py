import unittest
from exercicio03 import search_high_values

class TestSearchHighValues(unittest.TestCase):

    def test_lista_com_um_elemento(self):
        dados = [{'high': '5.4734'}]
        esperado = ['5.4734']
        self.assertEqual(search_high_values(dados), esperado)

    def test_lista_com_dois_elementos(self):
        dados = [{'high': '5.40'}, {'high': '5.45'}]
        esperado = ['5.40', '5.45']
        self.assertEqual(search_high_values(dados), esperado)

    def test_lista_vazia(self):
        dados = []
        esperado = []
        self.assertEqual(search_high_values(dados), esperado)

    def test_valores_numericos_em_vez_de_string(self):
        dados = [{'high': 5.40}, {'high': 5.45}]
        esperado = [5.40, 5.45]
        self.assertEqual(search_high_values(dados), esperado)

    def test_valores_high_repetidos(self):
        dados = [{'high': '5.40'}, {'high': '5.40'}]
        esperado = ['5.40', '5.40']
        self.assertEqual(search_high_values(dados), esperado)

    def test_valores_high_negativos(self):
        dados = [{'high': '-5.40'}, {'high': '-5.45'}]
        esperado = ['-5.40', '-5.45']
        self.assertEqual(search_high_values(dados), esperado)

    def test_high_com_zero(self):
        dados = [{'high': '0.00'}]
        esperado = ['0.00']
        self.assertEqual(search_high_values(dados), esperado)

    def test_high_faltando_em_um_registro(self):
        dados = [{'high': '5.40'}, {}]
        with self.assertRaises(KeyError):
            search_high_values(dados)

    def test_tipo_de_entrada_incorreto(self):
        dados = "isso não é uma lista"
        with self.assertRaises(TypeError):
            for item in dados:
                _ = item['high']

    def test_high_com_valores_invalidos(self):
        dados = [{'high': 'abc'}, {'high': '5.43'}]
        esperado = ['abc', '5.43']
        self.assertEqual(search_high_values(dados), esperado)

# Executar os testes
if __name__ == '__main__':
    unittest.main()
