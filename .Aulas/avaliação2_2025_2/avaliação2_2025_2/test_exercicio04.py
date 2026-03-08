import unittest
from exercicio04 import listar_nomes_personagens

class TestListarNomesPersonagens(unittest.TestCase):

    def test_lista_com_dois_personagens(self):
        dados = [
            {'name': 'Luke Skywalker'},
            {'name': 'C-3PO'}
        ]
        esperado = ['Luke Skywalker', 'C-3PO']
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_lista_com_dois_personagens_completos(self):
        dados = [
            {'name': 'Luke Skywalker','gender':'male'},
            {'name': 'C-3PO','gender': 'n/a'}
        ]
        esperado = ['Luke Skywalker', 'C-3PO']
        self.assertEqual(listar_nomes_personagens(dados), esperado)
        
    def test_lista_vazia(self):
        dados = []
        esperado = []
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_personagem_sem_nome(self):
        dados = [{'height': '172'}]
        esperado = [None]
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_personagem_com_nome_vazio(self):
        dados = [{'name': ''}]
        esperado = ['']
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_personagem_com_nome_none(self):
        dados = [{'name': None}]
        esperado = [None]
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_personagem_com_outros_campos_apenas(self):
        dados = [{'height': '167', 'mass': '75'}]
        esperado = [None]
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_nome_em_tipo_numerico(self):
        dados = [{'name': 12345}]
        esperado = [12345]
        self.assertEqual(listar_nomes_personagens(dados), esperado)

    def test_entrada_com_elemento_nao_dicionario(self):
        dados = ['nome errado']
        with self.assertRaises(AttributeError):
            listar_nomes_personagens(dados)

    def test_lista_com_misto_de_entradas(self):
        dados = [
            {'name': 'Leia'},
            {},
            {'height': '180'},
            {'name': 'Han Solo'}
        ]
        esperado = ['Leia', None, None, 'Han Solo']
        self.assertEqual(listar_nomes_personagens(dados), esperado)

# Executar os testes
if __name__ == '__main__':
    unittest.main()