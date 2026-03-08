import pickle

def extrair_dados(lista_enderecos):
    ''' Seu código aqui '''
    pass

with open("exercicio02.bin", "rb") as arquivo:
    dados_cep = pickle.load(arquivo)

# print(dados_cep)
print(extrair_dados(dados_cep))
