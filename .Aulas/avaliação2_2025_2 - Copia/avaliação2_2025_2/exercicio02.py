import pickle

def extrair_dados(lista_enderecos):
    
    # Verifica se a entrada é uma lista
    if not isinstance(lista_enderecos, list):
        raise TypeError
    
    # Processa cada endereço na lista
    resultado = []
    for endereco in lista_enderecos:
        # Verifica se todos os campos obrigatórios existem
        if 'cep' not in endereco or 'localidade' not in endereco or 'estado' not in endereco:
            raise KeyError
        
        # Cria uma tupla com os valores na ordem: (cep, localidade, estado)
        tupla_endereco = (endereco['cep'], endereco['localidade'], endereco['estado'])
        resultado.append(tupla_endereco)
    
    return resultado

with open("exercicio02.bin", "rb") as arquivo:
    dados_cep = pickle.load(arquivo)

# print(dados_cep)
print(extrair_dados(dados_cep))