import unittest
from exercicio02 import extrair_dados

class TestExtrairDados(unittest.TestCase):

    def test_lista_com_um_elemento(self):
        entrada = [{'cep': '01001-000', 'localidade': 'São Paulo', 'estado': 'São Paulo'}]
        esperado = [('01001-000', 'São Paulo', 'São Paulo')]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_lista_com_dois_elementos(self):
        entrada = [
            {'cep': '01001-000', 'localidade': 'São Paulo', 'estado': 'São Paulo'},
            {'cep': '04003-010', 'localidade': 'São Paulo', 'estado': 'São Paulo'}
        ]
        esperado = [
            ('01001-000', 'São Paulo', 'São Paulo'),
            ('04003-010', 'São Paulo', 'São Paulo')
        ]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_lista_vazia(self):
        self.assertEqual(extrair_dados([]), [])

    def test_cep_em_formato_diferente(self):
        entrada = [{'cep': '01001000', 'localidade': 'São Paulo', 'estado': 'SP'}]
        esperado = [('01001000', 'São Paulo', 'SP')]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_dados_com_valores_none(self):
        entrada = [{'cep': None, 'localidade': None, 'estado': None}]
        esperado = [(None, None, None)]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_faltando_cep(self):
        entrada = [{'localidade': 'São Paulo', 'estado': 'SP'}]
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_faltando_localidade(self):
        entrada = [{'cep': '01001-000', 'estado': 'SP'}]
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_faltando_estado(self):
        entrada = [{'cep': '01001-000', 'localidade': 'São Paulo'}]
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_elemento_extra_na_entrada(self):
        entrada = [{
            'cep': '01001-000', 'localidade': 'São Paulo', 'estado': 'SP',
            'bairro': 'Sé', 'ddd': '11'
        }]
        esperado = [('01001-000', 'São Paulo', 'SP')]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_tipo_errado_de_entrada(self):
        entrada = "isso não é uma lista"
        with self.assertRaises(TypeError):
            extrair_dados(entrada)

# Executar os testes
if __name__ == "__main__":
    unittest.main()
