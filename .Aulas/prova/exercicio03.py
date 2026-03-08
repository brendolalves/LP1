import pickle

def search_high_values(dados):
    
    resultado = []
    for item in dados:
        resultado.append(item['high'])
    return resultado

def search_low_values(dados):
    
    resultado = []
    for item in dados:
        resultado.append(item['low'])
    return resultado

with open("exercicio03.bin", "rb") as arquivo:
    dados = pickle.load(arquivo)

high = search_high_values(dados)
low = search_low_values(dados)