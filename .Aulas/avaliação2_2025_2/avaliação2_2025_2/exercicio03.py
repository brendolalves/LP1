import pickle

def search_high_values(dados):
    ''' Seu código aqui '''
    pass

def search_low_values(dados):
    ''' Seu código aqui '''
    pass

with open("exercicio03.bin", "rb") as arquivo:
    dados = pickle.load(arquivo)

# print(dados)
high = search_high_values(dados)
low = search_low_values(dados)

