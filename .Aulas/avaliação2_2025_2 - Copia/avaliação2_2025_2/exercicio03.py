import pickle

def search_high_values(dados):
    
    resultado = []
    for item in dados:
        # Acessa diretamente - se 'high' não existir em dict, raise KeyError
        # Se item não for dict (ex: string), tentar acessar ['high'] raise TypeError
        resultado.append(item['high'])
    return resultado

def search_low_values(dados):
    
    resultado = []
    for item in dados:
        # Acessa diretamente - se 'low' não existir em dict, raise KeyError
        # Se item não for dict (ex: string), tentar acessar ['low'] raise TypeError
        resultado.append(item['low'])
    return resultado

with open("exercicio03.bin", "rb") as arquivo:
    dados = pickle.load(arquivo)

# print(dados)
high = search_high_values(dados)
low = search_low_values(dados)