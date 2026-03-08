import pickle

def extrair_dados(dados):
    ''' Seu código aqui '''
    pass

with open("exercicio01.bin", "rb") as arquivo:
    dados_rickandmortyapi = pickle.load(arquivo)

entrada = {
    "results": [
        {
            "id": 1,
            "name": "Rick Sanchez",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Male"
        },
        {
            "id": 2,
            "name": "Morty Smith",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Male"
        }
    ]
}


# print(dados_rickandmortyapi)
print(extrair_dados(dados_rickandmortyapi))