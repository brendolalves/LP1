import unittest
from exercicio01 import extrair_dados

class TestExtrairDados(unittest.TestCase):

    def test_lista_com_um_personagem(self):
        entrada = {
            "results": [
                {"id": 1, "name": "Rick", "species": "Human", "gender": "Male"}
            ]
        }
        esperado = [{"id": 1, "nome": "Rick", "especie": "Human", "genero": "Male"}]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_lista_com_dois_personagens(self):
        entrada = {
            "results": [
                {"id": 1, "name": "Rick", "species": "Human", "gender": "Male"},
                {"id": 2, "name": "Morty", "species": "Human", "gender": "Male"}
            ]
        }
        esperado = [
            {"id": 1, "nome": "Rick", "especie": "Human", "genero": "Male"},
            {"id": 2, "nome": "Morty", "especie": "Human", "genero": "Male"}
        ]
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_lista_vazia(self):
        entrada = {"results": []}
        esperado = []
        self.assertEqual(extrair_dados(entrada), esperado)

    def test_ausencia_de_resultados(self):
        with self.assertRaises(KeyError):
            extrair_dados({})  # 'results' não existe

    def test_faltando_campo_id(self):
        entrada = {
            "results": [
                {"name": "Rick", "species": "Human", "gender": "Male"}
            ]
        }
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_faltando_campo_name(self):
        entrada = {
            "results": [
                {"id": 1, "species": "Human", "gender": "Male"}
            ]
        }
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_faltando_campo_species(self):
        entrada = {
            "results": [
                {"id": 1, "name": "Rick", "gender": "Male"}
            ]
        }
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_faltando_campo_gender(self):
        entrada = {
            "results": [
                {"id": 1, "name": "Rick", "species": "Human"}
            ]
        }
        with self.assertRaises(KeyError):
            extrair_dados(entrada)

    def test_tipo_errado_para_results(self):
        entrada = {"results": "Rick"}  # deveria ser uma lista
        with self.assertRaises(TypeError):
            extrair_dados(entrada)

    def test_personagem_com_valores_none(self):
        entrada = {
            "results": [
                {"id": None, "name": None, "species": None, "gender": None}
            ]
        }
        esperado = [{"id": None, "nome": None, "especie": None, "genero": None}]
        self.assertEqual(extrair_dados(entrada), esperado)

# Executar os testes
if __name__ == "__main__":
    unittest.main()
