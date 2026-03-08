import pickle

def extrair_dados(dados):
    
    # Verifica se a chave 'results' existe
    if 'results' not in dados:
        raise KeyError
    
    results = dados['results']
    
    # Verifica se 'results' é uma lista
    if not isinstance(results, list):
        raise TypeError
    
    # Transforma cada personagem na lista
    resultado = []
    for personagem in results:
        # Verifica se todos os campos obrigatórios existem
        if 'id' not in personagem or 'name' not in personagem or 'species' not in personagem or 'gender' not in personagem:
            raise KeyError
        
        # Cria novo dicionário com os campos renomeados
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

# print(dados_rickandmortyapi)
print(extrair_dados(dados_rickandmortyapi))

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
        },
        {
        'id': 3, 'nome': 'Summer Smith', 'especie': 'Human', 'genero': 'Female'
        }, 
        {'id': 4, 'nome': 'Beth Smith', 'especie': 'Human', 'genero': 'Female'
        }, 
        {'id': 5, 'nome': 'Jerry Smith', 'especie': 'Human', 'genero': 'Male'}, 
        {'id': 6, 'nome': 'Abadango Cluster Princess', 'especie': 'Alien', 'genero': 'Female'
        }, 
        {'id': 7, 'nome': 'Abradolf Lincler', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 8, 'nome': 'Adjudicator Rick', 'especie': 'Human', 'genero': 'Male'
        },
        {'id': 9, 'nome': 'Agency Director', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 10, 'nome': 'Alan Rails', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 11, 'nome': 'Albert Einstein', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 12, 'nome': 'Alexander', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 13, 'nome': 'Alien Googah', 'especie': 'Alien', 'genero': 'unknown'
        }, 
        {'id': 14, 'nome': 'Alien Morty', 'especie': 'Alien', 'genero': 'Male'
        }, 
        {'id': 15, 'nome': 'Alien Rick', 'especie': 'Alien', 'genero': 'Male'
        }, 
        {'id': 16, 'nome': 'Amish Cyborg', 'especie': 'Alien', 'genero': 'Male'
        }, 
        {'id': 17, 'nome': 'Annie', 'especie': 'Human', 'genero': 'Female'
        }, 
        {'id': 18, 'nome': 'Antenna Morty', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 19, 'nome': 'Antenna Rick', 'especie': 'Human', 'genero': 'Male'
        }, 
        {'id': 20, 'nome': 'Ants in my Eyes Johnson', 'especie': 'Human', 'genero': 'Male'
        }
    ]
}

print('   ')

print(entrada.get("results"))