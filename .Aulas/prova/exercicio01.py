import pickle

def extrair_dados(dados):
    
    if 'results' not in dados:
        raise KeyError
    
    results = dados['results']
    
    if not isinstance(results, list):
        raise TypeError
    
    resultado = []
    for personagem in results:
        if 'id' not in personagem or 'name' not in personagem or 'species' not in personagem or 'gender' not in personagem:
            raise KeyError
        
        novo_personagem = {
            'id': personagem['id'],
            'nome': personagem['name'],
            'especie': personagem['species'],
            'genero': personagem['gender']
        }
        resultado.append(novo_personagem)
    
    return resultado

with open("exercicio01.bin", "rb") as arquivo:
    dados_rickandmortyapi = pickle.load(arquivo)

print(extrair_dados(dados_rickandmortyapi))